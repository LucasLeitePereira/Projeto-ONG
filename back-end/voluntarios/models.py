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

class Estagiario(models.Model):
    PERIODOS = [
        ('1', '1º Período'),
        ('2', '2º Período'),
        ('3', '3º Período'),
        ('4', '4º Período'),
        ('5', '5º Período'),
        ('6', '6º Período'),
        ('7', '7º Período'),
        ('8', '8º Período'),
        ('9', '9º Período'),
        ('10', '10º Período'),
    ]
    
    id_estagiario = models.AutoField(primary_key=True)
    
    id_voluntario = models.OneToOneField(
        Voluntario,
        on_delete=models.CASCADE,
        db_column='id_voluntario',
        related_name='estagiario'
    )
    
    curso_estagiario = models.CharField(max_length=20)
    periodo_estagiario = models.CharField(max_length=2, choices=PERIODOS)
    
    class Meta:
        db_table = 'Estagiarios'
        verbose_name = 'Estagiário'
        verbose_name_plural = 'Estagiários'
    
    def __str__(self):
        return f"{self.id_voluntario.nomecompleto_voluntario} - Estagiário"