from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro-vitima/', views.cadastro_vitima, name='cadastro_vitima'),
    path('voluntarios/', views.voluntarios, name='voluntarios'),
    path('voluntarios/advogado/', views.voluntario_advogado, name='voluntario_advogado'),
    path('voluntarios/bacharel/', views.voluntario_bacharel, name='voluntario_bacharel'),
    path('estagio/', views.voluntario_estagiario, name='estagio'),
]