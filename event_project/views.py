from django.shortcuts import render,redirect
from events.models import Event

def home(request):
    data = Event.objects.all()
    return render(request,'home.html',{'data':data})