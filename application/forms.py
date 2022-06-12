from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Color, User


class EquationForm(forms.Form):
    a_var = forms.FloatField(required=True)
    b_var = forms.FloatField(required=True)
    c_var = forms.FloatField(required=True)


class GuessColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ("number",)


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email")
