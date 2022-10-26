from django.shortcuts import render, get_object_or_404, redirect
from accound.models import CustomUserModel
from blogs.models import *
from blogs.forms import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.views.generic import FormView
import logging

# Create your views here.


def anasayfa(request):
    sorgu = request.GET.get('sorgu')
    yazilar = YazilarModel.objects.order_by('-id')
    if sorgu:
        yazilar = yazilar.filter(
            Q(baslik__icontains=sorgu)|
            Q(icerik__icontains=sorgu)
        ).distinct()
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar, 4)

    context = {
        'yazilar':paginator.get_page(sayfa)
    }
    return render(request, 'anasayfa.html', context)


""" class IletisimFormView(FormView):
    template_name = 'iletisim.html'
    form_class = IletisimForm
    success_url = 'email-gonderildi/'

    def form_valid(self, form):
        form.save()
        form.send_email(mesaj=form.cleaned_data.get('mesaj'))
        return super().form_valid(form) """


def gonderildi(request):
    messages.success(request, 'E-mail Başarıyla Gönderildi.')
    return render(request, 'email-gonderildi.html')


def iletisim(request):
    form = IletisimForm()
    if request.method == 'POST':
        form = IletisimForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gonderildi')
    context = {
        'form':form
    } 
    return render(request, 'iletisim.html', context)


def kategori(request, kategoriSlug):
    kategori = get_object_or_404(KategoriModel, slug=kategoriSlug)
    yazilar = kategori.yazi.order_by('-id')
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar, 2)
    context = {
        'yazilar':paginator.get_page(sayfa),
        'kategori_isim':kategori.isim
    }
    return render(request, 'kategori.html', context)


@login_required(login_url='/')
def yazilarim(request):
    yazilar = request.user.yazilar.order_by('-id')
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar, 5)
    context = {
        'yazilar':paginator.get_page(sayfa)
    }
    return render(request, 'yazilarim.html', context)


logger = logging.getLogger('konu_okuma')
def detay(request, slug):
    yazi = get_object_or_404(YazilarModel, slug=slug)
    if request.user.is_authenticated:
        logger.info('konu okundu!' + request.user.username)
    yorumlar = yazi.yorumlar.all()

    if request.method == 'POST':
        yorum_ekle_form = YorumEkleModelForm(request.POST)
        if yorum_ekle_form.is_valid():
            yorum = yorum_ekle_form.save(commit=False)
            yorum.yazan = request.user
            yorum.yazi = yazi
            yorum.save()
    yorum_ekle_form = YorumEkleModelForm()
    context = {
        'yazi':yazi,
        'yorumlar':yorumlar,
        'yorum_ekle_form':yorum_ekle_form,
    }
    return render(request, 'detay.html', context)


@login_required(login_url='/')
def yazi_ekle(request):
    form = YaziEkleModelForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        yazi = form.save(commit=False)
        yazi.yazar = request.user
        yazi.save()
        form.save_m2m()
        return redirect('detay', slug=yazi.slug)
    context = {
        'form':form
    }
    return render(request, 'yazi-ekle.html', context)


@login_required(login_url='/')
def yazi_guncelle(request, slug):
    yazi = get_object_or_404(YazilarModel, slug=slug, yazar=request.user)
    form = YaziGuncelleModelForm(request.POST or None, files=request.FILES or None, instance=yazi)
    if form.is_valid():
        form.save()
        return redirect('detay', slug=yazi.slug)
    concext = {
        'form':form
    }
    return render(request, 'yazi-guncelle.html', concext)


@login_required(login_url='/')
def yazi_sil(request, slug):
    get_object_or_404(YazilarModel, slug=slug, yazar=request.user).delete()
    return redirect('yazilarim')


@login_required(login_url='/')
def yorum_sil(request, id):
    yorum = get_object_or_404(YorumModel, id=id)
    if yorum.yazan == request.user or yorum.yazi.yazar == request.user:
        yorum.delete()
        messages.success(request, 'Yorum başarıyla silindi.')
        return redirect('detay', slug=yorum.yazi.slug)
    return redirect('anasayfa')

