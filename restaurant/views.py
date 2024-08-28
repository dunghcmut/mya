from django.shortcuts import render
from .models import BookingTable, Menu
from .Serializers import MenuSerializers, BookingSerializers
from rest_framework import generics, viewsets, permissions  # Import generics
from rest_framework.decorators import api_view


# Create your views here.
def index(request):
    return render(request, "index.html", {})


class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers


class MenuSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers


class BookingTableView(generics.ListCreateAPIView):
    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializers


class BookingSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializers


class BookingViewSet(viewsets.ModelViewSet):
    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [permissions.IsAuthenticated]
