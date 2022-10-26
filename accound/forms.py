from dataclasses import fields
from django.contrib.auth.forms import UserChangeForm
from accound.models import *
from django.contrib.auth.forms import UserCreationForm

class ProfilDuzenleForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUserModel
        fields = ('email', 'first_name', 'last_name', 'avatar')

class KayitForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
            )

