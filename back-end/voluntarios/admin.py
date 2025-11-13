from django.contrib import admin
from .models import Voluntario

@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    list_display = [
        'id_voluntario', 
        'nomecompleto_voluntario', 
        'email_voluntario', 
        'telefone_voluntario',
        'cpf_voluntario',
        'cidade_voluntario'
    ]
    
    list_filter = ['sexo_voluntario', 'estado_voluntario', 'cidade_voluntario']
    
    search_fields = [
        'nomecompleto_voluntario', 
        'email_voluntario', 
        'cpf_voluntario',
        'telefone_voluntario'
    ]
    
    list_per_page = 25
    
    fieldsets = (
        ('Informações Pessoais', {
            'fields': (
                'nomecompleto_voluntario',
                'email_voluntario',
                'datanasc_voluntario',
                'sexo_voluntario'
            )
        }),
        ('Documentos', {
            'fields': ('cpf_voluntario', 'rg_voluntario')
        }),
        ('Localização', {
            'fields': ('endereco_voluntario', 'cidade_voluntario', 'estado_voluntario')
        }),
        ('Contato', {
            'fields': ('telefone_voluntario', 'instagram_voluntario')
        }),
        ('Uploads', {
            'fields': ('cpfupload_voluntario', 'fotoupload_voluntario', 'termoupload_voluntario')
        }),
    )