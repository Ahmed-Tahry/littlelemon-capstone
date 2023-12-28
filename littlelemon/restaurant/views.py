from django.shortcuts import render
from .models import Menu,Booking
from rest_framework.viewsets import ModelViewSet
from.serializers import MenuSerializer,BookingSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
# Create your views here.


# Create your views here.
class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewset(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

