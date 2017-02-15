from django.contrib import admin

from .models import Imovel, Image

class ImovelAdmin(admin.ModelAdmin):
    list_display = ['name', 'book_type', 'created','modified']
    search_fields = ['name','book_type']
    list_filter = ['created', 'modified']

class ImageAdmin(admin.ModelAdmin):
	list_display = ['category']

admin.site.register(Imovel, ImovelAdmin)
admin.site.register(Image, ImageAdmin)



