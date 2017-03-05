# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic


from .models import Imovel

class VendaListView(generic.ListView):
    template_name = 'venda.html'
    context_object_name = 'venda'
    paginate_by = 3

    def get_queryset(self):
        return Imovel.objects.filter(tipo_imovel='VENDA')


venda = VendaListView.as_view()

class AluguelListView(generic.ListView):
    template_name = 'aluguel.html'
    context_object_name = 'aluguel'
    paginate_by = 6

    def get_queryset(self):
        return Imovel.objects.filter(tipo_imovel='ALUGUEL')


aluguel = AluguelListView.as_view()




def imovel(request, slug):
    imovel = Imovel.objects.get(slug=slug)
    context = {
        'imovel': imovel,
    }
    return render(request, 'slide.html', context)






