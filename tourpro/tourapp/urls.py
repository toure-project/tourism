from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name='home'),
    path('register_hotel/',views.register_hotel, name='register_hotel'),
    path ('hotel_list', views.hotel_list, name="hotel_list"),
    path('delete/<int:hotel_id>/',views.delete_hotel, name='delete_hotel'),
    path('update/<int:hotel_id>/', views.update_hotel, name='update_hotel'),
]
