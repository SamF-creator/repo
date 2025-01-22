from django.contrib import admin
from rest_framework.authtoken.models import Token
from .models import Menu, Booking

# Register your models here.
admin.site.register(Menu)
admin.site.register(Booking)
admin.site.register(Token)