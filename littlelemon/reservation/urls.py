from django.contrib import admin 
from django.urls import path, include
from .views import sayHello
from . import views
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

  
urlpatterns = [ 
    # path('hello/', sayHello, name='sayHello'),
    path('', views.index, name='index'),
]