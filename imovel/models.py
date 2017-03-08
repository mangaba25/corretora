# coding=utf-8

from django.db import models
from django.core.urlresolvers import reverse



class Imovel(models.Model):
    VENDA = 'VENDA'
    ALUGUEL = 'ALUGUEL'
    TIPO_IMOVEL = (
        (VENDA, 'Venda'),
        (ALUGUEL, 'Aluguel'),
    )

    tipo_imovel = models.CharField(max_length= 10,choices=TIPO_IMOVEL, default=VENDA)
    slug = models.SlugField('Identificador', max_length=100, blank=True)
    lugar = models.CharField('Lugar', max_length=100, blank=True) 
    preco =  models.DecimalField('Preço', decimal_places=2, max_digits=8, blank=True, null=True)
    dormitorio = models.PositiveIntegerField('Quant. Dormitórios', blank=True, null=True)

    description = models.TextField('Descrição-do-Imovel', blank=True)
    image_1 = models.ImageField(upload_to='cumuruxatiba/images', verbose_name='Imagem', null=True, blank=True)
    description_1 = models.CharField('Descrição', max_length=100, blank=True)
    
    image_2 = models.ImageField(upload_to='cumuruxatiba/images', verbose_name='Imagem', null=True, blank=True)
    description_2 = models.CharField('Descrição', max_length=100, blank=True)
    
    image_3 = models.ImageField(upload_to='cumuruxatiba/images', verbose_name='Imagem', null=True, blank=True)
    description_3 = models.CharField('Descrição', max_length=100, blank=True)
    
    image_4 = models.ImageField(upload_to='cumuruxatiba/images', verbose_name='Imagem', null=True, blank=True)
    description_4 = models.CharField('Descrição', max_length=100, blank=True)
    
    image_5 = models.ImageField(upload_to='cumuruxatiba/images', verbose_name='Imagem', null=True, blank=True)
    description_5 = models.CharField('Descrição', max_length=100, blank=True)
    
    image_6 = models.ImageField(upload_to='cumuruxatiba/images', verbose_name='Imagem', null=True, blank=True)
    description_6 = models.CharField('Descrição', max_length=100, blank=True)
    
    image_7 = models.ImageField(upload_to='cumuruxatiba/images', verbose_name='Imagem', null=True, blank=True)
    description_7 = models.CharField('Descrição', max_length=100, blank=True)
    
    image_8 = models.ImageField(upload_to='cumuruxatiba/images', verbose_name='Imagem', null=True, blank=True)
    description_8 = models.CharField('Descrição', max_length=100, blank=True)
    
    image_9 = models.ImageField(upload_to='cumuruxatiba/images', verbose_name='Imagem', null=True, blank=True)
    description_9 = models.CharField('Descrição', max_length=100, blank=True)
    
    image_10 = models.ImageField(upload_to='cumuruxatiba/images', verbose_name='Imagem', null=True, blank=True)
    description_10 = models.CharField('Descrição', max_length=100, blank=True)
    
    

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name='Imovel'
        ordering = ['-created']

    def __str__(self):
        return self.lugar

    def get_absolute_url(self):
        return reverse('imovel:imovel', kwargs={'slug': self.slug})
