from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from imovel.models import Imovel
from .forms import ContactForm

def index(request):
	tres = Imovel.objects.filter(tipo_imovel='VENDA')[:3]
	um = Imovel.objects.first()
	dois = Imovel.objects.filter(tipo_imovel='ALUGUEL').order_by('-id')[0]
	dois_ = Imovel.objects.filter(tipo_imovel='ALUGUEL').order_by('-id')[1]
	context = {
		'tres': tres,
		'um':um,
		'dois': dois,
		'dois_':dois_,
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


