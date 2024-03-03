from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import hotels
from .forms import hotelform



def home(request):
     return render(request, 'tourapp/index.html')


def hotel_list(request):
    context = { "hotel_list" :hotels.objects.all() }
    return render(request, 'tourapp/hotel_list.html', context)

def register_hotel(request):
    if request.method == 'POST':
        H_Name = request.POST.get('hname')
        Email = request.POST.get('email')
        Phon_Number = request.POST.get('phone')    
        H_Locaation = request.POST.get('address')
        Superior_Room = request.POST.get('sroom')
        Deluxe_Room = request.POST.get('droom')
        single_Occupation = request.POST.get('soccopation')
        Double_Occupation = request.POST.get('doccopatin')
        Photo = request.FILES['photo']
        
        new_hotel = hotels(
            H_Name=H_Name,
            Email=Email,
            Phon_Number=Phon_Number,
            H_Locaation=H_Locaation,
            Superior_Room=Superior_Room,
            Deluxe_Room=Deluxe_Room,
            single_Occupation=single_Occupation,
            Double_Occupation=Double_Occupation,
            Photo=Photo
        )
        new_hotel.save()
        return redirect('hotel_list')
    return render(request, 'tourapp/hotelregistration.html')


def delete_hotel(request, hotel_id):
    hotel_to_delete = get_object_or_404(hotels, id=hotel_id)
    hotel_to_delete.delete()
    return redirect('hotel_list')


def update_hotel(request, hotel_id):
    hotel_instance = get_object_or_404(hotels, pk=hotel_id)
    if request.method == "POST":
        form = hotelform(request.POST, request.FILES, instance=hotel_instance)
        if form.is_valid():
            form.save()
            return redirect('hotel_list')
    else:
        form = hotelform(instance=hotel_instance)
        return redirect('hotel_list')

    return render(request, 'tourapp/hotelregistration.html', {'form': form})
