from django.db import models
from django.contrib.auth.models import AbstractUser



#Classe princial dos usuários
class User(AbstractUser):
    
    email = models.EmailField(unique=True, verbose_name="E-mail")
    is_company = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)

    def __str__(self):
        return self.email


#Classe para os candidatos
class Applicant(models.Model):

    def __str__(self):
        return str(self.user)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nome = models.CharField(max_length=200, verbose_name="Nome")
    
    sal = (("1000", "Até R$ 1000"), 
                    ("1000 - 2000", "De R$ 1000 a R$ 2000"),
                    ("2000 - 3000", "De R$ 2000 a R$ 3000"),
                    ("3000", "Acima de R$ 3000"))

    
    escol = (("fundamental", "Ensino fundamental"), 
                    ("medio", "Ensino médio"),
                    ("tecnologo", "Tecnólogo"),
                    ("superior", "Ensino Superior"),
                    ("pos", "Pós / MBA / Mestrado"),
                    ("doutorado", "Doutorado"))
    
    faixa_salarial = models.CharField(max_length=20, choices=sal, default="1000", verbose_name="Faixa Salarial")

    exp = models.TextField(verbose_name="Experiência")

    escolaridade = models.CharField(max_length=20, choices=escol, verbose_name="Última Escolaridade")



#Classe para as empresas
class Company(models.Model):

    def __str__(self):
        return self.nome

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(verbose_name="Nome", max_length=200)