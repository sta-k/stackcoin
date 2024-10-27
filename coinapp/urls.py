from django.urls import path
from . import views

app_name = "coinapp"
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path("offerings/", views.OfferingView.as_view(), name="offerings"),
    path('ajax/load_offerings/', views.load_offerings, name='ajax_load_offerings'), 
]
