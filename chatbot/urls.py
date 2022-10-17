from django.urls import path
from .views import ChatBotView

app_name = 'chatbot'

urlpatterns = [
    path('', ChatBotView.as_view(), name='chatbot'),
]