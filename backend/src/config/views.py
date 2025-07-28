"""
A view module directly attached to the basic top-level root

"""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'
    
