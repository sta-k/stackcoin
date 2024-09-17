from django.urls import path
from . import views

app_name = 'coinapp'
urlpatterns = [
	# if blank show districts(Thissur, palakkad...)
	path('getuser/', views.getuser, name='getuser'),	
]