# coding=utf-8

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from imovel.models import Imovel
from .models import Capa
from .forms import ContactForm

def index(request):
	recentes_a_venda = Imovel.objects.filter(tipo_imovel='VENDA')
	recentes_para_aluguel = Imovel.objects.filter(tipo_imovel='ALUGUEL')
	capa = Capa.objects.first()
	context = {
		'recentes_a_venda': recentes_a_venda,
		'recentes_para_aluguel': recentes_para_aluguel,
		'capa': capa,
	}
	return render(request, 'index.html', context)


def aluguel(request):
	return render(request, 'aluguel.html')

def contato(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
        # return redirect('contato')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contato.html', context)


