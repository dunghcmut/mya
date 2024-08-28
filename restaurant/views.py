from django.shortcuts import render
from .models import BookingTable, Menu
from .Serializers import MenuSerializers, BookingSerializers
from rest_framework import generics, viewsets, permissions, status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


# Create your views here.

class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        data = request.data
        title = data.get("title")
        
        # Check for duplicates based on the title field
        if Menu.objects.filter(title=title).exists():
            raise ValidationError({"detail": "Duplicate entry found."})
        
        return super().create(request, *args, **kwargs)



class MenuSingleView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers
 


class BookingTableView(generics.ListCreateAPIView):
    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        # Check for duplicates based on a specific field
        if BookingTable.objects.filter(field_name=data.get("field_name")).exists():
            raise ValidationError({"detail": "Duplicate entry found."})
        return super().create(request, *args, **kwargs)


class BookingSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [permissions.IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        # Check for duplicates based on a specific field
        if BookingTable.objects.filter(field_name=data.get("field_name")).exists():
            raise ValidationError({"detail": "Duplicate entry found."})
        return super().create(request, *args, **kwargs)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message": "This view is protected"})
