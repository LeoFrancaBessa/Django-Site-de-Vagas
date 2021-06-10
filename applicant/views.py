from django.shortcuts import redirect, render
from users.models import Applicant
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from vacancies.models import Vacancies, VacanciesApplications
from users.models import Applicant
from django.core import serializers
from django.contrib import messages



#View para listar todas as vagas
@method_decorator([login_required], name='dispatch')
class ListVacanciesApplicant(generic.ListView):
    model = Vacancies
    context_object_name = "vacancies"
    template_name = "applicant/list_vacancies_applicant.html"

    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)

        #Função de pesquisar vagas
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['vacancies'] = context['vacancies'].filter(
                nome__icontains=search_input)

        
        #Serve para manter o texto no campo de pesquisa
        context['search_input'] = search_input

        #checar se o candidato já completou o seu cadastro
        context['applicant_id'] = Applicant.objects.values_list('user', flat=True)

        #Será usado como link pro cadastro
        context['applicants'] = Applicant.objects.all()

        return context



@method_decorator([login_required], name='dispatch')
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



@method_decorator([login_required], name='dispatch')
class DetailVacanciesApplicant(generic.DetailView):
    model = Vacancies
    context_object_name = "vacancie"
    template_name = "applicant/detail_vacancies_applicants.html"


    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)

        #checar se o candidato já completou o seu cadastro
        context['applicant_id'] = Applicant.objects.values_list('user', flat=True)


        #Aloca o id da vaga na sessão, para a função do candidato se cadastrar na devida vaga
        self.request.session['vacancie_id'] = context['vacancie'].id

        return context



#View para registrar o candidato a vaga
@login_required
def confirm_vacancie_application(request):

    #reunido informações
    vacancie = Vacancies.objects.get(pk=request.session.get('vacancie_id'))
    applicant = Applicant.objects.get(user=request.user)


    #Restrição para impedir que o mesmo candidato se increva na mesma vaga várias vezes
    if (VacanciesApplications.objects.filter(vaga = vacancie).exists() and VacanciesApplications.objects.filter(candidato = applicant).exists()):
        messages.info(request, 'Você já realizou sua candidatura nesta vaga!')
        return redirect('applicant:list-vacancies-applicant')


    #Salvando
    vacan_appli = VacanciesApplications(vaga=vacancie, candidato=applicant)
    vacan_appli.save()

    messages.info(request, 'Candidatura realizada com sucesso!')
    return redirect('applicant:list-vacancies-applicant')