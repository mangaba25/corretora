# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Imovel

class ListarListView(generic.ListView):
    model = Imovel
    template_name = 'imovel/list.html'
    context_object_name = 'object_list'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(ListarListView, self).get_context_data(**kwargs)
        context['tres'] = Imovel.objects.all()[:3]
        return context

listar = ListarListView.as_view()

class CategoryListView(generic.ListView):
    template_name = 'ondecomer/descricao.html'
    context_object_name = 'object_list'
    paginate_by = 8

    def get_queryset(self):
        return OndeComer.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(CategoryOndeComer, slug=self.kwargs['slug'])
        context['capa'] = ImageOndecomer.objects.all()
        return context

category = CategoryListView.as_view()

def imovel(request, name):
    ondecomer = Imovel.objects.get(name=name)
    context = {
        'ondecomer': ondecomer
    }
    return render(request, 'te.html', context)






