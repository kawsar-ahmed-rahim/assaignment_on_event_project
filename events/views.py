from django.shortcuts import render,redirect
from .import forms
from .import models
from django.contrib.auth.decorators import login_required
from .forms import EventForm2,EventForm,SearchForm

from .models import Event

@login_required
def add_event(request):
    if request.method == "POST":
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            return redirect('add_event')
    else:
        event_form = EventForm()
    return render(request,'add_events.html',{'form':event_form})
@login_required
def edit_event(request,id):
    edit = models.Event.objects.get(pk=id)
    event_form = EventForm(instance=edit)

    if request.method == "POST":
        event_form = EventForm(request.POST,instance=edit)
        if event_form.is_valid():
            event_form.save()
            return redirect("homepage")
    else:
        event_form = EventForm(instance=edit)
    return render(request,'add_events.html',{'form':event_form})

@login_required
def delete_event(request,id):
    event = models.Event.objects.get(pk=id)
    event.delete()
    return redirect('homepage')



def search(request):
    events = Event.objects.all()
    search_form = SearchForm(request.POST)
    search_term = ""
    if search_form.is_valid():
        search_term = search_form.cleaned_data["query"]
    searched_event = []
    for event in events:
        if search_term and search_term in event.category.name.lower():
            searched_event.append(event)
    context = {
        "events":searched_event,
        "search_form":search_form,
    }
    return render(request,"search_results.html",context=context)



  
