from django.contrib import admin
from .models import Sintoma, Medicamento, Indicacao

class SintomaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 15

admin.site.register(Sintoma, SintomaAdmin)

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'dose', 'posologia')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 15

admin.site.register(Medicamento, MedicamentoAdmin)

class IndicacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'medicamento', 'sintoma')
    list_display_links = ('id', 'medicamento', 'sintoma')
    list_per_page = 15

admin.site.register(Indicacao, IndicacaoAdmin)