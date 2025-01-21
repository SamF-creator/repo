from django.http import HttpResponse
from rest_framework import permissions
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import viewsets
from .models import Menu, Booking, User
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here. 

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]