from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

## Inherent the User Creation Form
class UserRegisterForm(UserCreationForm):

	## Adding the Email field to the User Creation Form
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]



## Updaate the User Information
class UserUpdateForm(forms.ModelForm):
	## Adding the Email field to the User Creation Form
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ["image"]

