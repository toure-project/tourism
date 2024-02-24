from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
   path ('', views.hotel_form, name="hotel_form"),
   path ('<int:id>/', views.hotel_form, name="hotel_update"),
   path ('delete/<int:id>/', views.hotel_delete, name="hotel_delete"),
   path ('hotel_list', views.hotel_list, name="hotel_list"),

]