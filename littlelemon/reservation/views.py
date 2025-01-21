from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def sayHello(request):
 return HttpResponse('Hello World')

def index(request):
   return render(request, 'index.html', {})