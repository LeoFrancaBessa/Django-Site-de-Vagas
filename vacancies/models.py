from django.db import models
from users.models import Company, Applicant



#Classe para a vaga
class Vacancies(models.Model):

    def __str__(self):
        return self.nome

    company = models.ForeignKey(Company, verbose_name="Empresa", on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, verbose_name="Título")

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


    req = models.TextField(verbose_name="Requisitos")


    escolaridade = models.CharField(max_length=20, choices=escol, verbose_name="Escolaridade Mínima")



#Classe para registrar as aplicações de vagas dos candidatos
class VacanciesApplications(models.Model):
    
    vaga = models.ForeignKey(Vacancies, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    data = models.DateTimeField(verbose_name="Data do Registro", auto_now=True)
    pontos = models.PositiveIntegerField(verbose_name="Pontos do Candidato")