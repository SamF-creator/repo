# tests/test_views.py

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu
from .serializers import MenuSerializer
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create a few test instances of the Menu model
        Menu.objects.create(title="Burger", price=5.99, inventory=10)
        Menu.objects.create(title="Pizza", price=8.99, inventory=15)
        Menu.objects.create(title="Pasta", price=7.99, inventory=8)
        
        # Initialize the client and authenticate the user
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')

    def test_get_all(self):
        url = reverse('menu-list')  # This should match the correct URL pattern
        response = self.client.get(url)

        # Retrieve all Menu objects and serialize them
        menu_items = Menu.objects.all()
        serialized_data = MenuSerializer(menu_items, many=True).data

        # Assert that the response status is OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the serialized data equals the response data
        self.assertEqual(response.data, serialized_data)
