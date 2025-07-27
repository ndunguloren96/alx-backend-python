# messaging_app/urls.py
"""
URL configuration for messaging_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import ( # ADD THIS LINE
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView, # Optional: For verifying tokens
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include your chats app's API URLs under the 'api/' path
    path('api/', include('chats.urls')),
    # The api-auth/ endpoint is often added globally for browsable API login/logout.
    # It's already included via 'chats.urls', but if you prefer it directly here:
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # ADD THESE LINES for JWT authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'), # Optional
]
