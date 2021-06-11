from django.urls import path
from . views import charts_vacancies, index, charts_applicants

urlpatterns = [
    path('tela-principal-relatorios', index, name="chart-index"),
    path('relatorio-vagas', charts_vacancies, name="chart-vacancies"),
    path('relatorio-candidatos', charts_applicants, name="chart-applicants"),
]