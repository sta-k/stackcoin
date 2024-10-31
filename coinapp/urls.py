from django.urls import path
from . import views

app_name = "coinapp"
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:user>/', views.UserDetail.as_view(), name='user_detail'),
    # path("offerings/", views.OfferingView.as_view(), name="offerings"),
    # path('ajax/load_offerings/', views.load_offerings, name='ajax_load_offerings'), 
    path('ajax/get_balance/', views.get_balance, name='ajax_get_balance'), 
]
