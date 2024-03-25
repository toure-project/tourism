
from django.shortcuts import render
from .models import Location

def map_view(request):
    # Query all locations
    locations = Location.objects.all()
    return render(request, 'map/map.html', {'locations': locations})
