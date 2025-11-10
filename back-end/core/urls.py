from django.urls import path
from . import views

urlpatterns = [
    path('teste/', views.test_message, name='test_message'),
]
