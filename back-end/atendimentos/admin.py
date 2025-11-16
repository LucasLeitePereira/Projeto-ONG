from django.contrib import admin
from .models import Atendimento


@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = (
        'id_atendimento',
        'get_nome_vitima',
        'get_nome_estagiario',
        'data_atendimento',
        'hora_atendimento'
    )
    
    list_filter = (
        'data_atendimento',
        'id_estagiario'
    )
    
    search_fields = (
        'id_vitima__nome_vitima',
        'id_vitima__cpf_vitima',
        'id_estagiario__id_voluntario__nomecompleto_voluntario'
    )
    
    date_hierarchy = 'data_atendimento'
    
    fieldsets = (
        ('Informações da Vítima', {
            'fields': ('id_vitima',)
        }),
        ('Estagiário Responsável', {
            'fields': ('id_estagiario',)
        }),
        ('Data e Hora', {
            'fields': ('data_atendimento', 'hora_atendimento')
        }),
    )
    
    # Métodos personalizados para exibição
    def get_nome_vitima(self, obj):
        return obj.id_vitima.nome_vitima
    get_nome_vitima.short_description = 'Vítima'
    get_nome_vitima.admin_order_field = 'id_vitima__nome_vitima'
    
    def get_nome_estagiario(self, obj):
        return obj.id_estagiario.id_voluntario.nomecompleto_voluntario
    get_nome_estagiario.short_description = 'Estagiário'
    get_nome_estagiario.admin_order_field = 'id_estagiario__id_voluntario__nomecompleto_voluntario'
    
    # Configurações adicionais
    save_on_top = True
    list_per_page = 25