from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
   path('event_form', views.event_form, name="event_form"),
   path('event_create/',views.event_create, name='event_create'),
   path('event_form/<int:id>/', views.event_update, name="event_update"),
   path('delete/<int:id>/', views.event_delete, name="event_delete"),
   path('event_list', views.event_list, name="event_list"),

]