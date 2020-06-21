from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomePageView(TemplateView):
    # template
    template_name = 'home.html'


class AboutPageView(TemplateView):
    #template
    template_name = 'about.html'