from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Event, Registration
from django.utils import timezone
from .forms import CustomUserCreationForm
from django.contrib.auth import login

def event_list(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date', 'time')
    query = request.GET.get('q')
    if query:
        events = events.filter(Q(title__icontains=query) | Q(description__icontains=query))
    
    # check if user is authenticated
    if request.user.is_authenticated:
        registrations = Registration.objects.filter(user=request.user)
    else:
        registrations = Registration.objects.filter(user=None)
    registered_event_ids = registrations.values_list('event_id', flat=True)
    
    return render(request, 'events/event_list.html', {
        'events': events,
        'registered_event_ids': registered_event_ids
    })

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if event.available_slots > 0:
        # check if user already registered for this event
        if Registration.objects.filter(user=request.user, event=event).exists():
            messages.error(request, 'You are already registered for this event.')
            return redirect('event_detail', event_id=event.id)
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

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('event_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})