from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms

User = get_user_model()

class SignUpForm(UserCreationForm):
    username = forms.IntegerField(
        validators=[MinValueValidator(6000000000), MaxValueValidator(9999999999)],
        help_text="Enter your 10 digit mobile number.",
        error_messages={
            'required': 'Please enter your 10 digit mobile number.',
            # 'max_length': 'Mobile number must be .',
            'invalid': 'Please enter a valid mobile number.',
        }
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name","password1", "password2","offerings")
        