from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Vitima
from services import formatar_cpf

@csrf_exempt
def adicionar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            cpf = data.get('cpf')
            nome = data.get('nome')
            cep = data.get('cep')
            idade = data.get('idade')
            apelido = data.get('apelido')
            num_apelido = data.get('num_apelido')
            cidade = data.get('cidade')
            estado = data.get('estado')
            rua = data.get('rua')
            num_endereco = data.get('num_endereco')
            complemento_endereco = data.get('complemento_endereco')

            vitima = Vitima.objects.create(
                cpf_vitima= formatar_cpf(cpf),
                nome_vitima=nome,
                cep_vitima=cep,
                idade_vitima=idade,
                apelido_vitima=apelido,
                num_apelido_vitima=num_apelido,
                cidade_vitima=cidade,
                estado_vitima=estado,
                rua_vitima=rua,
                num_endereco_vitima=num_endereco,
                complemento_endereco_vitima=complemento_endereco
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Vítima cadastrada com sucesso!',
                'id': vitima.id_vitima
            }, status=201)
            
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'JSON inválido'
            }, status=400)
        
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Erro ao cadastrar: {str(e)}'
            }, status=400)
    
    return JsonResponse({
        'success': False,
        'message': 'Método não permitido'
    }, status=405)