from django import forms
from .models import Band


class AuthorizationForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ("band_name", "password")
        widgets = ({'password': forms.PasswordInput(
            attrs={'placeholder': 'Пароль', 'class': 'form-control', 'id': 'inputPassword'}),
                    'band_name': forms.TextInput(
                        attrs={'placeholder': 'Логин', 'class': 'form-control', 'id': 'inputLogin'})
                    })
