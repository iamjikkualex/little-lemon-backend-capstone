from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('api-token-auth/', obtain_auth_token),
]