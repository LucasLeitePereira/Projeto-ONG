from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/', views.test_message, name='test_message'),
]
