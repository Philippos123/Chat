from django.urls import path
from .views import *

urlpatterns = [
    path('', chat_view, name='home'),  # Hantera tomma sökvägen "/"
    path('<str:group_name>/', chat_view, name='chat'),

]
