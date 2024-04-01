import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)

from applications.entrada.models import Entry
from .models import Home
from .forms import SuscribirseForm


class HomePageView(TemplateView):
    template_name = "home/index.html"

    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Cargamos home
        context["home"] = Home.objects.latest('created')
        # Contexto para la portada
        context["portada"] = Entry.objects.entrada_en_portada()
        #Contexto para los articulos en home
        context["entradas_home"] = Entry.objects.entradas_en_home()
        #Contexto para las entradas recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()
        #Enviamos formulario de suscripción
        context["form"] = SuscribirseForm
        return context
    

class SuscriberCreateView(CreateView):
    form_class = SuscribirseForm
    success_url = "."
