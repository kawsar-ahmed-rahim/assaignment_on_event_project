from django.urls import path
from . import views

urlpatterns = [
    path('add_event/',views.add_event,name = "add_event"),
    path('edit/<int:id>',views.edit_event,name = "edit_event"),
    path('delete/<int:id>',views.delete_event,name = "delete_event"),
    path('search/', views.search, name='search'),


]