from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Offering

User = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2")


class OfferingForm(forms.ModelForm):
    class Meta:
        model = Offering
        fields = '__all__'

