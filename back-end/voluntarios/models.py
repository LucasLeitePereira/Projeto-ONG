from django.db import models

class Voluntario(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    
    id_voluntario = models.AutoField(primary_key=True)
    email_voluntario = models.EmailField(max_length=100)
    nomecompleto_voluntario = models.CharField(max_length=150)
    datanasc_voluntario = models.DateField()
    sexo_voluntario = models.CharField(max_length=1, choices=SEXO_CHOICES)
    cidade_voluntario = models.CharField(max_length=30)
    estado_voluntario = models.CharField(max_length=2)
    endereco_voluntario = models.CharField(max_length=50)
    telefone_voluntario = models.CharField(max_length=9)
    instagram_voluntario = models.CharField(max_length=30)  
    cpf_voluntario = models.CharField(max_length=14, unique=True)  
    rg_voluntario = models.CharField(max_length=9)
    cpfupload_voluntario = models.BooleanField()  
    fotoupload_voluntario = models.BooleanField()  
    termoupload_voluntario = models.BooleanField()  
    
    class Meta:
        db_table = 'Voluntarios'
    
    def __str__(self):
        return self.nomecompleto_voluntario