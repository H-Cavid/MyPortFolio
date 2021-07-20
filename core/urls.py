from django.urls import path
from .views import HomeTemplateView,send_gmail

urlpatterns = [
    path('', HomeTemplateView.as_view()),
    path('send_gmail/',send_gmail,name="send_gmail"),
]