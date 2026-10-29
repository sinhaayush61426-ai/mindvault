import re

from django import forms
from django.contrib.auth import get_user_model

from .models import Character


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data["username"].strip()
        if get_user_model().objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(
                "Username already exists. Please choose a different one."
            )
        return username

    def clean_email(self):
        email = self.cleaned_data["email"].strip()
        if get_user_model().objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "Email already exists. Please use a different email."
            )
        return email


class ReviewForm(forms.Form):
    author_name = forms.CharField(max_length=50)
    occupation = forms.CharField(max_length=50, required=False)
    content = forms.CharField(widget=forms.Textarea, max_length=10000)


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        exclude = ["user", "created_at", "updated_at"]

    def clean_avatar_color(self):
        color = self.cleaned_data.get("avatar_color")
        if color and not re.fullmatch(r"#[0-9a-fA-F]{6}", color):
            raise forms.ValidationError("Enter a valid six-digit hex color.")
        return color
