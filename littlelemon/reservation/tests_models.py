# tests/test_models.py

from django.test import TestCase
from reservation.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        
        item = Menu.objects.create(title="Tiramisu", price=40, inventory=100)

        self.assertEqual(str(item), "Tiramisu : 40")
