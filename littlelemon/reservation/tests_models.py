# tests/test_models.py

from django.test import TestCase
from reservation.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        # Create a Menu object
        item = Menu.objects.create(title="Tiramisu", price=40, inventory=100)

        # Assert that the string representation of the Menu item is as expected
        self.assertEqual(str(item), "Tiramisu : 40")
