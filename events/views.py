from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Event, Registration
from django.utils import timezone

def event_list(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date', 'time')
    query = request.GET.get('q')
    if query:
        events = events.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if event.available_slots > 0:
        Registration.objects.get_or_create(user=request.user, event=event)
        event.available_slots -= 1
        event.save()
        messages.success(request, 'You have successfully registered for this event.')
    else:
        messages.error(request, 'Sorry, this event is full.')
    return redirect('event_detail', event_id=event.id)

@login_required
def unregister_from_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    registration = Registration.objects.filter(user=request.user, event=event).first()
    if registration:
        registration.delete()
        event.available_slots += 1
        event.save()
        messages.success(request, 'You have successfully unregistered from this event.')
    else:
        messages.error(request, 'You are not registered for this event.')
    return redirect('event_detail', event_id=event.id)

@login_required
def user_dashboard(request):
    registrations = Registration.objects.filter(user=request.user).select_related('event')
    return render(request, 'events/user_dashboard.html', {'registrations': registrations})