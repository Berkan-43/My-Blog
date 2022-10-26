from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)

    class Meta:
        verbose_name='Kullanıcı'
        verbose_name_plural= 'Kullanıcılar'
