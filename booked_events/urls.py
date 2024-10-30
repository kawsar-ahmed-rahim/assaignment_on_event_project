from django.urls import path
from . import views

urlpatterns = [
    path('booked_event/',views.event_page,name = "booked_event")
]