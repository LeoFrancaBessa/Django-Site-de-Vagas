from django.contrib import admin
from django.urls import path
from . views import ListVacancies, CreateVacancie, UpdateVacancie, DeleteVacancie, DetailVacancie

urlpatterns = [
    path('listar-vagas/', ListVacancies.as_view(), name="list-vacancies"),
    path('criar-vaga/', CreateVacancie.as_view(), name="create-vacancie"),
    path('editar-vaga/<int:pk>/', UpdateVacancie.as_view(), name="update-vacancie"),
    path('deletar-vaga/<int:pk>/', DeleteVacancie.as_view(), name="delete-vacancie"),
    path('detalhes-vaga/<int:pk>/', DetailVacancie.as_view(), name="detail-vacancie"),
]
