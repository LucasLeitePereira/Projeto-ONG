from django.db import models

class Vitima(models.Model):
    id_vitima = models.AutoField(primary_key=True)
    cpf_vitima = models.CharField(max_length=14, unique=True)
    nome_vitima = models.CharField(max_length=150)
    cep_vitima = models.CharField(max_length=8)
    idade_vitima = models.IntegerField()
    apelido_vitima = models.CharField(max_length=30, blank=True, null=True)
    cidade_vitima = models.CharField(max_length=30)
    estado_vitima = models.CharField(max_length=2)
    rua_vitima = models.CharField(max_length=50)
    num_endereco_vitima = models.IntegerField()
    complemento_endereco_vitima = models.CharField(max_length=120, blank=True, null=True)
    
    class Meta:
        db_table = 'Vitimas'
        verbose_name = 'Vítima'
        verbose_name_plural = 'Vítimas'
    
    def __str__(self):
        return self.nome_vitima