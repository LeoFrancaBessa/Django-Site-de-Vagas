from typing import Generic
from django.shortcuts import render
from . models import Vacancies, VacanciesApplications
from users.models import Applicant, Company
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



#Listar vagas
@method_decorator([login_required], name='dispatch')
class ListVacancies(generic.ListView):

    model = Vacancies
    context_object_name = "vacancies"
    template_name = "vacancies/list_vacancies.html"

    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)

        #Listar só as vagas da empresa
        current_company = Company.objects.filter(user = self.request.user)
        context['vacancies'] = context['vacancies'].filter(company = current_company[0])

        #checar se a empresa já completou o seu cadastro
        context['company_id'] = Company.objects.values_list('user', flat=True)

        return context



#Criar vagas
@method_decorator([login_required], name='dispatch')
class CreateVacancie(generic.CreateView):

    model = Vacancies
    template_name = "vacancies/create_vacancies.html"
    fields = ['nome', 'faixa_salarial', 'req', 'escolaridade']
    success_url = reverse_lazy('vacancies:list-vacancies')

    #colocar o nome da empresa como padrão
    def  form_valid(self, form):

        current_company = Company.objects.filter(user = self.request.user)
        form.instance.company = current_company[0]
        return super(CreateVacancie, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)

        #checar se a empresa já completou o seu cadastro
        context['company_id'] = Company.objects.values_list('user', flat=True)

        return context



#Editar vagas
@method_decorator([login_required], name='dispatch')
class UpdateVacancie(generic.UpdateView):

    model = Vacancies
    fields = ['nome', 'faixa_salarial', 'req', 'escolaridade']
    template_name = "vacancies/update_vacancie.html"
    success_url = reverse_lazy('vacancies:list-vacancies')


    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)

        #checar se a empresa já completou o seu cadastro
        context['company_id'] = Company.objects.values_list('user', flat=True)

        return context



#Deletar vagas
class DeleteVacancie(generic.DeleteView):
    model = Vacancies
    context_object_name = "vacancie"
    template_name = "vacancies/delete_vacancie.html"
    success_url = reverse_lazy('vacancies:list-vacancies')

    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)

        #checar se a empresa já completou o seu cadastro
        context['company_id'] = Company.objects.values_list('user', flat=True)

        return context