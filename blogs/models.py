from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField


# Create your models here.
class KategoriModel(models.Model):
    isim = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='isim', unique=True)

    class Meta:
        verbose_name_plural = 'Kategoriler'
        verbose_name = 'Kategori'

    def __str__(self):
        return self.isim

class DateAbstarctModel(models.Model):
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    duzenlenme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class YazilarModel(DateAbstarctModel):
    resim = models.ImageField(upload_to='yazi_resimleri')
    baslik = models.CharField(max_length=50)
    icerik = RichTextField()
    slug = AutoSlugField(populate_from = 'baslik', unique=True)
    kategoriler = models.ManyToManyField(KategoriModel, related_name='yazi')
    yazar = models.ForeignKey('accound.CustomUserModel', on_delete=models.CASCADE ,related_name='yazilar')

    class Meta:
        verbose_name='Yazi'
        verbose_name_plural = 'Yazilar'

    def __str__(self):
        return self.baslik

class YorumModel(DateAbstarctModel):
    yazan = models.ForeignKey('accound.CustomUserModel', on_delete=models.CASCADE, related_name='yorum')
    yazi = models.ForeignKey(YazilarModel, on_delete=models.CASCADE, related_name='yorumlar')
    yorum = models.TextField()
    slug = AutoSlugField(populate_from = 'yorum', unique=True)

    class Meta:
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'

    def __str__(self):
        return self.yazan.username

class IletisimModel(models.Model):
    email = models.EmailField(max_length=250)
    isim_soyisim = models.CharField(max_length=150)
    mesaj = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişim'

    def __str__(self):
        return self.email

