from django.urls import path
from .views import chat_view, get_or_create_chatroom, chat_view

urlpatterns = [
    path('', chat_view, name='home'),  # For the root path
    path('chat/<username>/', get_or_create_chatroom, name="start-chat"),
    path('chat/room/<chatroom_name>', chat_view, name="chatroom"),
]
