from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from .forms import LoginForm, ApplicantRegisterForm, CompanyRegisterForm
from . models import User, Applicant, Company



#View para gerar a página inicial
def Index(request):
    return render(request, 'users/index.html')



#View para a tela de login
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True



#Redireciona o usuário baseado em seu tipo
def login_success(request):

    if request.user.is_applicant:
        return redirect('applicant:list-vacancies-applicant')
    
    else:
        return redirect('vacancies:list-vacancies')



#View que realizará o cadastro dos participantes
class ApplicantRegisterView(generic.CreateView):

    model = User
    form_class = ApplicantRegisterForm
    template_name = 'users/applicant_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'applicant'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('users:applicant-register-complete')



#View que realizará o cadastro das empresas
class CompanyRegisterView(generic.CreateView):

    model = User
    form_class = CompanyRegisterForm
    template_name = 'users/company_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('users:company-register-complete')






#View para completar o cadastro dos candidatos
#Só pode ser acessada se o usuário estiver logado e for candidato
@method_decorator([login_required], name='dispatch')
class ApplicantCompleteRegister(generic.CreateView):
    model = Applicant
    template_name = "users/applicant_complete_register.html"
    fields = ['nome', 'faixa_salarial', 'exp', 'escolaridade']
    success_url = reverse_lazy('users:list-user')


    def  form_valid(self, form):
       form.instance.user = self.request.user
       return super(ApplicantCompleteRegister, self).form_valid(form)

    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)
    
        #checar se o usuário já realizou o seu cadastro
        context['applicants_id'] = Applicant.objects.values_list('user', flat=True)

        return context





#View para completar o cadastro das empresas
#Só pode ser acessada se o usuário estiver logado e for uma empresa
@method_decorator([login_required], name='dispatch')
class CompanyCompleteRegister(generic.CreateView):
    model = Company
    template_name = "users/company_complete_register.html"
    fields = ['nome']
    success_url = reverse_lazy('vacancies:list-vacancies')

    def  form_valid(self, form):
       form.instance.user = self.request.user
       return super(CompanyCompleteRegister, self).form_valid(form)


    def get_context_data(self, **kwargs):
    
        context = super().get_context_data(**kwargs)

        #checar se o usuário já realizou o seu cadastro
        context['companies_id'] = Company.objects.values_list('user', flat=True)

        return context
        


