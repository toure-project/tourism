from django.shortcuts import render, redirect
from  django.contrib.auth.forms import UserCreationForm
from .forms import hotelform
from .forms import hotels



def hotel_list(request):
    context = { "hotel_list" :hotels.objects.all() }
    return render(request, 'frontend/hotel_list.html', context)



def hotel_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = hotelform()
        else:
            form = hotelform(instance=hotels.objects.get(pk=id))
        return render(request, 'frontend/hotel_form.html', {'form': form})
    else:
        if id == 0:
            form = hotelform(request.POST)
        else:
            form = hotelform(request.POST, instance=hotels.objects.get(pk=id))

        if form.is_valid():
            form.save()
        return redirect('hotel_list')
    


def hotel_delete(request, id):
    hotels.objects.get(pk=id).delete()
    return redirect('hotel_list')

