from django.urls import path
from . import views

app_name = "coinapp"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("users/", views.ExchangeView.as_view(), name="exchange_list"),
    path("users/<str:exchange>/", views.UserList.as_view(), name="user_list"),
    path(
        "users/<str:exchange>/<int:user>/",
        views.UserDetail.as_view(),
        name="user_detail",
    ),
    path("ajax/get_balance/", views.get_balance, name="ajax_get_balance"),
]
