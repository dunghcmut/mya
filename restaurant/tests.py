from django.test import TestCase
from .models import Menu  # Assuming Menu is a model, not a view


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Icecream", price=20, inventory=10)
        self.assertEqual(str(item), "Icecream : 20")
