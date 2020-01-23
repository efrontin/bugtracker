from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

# Create your views here.
from app.forms.authForm import ConnectionForm
from app.forms.myAccount import MyAccount
from app.forms.projectForm import ProjectForm
from app.models import Project, Ticket, Employee, Company, CompanyProject


class IndexView(LoginRequiredMixin, generic.TemplateView):
    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['projects'] = Project.objects.all().order_by('name')
        result['tickets'] = Ticket.objects.all()

        return result

    template_name = 'index.html'


class TicketListView(LoginRequiredMixin, generic.ListView):
    model = Ticket

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['tickets'] = Ticket.objects.all()

        return result

    template_name = 'ticket_list.html'


class TicketDetailView(LoginRequiredMixin, generic.DetailView):
    model = Ticket
    template_name = 'ticket_detail.html'


class UserListView(LoginRequiredMixin, generic.ListView):
    model = Employee
    template_name = 'user_list.html'


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = Employee
    template_name = 'user_detail.html'


class CompanyListView(LoginRequiredMixin, generic.ListView):
    model = Company
    template_name = 'company_list.html'


class CompanyDetailView(LoginRequiredMixin, generic.DetailView):
    model = Company
    template_name = 'company_detail.html'


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['projects'] = Project.objects.all().order_by('name')

        return result

    template_name = 'project_list.html'


class ProjectCreateView(generic.FormView):
    form_class = ProjectForm
    template_name = 'project_form.html'

    def get_success_url(self):
        return reverse('index')

    def get_initial(self):
        user = self.request.user
        initial = super().get_initial()
        initial.update({
            'companies_choices': [
                (v.pk, str(v))
                for v in Company.objects.exclude(
                    employees__in=[user.employee.pk])]
        })
        return initial

    def form_valid(self, form):
        name = form.cleaned_data['name']
        company_str = form.cleaned_data['company']
        is_client = self.request.POST.get('is_client') is not None

        project = Project()
        project.save()
        company = Company.objects.get(name=company_str.name)
        CompanyProject.objects.create(
            project=project,
            company=company,
            is_client=is_client
        )
        CompanyProject.objects.create(
            project=project,
            company=self.request.user.employee.company,
            is_client=not is_client
        )
        project.name = name
        project.save()

        return super().form_valid(form)


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    template_name = 'project_detail.html'


def logout_user(request):
    logout(request)
    return redirect('login')


class Login(generic.FormView):
    template_name = 'login.html'
    form_class = ConnectionForm

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, "Utilisateur ou mot de passe incorrect")
            return super().form_invalid(form)


class TicketSearchByProjectListView(LoginRequiredMixin, generic.ListView):
    model = Ticket
    template_name = 'ticket_list.html'

    def get_queryset(self):
        return Ticket.objects.filter(project_id=self.kwargs['pk'])


class MyAccountView(generic.FormView):
    template_name = 'my_account.html'
    form_class = MyAccount

    def get_success_url(self):
        return reverse('my_account')

    def get_initial(self):
        user = self.request.user

        try:
            company = Company.objects.get(employees__user__in=[user.pk])
        except Company.DoesNotExist:
            company = None

        initial = super().get_initial()
        initial.update({
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'companies': company
        })
        return initial

    def form_valid(self, form):
        user = self.request.user
        user.username = form.cleaned_data['username']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.employee.company = form.cleaned_data['companies']
        user.save()
        user.employee.save()
        messages.success(self.request, "Mise a jour effectué")
        return super().form_valid(form)

        # if user.employee is not None:
        #     login(self.request, user)
        #     return super().form_valid(form)
        # else:
        #     messages.error(self.request, "Utilisateur ou mot de passe incorrect")
        #     return super().form_invalid(form)
