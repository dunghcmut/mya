from django.contrib.auth.models import User
from .models import BookingTable, Menu
from rest_framework import serializers
from rest_framework import permissions
from rest_framework import viewsets

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]
        permission_class = [permissions.IsAuthenticated]


class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = "__all__"



