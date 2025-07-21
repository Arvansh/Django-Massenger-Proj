from django.urls import path
from . import views
urlpatterns = [
    path('', views.group_chat, name='group_chat'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout')
]
