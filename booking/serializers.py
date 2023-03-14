from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Booking


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class CreateBooking(serializers.ModelSerializer):
    # client = UserInfoSerializer()

    class Meta:
        model = Booking
        fields = (
            "client",
            "date",
            "time",
            "persons")


class GetBooking(serializers.ModelSerializer):
    client = UserInfoSerializer()

    class Meta:
        model = Booking
        fields = ("id",
                  "client",
                  "date",
                  "time",
                  "persons")

