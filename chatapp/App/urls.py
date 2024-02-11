from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('auth/login/', views.LoginView),
    path('auth/register/', views.RegisterView),
    path('lobby/', views.lobby),
    path('logout/', views.Logout),
    path('chat/<int:room>', views.ChatView),
    path('CreateRoom/', views.CreateRoom),
    path('JoinRoom/', views.JoinRoom),
    path('send_msg/<int:room>', views.SendMessage),
    path('get_messages/', views.GetMessages, name='get_messages'),
]

