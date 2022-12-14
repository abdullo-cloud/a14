from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import *




class Home(ListView):
    paginate_by = 3
    model = Post
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"
class Contact(CreateView):
    model = Contact
    template_name = "contact.html"
    fields = "__all__"
class Myteam(TemplateView):
    template_name = "myteam.html"
class Reklama(TemplateView):
    template_name = "reklama.html"
class Registration(CreateView):
    model = Registration
    template_name = "registration.html"
    fields = "__all__"
class Succes(TemplateView):
    template_name = "succes.html"

# Create your views here.


