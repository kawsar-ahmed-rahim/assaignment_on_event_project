from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, Booking

@login_required
def book_event(request, event_id):
    event = Event.objects.get(id=event_id)
    Booking.objects.get_or_create(user=request.user, event=event)
    return redirect('booked_event')
@login_required
def event_page(request):
    events = Event.objects.all()
    booked_events = Booking.objects.filter(user=request.user).values_list('event_id', flat=True) if request.user.is_authenticated else []
    return render(request, 'booked_events.html', {'events': events, 'booked_events': booked_events})

