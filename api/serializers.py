from rest_framework import serializers
from coinapp.models import Listing


class ListingModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Listing
        fields = ("id", "category", "heading", "username")  # name', 'id')

