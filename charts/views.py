from django.shortcuts import render
from users.models import Applicant
from vacancies.models import Vacancies
from django.db.models.functions import ExtractMonth
from django.db.models import Count
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'charts/index_charts.html')



#Tela para relatórios de vagas
@login_required
def charts_vacancies(request):

    #Vagas criadas no mês
    company_vacancies_by_month = Vacancies.objects.annotate(month=ExtractMonth('data_criacao')).values('month').annotate(count=Count('id'))

    x = [x[0] for x in company_vacancies_by_month.values_list('month')]
    y = [y[0] for y in company_vacancies_by_month.values_list('count')]

    context = {
        'x' : x,
        'y' : y
    }

    return render(request, 'charts/charts_vacancies.html', context)


#Tela para relatorios de candidatos
@login_required
def charts_applicants(request):

    #Candidatos recebidos por mês
    company_applicants_by_month = Applicant.objects.annotate(month=ExtractMonth('data_cadastro')).values('month').annotate(count=Count('id'))

    x = [x[0] for x in company_applicants_by_month.values_list('month')]
    y = [y[0] for y in company_applicants_by_month.values_list('count')]

    context = {
        'x' : x,
        'y' : y
    }

    return render(request, 'charts/charts_applicants.html', context)
