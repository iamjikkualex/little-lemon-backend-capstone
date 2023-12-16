from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.item01 = Menu.objects.create(title='Sandwich', price=60, inventory=50)
        self.item02 = Menu.objects.create(title='Doughnut', price=85, inventory=30)

    def test_getall(self):
        response = self.client.get(reverse('menu'))
        menu = Menu.objects.all()
        serializer = MenuItemSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)