from re import template
from django.urls import path
from blogs.views import *
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    
    path('iletisim',iletisim, name='iletisim'),
    path('gonderildi/',gonderildi, name='gonderildi'),
    path('yonlendir/',RedirectView.as_view(
        url='https://www.google.com'
    ), name='yonlendir'),
    path('hakkinda/',TemplateView.as_view(
        template_name='hakkinda.html'
    ), name='hakkinda'),
    path("yazilarim/", yazilarim, name='yazilarim'),
    path("kategori/<slug:kategoriSlug>", kategori, name='kategori'),
    path("detay/<slug:slug>", detay, name='detay'),
    path("yazi-ekle/", yazi_ekle, name='yazi-ekle'),
    path("yazi-guncelle/<slug:slug>", yazi_guncelle, name='yazi-guncelle'),
    path("yazi-sil/<slug:slug>", yazi_sil, name='yazi-sil'),
    path("yorum-sil/<int:id>", yorum_sil, name='yorum-sil'),
]