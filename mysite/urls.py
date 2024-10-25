
from django.contrib import admin
from django.urls import path, include
from coinapp.views import SignUpView,HomeView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    # path('coinapp/', include('coinapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
]
