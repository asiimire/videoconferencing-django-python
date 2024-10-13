from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('join/', views.join, name='join'),
    path('meeting/', views.videocall, name='meeting'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]