from django.urls import path
from . import views

urlpatterns = [
    path('reset/', views.password_reset_request, name='password_reset_request'),
    #path('reset/done/', views.password_reset_done, name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',views. password_reset_confirm, name='password_reset_confirm'),
    path('reset/complete/', views.password_reset_complete, name='password_reset_complete'),
]
