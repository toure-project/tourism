from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.feedback, name='feedback'),
    path('add_event/', views.add_event, name='add_event'),
    path('event_list/', views.event_list, name='event_list'),

]
