from django.contrib import admin
from django.urls import path, include
from . views import LoginView, ListUser, Index, ApplicantRegisterView, CompanyRegisterView, ApplicantCompleteRegister, CompanyCompleteRegister

urlpatterns = [
    path('', Index, name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('register-applicant/', ApplicantRegisterView.as_view(), name="register-applicant"),
    path('register-company/', CompanyRegisterView.as_view(), name="register-company"),
    path('applicant-register-complete', ApplicantCompleteRegister.as_view(), name="applicant-register-complete"),
    path('company-register-complete', CompanyCompleteRegister.as_view(), name="company-register-complete"),
    path('list-users/', ListUser.as_view(), name="list-user"),
]
