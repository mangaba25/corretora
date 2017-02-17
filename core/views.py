from django.shortcuts import render
from imovel.models import Imovel
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


