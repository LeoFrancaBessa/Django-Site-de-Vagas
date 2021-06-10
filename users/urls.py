from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . views import LoginView, Index, ApplicantRegisterView, CompanyRegisterView, ApplicantCompleteRegister, CompanyCompleteRegister, login_success

urlpatterns = [
    path('', Index, name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="users:index"), name="logout"),
    path('login-sucesso', login_success, name="login-success"),
    path('registrar-candidato/', ApplicantRegisterView.as_view(), name="register-applicant"),
    path('registrar-empresa/', CompanyRegisterView.as_view(), name="register-company"),
    path('completar-cadastro-candidato/', ApplicantCompleteRegister.as_view(), name="applicant-register-complete"),
    path('completar-cadastro-empresa/', CompanyCompleteRegister.as_view(), name="company-register-complete"),
]
