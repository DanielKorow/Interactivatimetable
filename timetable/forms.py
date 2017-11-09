from django import forms
from .models import Band, BandReg, Repetition


class AuthorizationForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ("band_name", "password")
        widgets = ({'password': forms.PasswordInput(
            attrs={'placeholder': 'Пароль', 'class': 'form-control', 'id': 'inputPassword'}),
                    'band_name': forms.TextInput(
                        attrs={'placeholder': 'Название группы', 'class': 'form-control', 'id': 'inputLogin'})
                    })


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = BandReg
        fields = ("band_name", "password", "email")
        widgets = ({'password': forms.PasswordInput(
            attrs={'placeholder': 'Пароль', 'class': 'form-control', 'id': 'inputPassword'}),
            'band_name': forms.TextInput(
            attrs={'placeholder': 'Название группы', 'class': 'form-control', 'id': 'inputLogin'}),
            'email': forms.EmailInput(
            attrs={'placeholder': 'E-mail', 'class': 'form-control', 'id': 'inputEmail'})
        })


class CreateRep(forms.ModelForm):
    class Meta:
        model = Repetition
        fields = ("time_start", "time_end", "date")
        widgets = ({'date': forms.DateInput(attrs={'id': 'date'})})