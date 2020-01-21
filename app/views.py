from django.shortcuts import render
from django.views import generic

# Create your views here.
from app.models import Project, Ticket, User, Company


class IndexView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['projects'] = Project.objects.all().order_by('name')
        result['tickets'] = Ticket.objects.all()

        return result

    template_name = 'index.html'


class TicketListView(generic.ListView):
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
    model = User
    template_name = 'user_list.html'


class UserDetailView(generic.DetailView):
    model = User
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


class TicketSearchByProjectListView(generic.ListView):
    template_name = 'ticket_list.html'

    def get_queryset(self, queryset=None):
        return Ticket.objects.get(pk=self.kwargs['pk'])

