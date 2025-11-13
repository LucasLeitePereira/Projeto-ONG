from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Voluntario, Estagiario, Advogado, Bacharel
from services import formatar_cpf

import json

@csrf_exempt
def adicionar_estagiario(request):
    if request.method == 'POST':
        try: 
            data = json.loads(request.body)
            
            email = data.get('email')
            nome = data.get('nome')
            datanasc = data.get('dataNascimento')
            sexo = data.get('sexo')
            cidade = data.get('cidade')
            estado = data.get('estado')
            endereco = data.get('endereco')
            telefone = data.get('telefone')
            instagram = data.get('instagram')
            cpf = data.get('cpf')
            rg = data.get('rg')
            cpfupload = data.get('cpfupload')
            fotoupload = data.get('fotoupload')
            termoupload = data.get('termoupload')

            voluntario = Voluntario.objects.create(
                email_voluntario=email,
                nomecompleto_voluntario=nome,
                datanasc_voluntario=datanasc,
                sexo_voluntario=sexo,
                cidade_voluntario=cidade,
                estado_voluntario=estado,
                endereco_voluntario=endereco,
                telefone_voluntario=telefone,
                instagram_voluntario=instagram,
                cpf_voluntario=formatar_cpf(cpf),
                rg_voluntario=rg,
                cpfupload_voluntario=cpfupload,
                fotoupload_voluntario=fotoupload,
                termoupload_voluntario=termoupload
            )

            estagiario = Estagiario.objects.create(
                id_voluntario=voluntario,
                curso_estagiario=data.get('curso'),
                periodo_estagiario=data.get('periodo')
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Voluntário cadastrado com sucesso!',
                'id': voluntario.id_voluntario
            }, status=201)
            
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'JSON inválido'
            }, status=400)
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Erro ao cadastrar estagiario: {str(e)}'
            }, status=400)
    else:
        return JsonResponse({
            'success': False,
            'message': 'Método não permitido'
        }, status=405)

@csrf_exempt
def adicionar_advogado(request):
    if request.method == 'POST':
        try: 
            data = json.loads(request.body)
            
            email = data.get('email')
            nome = data.get('nome')
            datanasc = data.get('dataNascimento')
            sexo = data.get('sexo')
            cidade = data.get('cidade')
            estado = data.get('estado')
            endereco = data.get('endereco')
            telefone = data.get('telefone')
            instagram = data.get('instagram')
            cpf = data.get('cpf')
            rg = data.get('rg')
            cpfupload = data.get('cpfupload')
            fotoupload = data.get('fotoupload')
            termoupload = data.get('termoupload')

            voluntario = Voluntario.objects.create(
                email_voluntario=email,
                nomecompleto_voluntario=nome,
                datanasc_voluntario=datanasc,
                sexo_voluntario=sexo,
                cidade_voluntario=cidade,
                estado_voluntario=estado,
                endereco_voluntario=endereco,
                telefone_voluntario=telefone,
                instagram_voluntario=instagram,
                cpf_voluntario=formatar_cpf(cpf),
                rg_voluntario=rg,
                cpfupload_voluntario=cpfupload,
                fotoupload_voluntario=fotoupload,
                termoupload_voluntario=termoupload
            )

            advogado = Advogado.objects.create(
                id_voluntario=voluntario,
                oab_advogado=data.get('oab')
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Voluntário cadastrado com sucesso!',
                'id': voluntario.id_voluntario
            }, status=201)
            
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'JSON inválido'
            }, status=400)
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Erro ao cadastrar adogado: {str(e)}'
            }, status=400)
    else:
        return JsonResponse({
            'success': False,
            'message': 'Método não permitido'
        }, status=405)
    
@csrf_exempt
def adicionar_bacharel(request):
    if request.method == 'POST':
        try: 
            data = json.loads(request.body)
            
            email = data.get('email')
            nome = data.get('nome')
            datanasc = data.get('dataNascimento')
            sexo = data.get('sexo')
            cidade = data.get('cidade')
            estado = data.get('estado')
            endereco = data.get('endereco')
            telefone = data.get('telefone')
            instagram = data.get('instagram')
            cpf = data.get('cpf')
            rg = data.get('rg')
            cpfupload = data.get('cpfupload')
            fotoupload = data.get('fotoupload')
            termoupload = data.get('termoupload')
            cursoformacao = data.get('cursoBacharel')

            voluntario = Voluntario.objects.create(
                email_voluntario=email,
                nomecompleto_voluntario=nome,
                datanasc_voluntario=datanasc,
                sexo_voluntario=sexo,
                cidade_voluntario=cidade,
                estado_voluntario=estado,
                endereco_voluntario=endereco,
                telefone_voluntario=telefone,
                instagram_voluntario=instagram,
                cpf_voluntario=formatar_cpf(cpf),
                rg_voluntario=rg,
                cpfupload_voluntario=cpfupload,
                fotoupload_voluntario=fotoupload,
                termoupload_voluntario=termoupload
            )

            bacharel = Bacharel.objects.create(
                id_voluntario=voluntario,
                cursoformacao_bacharel=cursoformacao
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Voluntário cadastrado com sucesso!',
                'id': voluntario.id_voluntario
            }, status=201)
            
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'JSON inválido'
            }, status=400)
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Erro ao cadastrar adogado: {str(e)}'
            }, status=400)
    else:
        return JsonResponse({
            'success': False,
            'message': 'Método não permitido'
        }, status=405)