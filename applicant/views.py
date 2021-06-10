from django.shortcuts import render
from users.models import Applicant
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from vacancies.models import Vacancies, VacanciesApplications


#View para listar todas as vagas
@method_decorator([login_required], name='dispatch')
class ListVacanciesApplicant(generic.ListView):
    model = Vacancies
    context_object_name = "vacancies"
    template_name = "applicant/list_vacancies_applicant.html"

    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)

        #checar se o candidato já completou o seu cadastro
        context['applicant_id'] = Applicant.objects.values_list('user', flat=True)

        context['applicants'] = Applicant.objects.all()

        return context



class RegisterUpdate(generic.UpdateView):
    model = Applicant
    fields = ['nome', 'faixa_salarial', 'exp', 'escolaridade']
    template_name = "applicant/register_update_applicant.html"
    success_url = reverse_lazy('applicant:list-vacancies-applicant')

    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)

        #checar se o candidato já completou o seu cadastro
        context['applicant_id'] = Applicant.objects.values_list('user', flat=True)

        return context