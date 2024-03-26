from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
 
urlpatterns = [
    path ('', views.home, name='home'),
    path('register/', views.register_manager, name='register_manager'),
    path('login/', views.login_view, name='login'),
    path('hotel_dashboard/', views.hotel_dashboard, name='hotel_dashboard'),
    path('transport_dashboard/', views.transport_dashboard, name='transport_dashboard'),
    
]