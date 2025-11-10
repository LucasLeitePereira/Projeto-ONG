from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def test_message(request):
    if request.method == 'GET':
        return JsonResponse(
            {
                "status": 200,
                "rota": "grutas",
                "metodo": "GET",
            }
        )
    elif request.method == 'POST':
        data = json.loads(request.body)
        mensagem = data.get('mensagem', 'Nenhuma mensagem enviada')
            
        return JsonResponse({
            "sucesso": 200,
            "rota": "grutas",
            "metodo": "POST",
            "mensagem_recebida": mensagem
        })