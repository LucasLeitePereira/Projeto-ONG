from django.contrib import admin
from .models import Voluntario, Estagiario

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

    @admin.display(description='Tipo')
    def tipo_voluntario(self, obj):
        if hasattr(obj, 'estagiario'):
            return 'Estagiário'
        elif hasattr(obj, 'advogado'):
            return 'Advogado'
        elif hasattr(obj, 'bacharel'):
            return 'Bacharel'
        return 'Voluntário'
    
@admin.register(Estagiario)
class EstagiarioAdmin(admin.ModelAdmin):
    list_display = [
        'id_estagiario',
        'get_nome_voluntario',
        'curso_estagiario',
        'periodo_estagiario'
    ]
    
    search_fields = ['id_voluntario__nomecompleto_voluntario', 'curso_estagiario']
    list_filter = ['curso_estagiario', 'periodo_estagiario']
    readonly_fields = ['id_estagiario']
    #inlines = [DisponibilidadeInline]
    
    @admin.display(description='Nome', ordering='id_voluntario__nomecompleto_voluntario')
    def get_nome_voluntario(self, obj):
        return obj.id_voluntario.nomecompleto_voluntario