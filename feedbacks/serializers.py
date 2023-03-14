from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Feedbacks


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class FeedbacksListSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Feedbacks
        fields = (
            "id",
            "author",
            "create_date",
            "text",
            "status"
        )


class FeedbacksCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedbacks
        fields = (
            "author",
            "text"
        )
