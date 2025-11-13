from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/', views.adicionar, name='adicionar'),
]
