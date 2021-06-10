from django.contrib import admin
from django.urls import path
from . views import ListVacanciesApplicant, RegisterUpdate, DetailVacanciesApplicant, confirm_vacancie_application


urlpatterns = [
    path('vagas-disponiveis', ListVacanciesApplicant.as_view(), name="list-vacancies-applicant"),
    path('editar-cadastro/<int:pk>/', RegisterUpdate.as_view(), name="update-register"),
    path('detalhes-vaga/<int:pk>/', DetailVacanciesApplicant.as_view(), name="detail-vacancie-applicant"),
    path('confirmar-registro-vaga', confirm_vacancie_application, name="confirm-application"),
]