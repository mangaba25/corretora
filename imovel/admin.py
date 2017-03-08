# coding=utf-8

from django.contrib import admin

from .models import Imovel

class ImovelAdmin(admin.ModelAdmin):
    list_display = ['lugar', 'tipo_imovel', 'created','modified']
    search_fields = ['lugar','tipo_imovel']
    list_filter = ['created', 'modified']


admin.site.register(Imovel, ImovelAdmin)



