from django.shortcuts import render

def index(request):
    return render(request, 'front/index.html')

def cadastro_vitima(request):
    return render(request, 'front/cadastro-vitima.html')

def voluntarios(request):
    return render(request, 'front/voluntarios.html')

def voluntario_advogado(request):
    return render(request, 'front/voluntario-advogado.html')

def voluntario_bacharel(request):
    return render(request, 'front/voluntario-bacharel.html')

def voluntario_estagiario(request):
    return render(request, 'front/voluntario-estagiario.html')