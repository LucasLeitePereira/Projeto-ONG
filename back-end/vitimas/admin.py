from django.contrib import admin
from .models import Vitima

@admin.register(Vitima)
class VitimaAdmin(admin.ModelAdmin):
    list_display = [
        'id_vitima',
        'nome_vitima',
        'cpf_vitima',
        'idade_vitima',
        'cidade_vitima',
        'estado_vitima'
    ]
    
    list_filter = ['estado_vitima', 'cidade_vitima']
    
    search_fields = [
        'nome_vitima',
        'cpf_vitima',
        'apelido_vitima'
    ]
    
    readonly_fields = ['id_vitima']
    
    list_per_page = 25
    
    fieldsets = (
        ('Informações Pessoais', {
            'fields': (
                'id_vitima',
                'nome_vitima',
                'cpf_vitima',
                'idade_vitima',
                'apelido_vitima',
                'num_apelido_vitima'
            )
        }),
        ('Endereço', {
            'fields': (
                'cep_vitima',
                'rua_vitima',
                'num_endereco_vitima',
                'complemento_endereco_vitima',
                'cidade_vitima',
                'estado_vitima'
            )
        }),
    )