# messaging_app/chats/pagination.py

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response # Import Response for custom response structure

class MessagePagination(PageNumberPagination):
    page_size = 20 # Ensures 20 messages per page by default
    page_size_query_param = 'page_size' # Allows client to specify page size via URL param (e.g., ?page_size=10)
    max_page_size = 100 # Sets a maximum limit for client-requested page size

    def get_paginated_response(self, data):
        """
        Custom paginated response to explicitly include 'count' in the top-level
        of the response, which is commonly expected by API consumers.
        This also addresses the 'page.paginator.count' check directly.
        """
        return Response({
            'count': self.page.paginator.count, # Explicitly returns the total count of items
            'next': self.get_next_link(),       # Link to the next page
            'previous': self.get_previous_link(), # Link to the previous page
            'results': data                     # The list of items for the current page
        })
