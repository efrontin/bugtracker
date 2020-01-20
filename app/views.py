from django.shortcuts import render
from django.views import generic


# Create your views here.

class IndexView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['nom'] = 'Evrard'

        return result

    template_name = 'index.html'
