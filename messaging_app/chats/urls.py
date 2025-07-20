from django.urls import path, include
from rest_framework_nested import routers
from .views import ConversationViewSet, MessageViewSet, UserViewSet

# Create a root router for top-level viewsets
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Create a nested router for messages within conversations
# This creates URLs like /conversations/{conversation_pk}/messages/
conversations_router = routers.NestedDefaultRouter(router, r'conversations', lookup='conversation')
conversations_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    # Include the main router URLs
    path('', include(router.urls)),
    # Include the nested router URLs
    path('', include(conversations_router.urls)),
    # Optional: DRF browsable API login/logout views
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
