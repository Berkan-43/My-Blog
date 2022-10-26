from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from accound.forms import *
from django.contrib.auth import login, authenticate
from django.views.generic import DetailView

# Create your views here.

def cikis(request):
    logout(request)
    return redirect('anasayfa')

@login_required(login_url='/')
def sifre_degistir(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            kullanici = form.save()
            update_session_auth_hash(request, kullanici)
            messages.success(request, 'Şifre başarıyla güncellendi.')
            return redirect('sifre-degistir')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
    }
    return render(request, 'sifre_degistir.html', context)


@login_required(login_url='/')
def profil_duzenle(request):
    if request.method == 'POST':
        form = ProfilDuzenleForm(request.POST,  request.FILES, instance = request.user) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil bilgileri başarıyla güncellendi.')
    else:
        form = ProfilDuzenleForm( instance = request.user)
    return render(request, 'profil-duzenle.html', context={
        'form':form
    })


def kayit(request):
    if request.method == 'POST':
        form = KayitForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('anasayfa')
    else:
        form = KayitForm()
    return render(request, 'kayit.html', context={
        'form':form
    })

class ProfilDetailView(DetailView):
    template_name = 'profil.html'
    context_object_name = 'profil'

    def get_object(self):
        return get_object_or_404(
            CustomUserModel, username=self.kwargs.get('username')
        )