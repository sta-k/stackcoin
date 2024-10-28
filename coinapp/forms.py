from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
# from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms

User = get_user_model()

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        validators=[RegexValidator(r'^\d{10}$',message="Please enter a valid 10 digit mobile number.")],
        help_text="Enter your 10 digit mobile number.",
        # error_messages={
        #     # 'required': 'Please enter your 10 digit mobile number.',
        #     # 'max_length': 'Mobile number must be .',
        #     # 'invalid': 'Please enter a valid mobile number.',
        # }
    )
    tandc = forms.BooleanField(label="Terms and Conditions.")
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name","password1", "password2","offerings","tandc")
        