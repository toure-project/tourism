from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import eventform
from .models import Events

def event_list(request):
    context = {"event_list": Events.objects.all()}
    return render(request, 'tourapp/event_list.html', context)

def event_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = eventform()
        else:
            event = Events.objects.get(pk=id)
            form = eventform(instance=event)
        return render(request, 'tourapp/event_form.html', {'form': form})
    else:
        if id == 0:
            form = eventform(request.POST)
        else:
            event = Events.objects.get(pk=id)
            form = eventform(request.POST, instance=event)

        if form.is_valid():
            form.save()
        return redirect('event_list')
    
def event_create(request):
    if request.method == "POST":
        form = eventform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = eventform()

    return render(request, 'tourapp/event_form.html', {'form': form})
def event_delete(request, id):
    event = Events.objects.get(pk=id)
    event.delete()
    return redirect('event_list')
def event_update(request, id):
    event = Events.objects.get(pk=id)

    if request.method == "POST":
        form = eventform(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = eventform(instance=event)

    return render(request, 'tourapp/event_form.html', {'form': form})