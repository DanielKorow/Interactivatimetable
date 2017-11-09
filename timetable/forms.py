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
        fields = ("band_name", "password", "email", "phone")
        widgets = ({'password': forms.PasswordInput(
            attrs={'placeholder': 'Пароль', 'class': 'form-control', 'id': 'inputPassword'}),
            'band_name': forms.TextInput(
            attrs={'placeholder': 'Название группы', 'class': 'form-control', 'id': 'inputLogin'}),
            'email': forms.EmailInput(
            attrs={'placeholder': 'E-mail', 'class': 'form-control', 'id': 'inputEmail'}),
            'phone': forms.TextInput(
            attrs={'placeholder': 'Телефон', 'class': 'form-control', 'id': 'inputPhone'}),

        })


class CreateRep(forms.ModelForm):
    class Meta:
        model = Repetition
        fields = ("date", "time_start", "time_end")
        widgets = ({'date': forms.SelectDateWidget(),
                    'time_start': forms.TimeInput(attrs={'placeholder': '18:00', 'class': 'inputform'}),
                    'time_end': forms.TimeInput(attrs={'placeholder': '19:00', 'class': 'inputform'}),
                    })
