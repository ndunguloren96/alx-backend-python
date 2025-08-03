from django.urls import path
from . import views

urlpatterns = [
    path('delete-account/', views.delete_user_account, name='delete_user_account'),
    path('home/', views.home, name='home'), # A simple home view
    path('conversations/', views.conversation_view, name='conversation_list'), # For unread messages and general list
    path('conversations/<int:message_id>/', views.conversation_view, name='conversation_detail'), # For threaded messages
]
