from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone  # Import timezone module
from .forms import EventForm
from .models import Event
from .models import Feedback

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        feedback_message = request.POST.get('feedback_message')
        
        Feedback.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            feedback_message=feedback_message
        )
        
        # Add a success message
        messages.success(request, 'Thank you for your feedback!')
        
        # Redirect back to the same page
        return redirect('feedback')
    
    return render(request, 'feed_event/feedback.html')





def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'feed_event/add_event.html', {'form': form})

def event_list(request):
    # Delete expired events
    Event.objects.filter(expiration_date__lte=timezone.now()).delete()
    events = Event.objects.all()
    return render(request, 'feed_event/event_list.html', {'events': events})
