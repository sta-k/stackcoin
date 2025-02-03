from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'api'

router = DefaultRouter()
router.register('listings', views.ListingModelViewSet, basename='listing-api')

urlpatterns = [    
    path('', include(router.urls)),
    
]
