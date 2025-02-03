from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from coinapp.models import Listing
from .serializers import ListingModelSerializer

class ListingModelViewSet(ModelViewSet):
    queryset = Listing.objects.all()[:10]
    serializer_class = ListingModelSerializer
    allowed_methods = ('GET', 'HEAD', 'OPTIONS') # 'POST', 
    # permission_classes = [IsAuthenticated]