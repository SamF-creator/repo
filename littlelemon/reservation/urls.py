#urls.py (app)
from django.contrib import admin 
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import MenuViewSet, BookingViewSet
from rest_framework.authtoken.views import obtain_auth_token
from .views import MenuViewSet, BookingViewSet, UserViewSet
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('msg/', views.msg, name='msg'),
    path('api-token-auth/', obtain_auth_token),
]

  