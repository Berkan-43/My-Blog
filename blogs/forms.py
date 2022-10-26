from django import forms
from blogs.models import *
from django.core.mail import send_mail


class IletisimForm(forms.ModelForm):
    class Meta:
        model = IletisimModel
        fields = ('isim_soyisim','email', 'mesaj')

    def send_email(self, mesaj):
            send_mail(
                subject='İletişim Formundan Yeni Mesaj Var!',
                message=mesaj,
                from_email=None,
                recipient_list=['berkanyildirim1999@gmail.com'],
                fail_silently=False
            )


class YaziEkleModelForm(forms.ModelForm):
    class Meta:
        model = YazilarModel
        exclude = ('yazar', 'slug')

    def __init__(self, *args, **kwargs):
        super(YaziEkleModelForm, self).__init__(*args, **kwargs)
    
        self.fields['icerik'].widget.attrs.update({'class': 'col-sm-3'})

class YaziGuncelleModelForm(forms.ModelForm):
    class Meta:
        model = YazilarModel
        exclude = ('yazar', 'slug')


class YorumEkleModelForm(forms.ModelForm):
    class Meta:
        model = YorumModel
        fields = ('yorum',)