# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic


from .models import Imovel

class VendaListView(generic.ListView):
    model = Imovel
    template_name = 'venda.html'
    context_object_name = 'object_list'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(VendaListView, self).get_context_data(**kwargs)
        context['venda'] = Imovel.objects.filter(tipo_imovel='VENDA')
        return context

venda = VendaListView.as_view()

class AluguelListView(generic.ListView):
    model = Imovel
    template_name = 'aluguel.html'
    context_object_name = 'object_list'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(AluguelListView, self).get_context_data(**kwargs)
        context['aluguel'] = Imovel.objects.filter(tipo_imovel='ALUGUEL')
        return context

aluguel = AluguelListView.as_view()




def imovel(request, slug):
    imovel = Imovel.objects.get(slug=slug)
    context = {
        'imovel': imovel,
    }
    return render(request, 'slide.html', context)






