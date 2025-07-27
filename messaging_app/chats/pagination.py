# messaging_app/chats/pagination.py

from rest_framework.pagination import PageNumberPagination

class MessagePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size' # Allows client to override page size using ?page_size=X
    max_page_size = 100 # Maximum page size allowed for client override
