from django.shortcuts import render, get_object_or_404
from .models import Car

# Create your views here.
def cars(request):
    return render(request, 'car/car.html')

def car_details(request):
    single = get_object_or_404(Car, pk=id)
    data = {
        'single_car': single
    }
    return render(request, 'car/car_details.html', data)