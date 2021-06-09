from django.contrib import admin
from django.urls import path, include
from . views import LoginView, ListUser, Index, ApplicantRegisterView, CompanyRegisterView, ApplicantCompleteRegister, CompanyCompleteRegister

urlpatterns = [
    path('', Index, name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('registrar-candidato/', ApplicantRegisterView.as_view(), name="register-applicant"),
    path('registrar-empresa/', CompanyRegisterView.as_view(), name="register-company"),
    path('completar-cadastro-candidato/', ApplicantCompleteRegister.as_view(), name="applicant-register-complete"),
    path('completar-cadastro-empresa/', CompanyCompleteRegister.as_view(), name="company-register-complete"),
    path('listar-usuarios/', ListUser.as_view(), name="list-user"),
]
