from django.shortcuts import render
from imovel.models import Imovel, Image
# Create your views here.
def index(request):
	tres = Imovel.objects.filter(book_type='1')[:3]
	dois = Imovel.objects.filter(book_type='1').order_by('-id')[0]
	dois_ = Imovel.objects.filter(book_type='1').order_by('-id')[1]
	context = {
		'tres': tres,
		'dois': dois,
		'dois_':dois_,
	}
	return render(request, 'index.html', context)


def aluguel(request):
	return render(request, 'aluguel.html')

def venda(request):
	return render(request, 'venda.html')

def slide(request):
	return render(request, 'slide.html')


