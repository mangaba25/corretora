

from django.contrib import admin

from .models import Capa

class CapaAdmin(admin.ModelAdmin):
    list_display = ['created']


admin.site.register(Capa, CapaAdmin)


