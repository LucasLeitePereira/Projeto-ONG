from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/estagiario/', views.adicionar_estagiario, name='adicionar_estagiario'),
    path('adicionar/advogado/', views.adicionar_advogado, name='adicionar_advogado'),
    path('adicionar/bacharel/', views.adicionar_bacharel, name='adicionar_bacharel'),
]
