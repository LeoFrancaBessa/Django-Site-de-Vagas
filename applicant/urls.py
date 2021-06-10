from django.contrib import admin
from django.urls import path
from . views import ListVacanciesApplicant, RegisterUpdate

urlpatterns = [
    path('vagas-disponiveis', ListVacanciesApplicant.as_view(), name="list-vacancies-applicant"),
    path('editar-cadastro/<int:pk>/', RegisterUpdate.as_view(), name="update-register"),
]