from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(KategoriModel)

@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    search_fields = (
        'baslik', 
        'icerik',
    )

    list_display = (
        'baslik',
        'olusturulma_tarihi',
        'duzenlenme_tarihi',
    )

@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    list_display = (
        'yazan',
        'olusturulma_tarihi',
        'duzenlenme_tarihi',
    )
    search_fields = (
        'yazan__username',
    )

@admin.register(IletisimModel)
class İletisimAdmin(admin.ModelAdmin):
    list_display = (
        'isim_soyisim',
        'email',
        'olusturulma_tarihi',
    )
    search_fields = (
        'email',
        'isim_soyisim',
    )