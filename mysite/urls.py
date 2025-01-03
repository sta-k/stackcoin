from django.contrib import admin
from django.urls import path, include
from coinapp.views import SignUpJoinView, SignUpNewView

from django.views.generic import TemplateView


urlpatterns = [
    path("", include("coinapp.urls")),
    path("admin/", admin.site.urls),
    # path("about/", about_view, name='about'), #TemplateView.as_view(template_name="about.html"), name='about'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup_join/", SignUpJoinView.as_view(), name="signup_join"),
    path("accounts/signup_new/", SignUpNewView.as_view(), name="signup_new"),
]
