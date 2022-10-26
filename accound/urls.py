from django.urls import path
from accound.views import *
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
urlpatterns = [
     path('giris/', auth_views.LoginView.as_view(
        template_name = 'giris.html'
    ), name='giris'),
    path('cikis', cikis, name='cikis'),
    path('sifre-degistir/', sifre_degistir, name='sifre-degistir'),
    path('profil-duzenle/', profil_duzenle, name='profil-duzenle'),
    path('kayit/', kayit, name='kayit'),
    path('kullanici/<str:username>', ProfilDetailView.as_view(), name='profil'),
    path('email-gonderildi/', TemplateView.as_view(
        template_name = 'email-gonderildi.html'
    ), name='email-gonderildi')
]