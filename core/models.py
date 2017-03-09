# coding=utf-8

from django.db import models
from django.core.urlresolvers import reverse



class Capa(models.Model):
    image_capa = models.ImageField(upload_to='images/capa', verbose_name='Imagem da capa', null=True, blank=True)
    slogan = models.CharField('Slogan', max_length=100, blank=True) 
    slogan_de_baixo = models.CharField('Slogan_de_baixo', max_length=100, blank=True) 
    created = models.DateTimeField('Criado em', auto_now_add=True)


    class Meta:
        ordering = ['-id']

    # def __str__(self):
    #     return self.id