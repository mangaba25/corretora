
from django.db import models
from django.core.urlresolvers import reverse



class Imovel(models.Model):
    VENDA = 1
    ALUGUEL = 2
    BOOK_TYPES = (
        (VENDA, 'Venda'),
        (ALUGUEL, 'Aluguel'),
    )
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)
    name = models.CharField('Nome', max_length=100, blank=True) 
    description = models.TextField('Descrição-do-Imovel', blank=True)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name='Imovel'
        ordering = ['-created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('imovel:imovel', kwargs={'name': self.name})


class Image(models.Model):
    category = models.ForeignKey('imovel.Imovel', verbose_name='Categoria')
    image = models.ImageField(upload_to='cumuruxatiba/images', verbose_name='Imagem', null=True, blank=True)
    description = models.CharField('Descrição', max_length=100, blank=True)

    def __str__(self):
        return self.category

