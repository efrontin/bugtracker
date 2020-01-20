from django.shortcuts import render
from django.views import generic


# Create your views here.
from app.models import Project


class IndexView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['nom'] = 'Evrard'
        result['projects'] = Project.objects.all().order_by('name')

        return result

    template_name = 'index.html'
