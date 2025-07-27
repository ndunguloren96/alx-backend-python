import logging
from datetime import datetime, time, timedelta
from django.http import HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import render

# Get a logger instance for request logging
request_logger = logging.getLogger('request_logger')

# This is a simple message box function to replace alert()
# In a real application, you would render a template with the message.
def message_box(request, message, status_code=200):
    """
    Renders a simple HTML page with a message.
    Used to replace alert() for displaying errors or confirmations.
    """
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Access Denied</title>
        <style>
            body {{ font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f0f0f0; margin: 0; }}
            .message-container {{ background-color: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: center; max-width: 400px; }}
            h1 {{ color: #dc3545; }}
            p {{ color: #666; }}
            a {{ display: inline-block; margin-top: 20px; padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px; }}
            a:hover {{ background-color: #0056b3; }}
        </style>
    </head>
    <body>
        <div class="message-container">
            <h1>Access Denied</h1>
            <p>{message}</p>
            <a href="/chats/">Go Back</a>
        </div>
    </body>
    </html>
    """
    return HttpResponseForbidden(html_content, status=status_code)


class RequestLoggingMiddleware:
    """
    Middleware to log each user's requests to a file.
    Logs timestamp, user (or 'Anonymous'), and request path.
    """
    def __init__(self, get_response):
        """
        Initializes the middleware.
        `get_response` is a callable that takes a request and returns a response.
        """
        self.get_response = get_response
        request_logger.info("RequestLoggingMiddleware initialized.")

    def __call__(self, request):
        """
        Processes the incoming request and logs information.
        """
        # Get the user; if not authenticated, default to 'Anonymous'
        user = request.user.username if request.user.is_authenticated else 'Anonymous'
        
        # Log the request information
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        request_logger.info(log_message)

        # Pass the request to the next middleware or view
        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    """
    Middleware to restrict access to the messaging app during certain hours.
    Access is allowed only between 6 PM (18:00) and 9 PM (21:00).
    Outside this window, a 403 Forbidden response is returned.
    """
    def __init__(self, get_response):
        """
        Initializes the middleware.
        """
        self.get_response = get_response
        self.allowed_start_time = time(18, 0) # 6 PM
        self.allowed_end_time = time(21, 0)   # 9 PM
        request_logger.info(f"RestrictAccessByTimeMiddleware initialized. Access allowed between {self.allowed_start_time} and {self.allowed_end_time}.")

    def __call__(self, request):
        """
        Checks the current server time and denies access if outside the allowed window.
        """
        current_time = datetime.now().time()

        # Check if the current time is within the allowed window
        if not (self.allowed_start_time <= current_time < self.allowed_end_time):
            # If outside the allowed window, return a 403 Forbidden response
            message = (f"Access to the chat is restricted. "
                       f"Please try again between {self.allowed_start_time.strftime('%I:%M %p')} and {self.allowed_end_time.strftime('%I:%M %p')}.")
            return message_box(request, message, 403)

        # If within the allowed window, proceed to the next middleware or view
        response = self.get_response(request)
        return response


class OffensiveLanguageMiddleware:
    """
    Middleware to implement rate limiting for chat messages (POST requests).
    Limits users to 5 messages per minute per IP address.
    If the limit is exceeded, a 403 Forbidden response is returned.
    """
    # Stores message counts and timestamps for each IP address
    # Format: {'ip_address': [{'timestamp': datetime_obj}, ...]}
    MESSAGE_COUNTS = {}
    RATE_LIMIT_MESSAGES = 5
    RATE_LIMIT_WINDOW_SECONDS = 60 # 1 minute

    def __init__(self, get_response):
        """
        Initializes the middleware.
        """
        self.get_response = get_response
        request_logger.info(f"OffensiveLanguageMiddleware initialized. Rate limit: {self.RATE_LIMIT_MESSAGES} messages per {self.RATE_LIMIT_WINDOW_SECONDS} seconds.")

    def __call__(self, request):
        """
        Tracks POST requests from each IP address and enforces rate limiting.
        """
        if request.method == 'POST':
            # Get the client's IP address
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip_address = x_forwarded_for.split(',')[0]
            else:
                ip_address = request.META.get('REMOTE_ADDR')

            current_time = datetime.now()

            # Clean up old entries for this IP
            if ip_address not in self.MESSAGE_COUNTS:
                self.MESSAGE_COUNTS[ip_address] = []
            
            # Remove timestamps older than the rate limit window
            self.MESSAGE_COUNTS[ip_address] = [
                t for t in self.MESSAGE_COUNTS[ip_address]
                if current_time - t < timedelta(seconds=self.RATE_LIMIT_WINDOW_SECONDS)
            ]

            # Check if the message limit has been exceeded
            if len(self.MESSAGE_COUNTS[ip_address]) >= self.RATE_LIMIT_MESSAGES:
                message = (f"You have exceeded the message limit of {self.RATE_LIMIT_MESSAGES} messages "
                           f"per {self.RATE_LIMIT_WINDOW_SECONDS} seconds. Please wait before sending more messages.")
                request_logger.warning(f"Rate limit exceeded for IP: {ip_address}")
                return message_box(request, message, 403)
            
            # If not exceeded, record the current message
            self.MESSAGE_COUNTS[ip_address].append(current_time)
            request_logger.info(f"Message count for {ip_address}: {len(self.MESSAGE_COUNTS[ip_address])}")

        # Pass the request to the next middleware or view
        response = self.get_response(request)
        return response


class RolePermissionMiddleware:
    """
    Middleware to enforce chat user role permissions.
    Only users with 'admin' or 'moderator' roles can access POST requests (sending messages).
    For demonstration, we'll assume a `role` attribute on the `request.user` object.
    In a real application, this would typically involve a custom user profile or a permissions system.
    """
    def __init__(self, get_response):
        """
        Initializes the middleware.
        """
        self.get_response = get_response
        self.allowed_roles = ['admin', 'moderator']
        request_logger.info(f"RolePermissionMiddleware initialized. Allowed roles for POST: {', '.join(self.allowed_roles)}.")

    def __call__(self, request):
        """
        Checks the user's role before allowing access to specific actions (POST requests).
        """
        # We only apply this restriction to POST requests (e.g., sending messages)
        # GET requests (viewing chat) are generally allowed for all authenticated users.
        if request.method == 'POST':
            if not request.user.is_authenticated:
                # If not authenticated, they can't have a role, so deny.
                return message_box(request, "You must be logged in to send messages.", 403)
            
            # For demonstration, we'll check a 'role' attribute on the user object.
            # In a real application, you might use:
            # - request.user.is_staff or request.user.is_superuser
            # - A custom user model or user profile with a 'role' field
            # - Django's permission system (e.g., user.has_perm('chats.can_post_message'))
            
            # Mocking a role for demonstration if it doesn't exist.
            # In a real app, ensure your User model or profile has a 'role' field.
            user_role = getattr(request.user, 'role', 'user') # Default to 'user' if no role attribute
            
            if user_role not in self.allowed_roles:
                message = f"Your role ('{user_role}') does not have permission to perform this action. Only {', '.join(self.allowed_roles)} can send messages."
                request_logger.warning(f"Role permission denied for user: {request.user.username} (Role: {user_role})")
                return message_box(request, message, 403)

        # If the request is not a POST, or if the user has the required role, proceed
        response = self.get_response(request)
        return response


