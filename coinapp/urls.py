from django.urls import path
from . import views

app_name = "coinapp"
urlpatterns = [
    path("", views.transaction_view, name="home"), # HomeView.as_view()
    path("users/", views.ExchangeView.as_view(), name="exchange_list"),
    path("users/<str:exchange>/", views.UserList.as_view(), name="user_list"),
    path(
        "users/<str:exchange>/<int:user>/",
        views.UserDetail.as_view(),
        name="user_detail",
    ),
    path("ajax/<str:purpose>/", views.ajax_get_view, name="ajax_get"),
]
