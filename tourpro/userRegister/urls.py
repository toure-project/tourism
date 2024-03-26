from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Other URL patterns
    
    
    path('user_register/', views.user_register, name='user_register'),
    path('user_login/', views.user_login, name='user_login'),
    

]