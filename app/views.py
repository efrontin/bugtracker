from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

# Create your views here.
from app.forms.authForm import ConnectionForm
from app.models import Project, Ticket, Employee, Company


class IndexView(generic.TemplateView):
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


class TicketDetailView(generic.DetailView):
    model = Ticket
    template_name = 'ticket_detail.html'


class UserListView(generic.ListView):
    model = Employee
    template_name = 'user_list.html'


class UserDetailView(generic.DetailView):
    model = Employee
    template_name = 'user_detail.html'


class CompanyListView(generic.ListView):
    model = Company
    template_name = 'company_list.html'


class CompanyDetailView(generic.DetailView):
    model = Company
    template_name = 'company_detail.html'


class ProjectListView(generic.ListView):
    model = Project

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['projects'] = Project.objects.all().order_by('name')

        return result

    template_name = 'project_list.html'


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'project_detail.html'


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
        if user.employee is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, "Utilisateur ou mot de passe incorrect")
            return super().form_invalid(form)
