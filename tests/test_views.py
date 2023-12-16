from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='lltestuser', password='testuser@123!')
        self.item01 = Menu.objects.create(title='Sandwich', price=60, inventory=50)
        self.item02 = Menu.objects.create(title='Doughnut', price=85, inventory=30)

    def test_getall(self):
        self.client.login(username='lltestuser', password='testuser@123!')
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        menu = Menu.objects.all()
        serializer = MenuItemSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)