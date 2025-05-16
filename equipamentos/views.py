from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Equipamento

class EquipamentoListView(LoginRequiredMixin, ListView): 
    model = Equipamento
    template_name = 'equipamentos/lista_equipamentos.html'
    context_object_name = 'equipamentos'

class EquipamentoCreateView(LoginRequiredMixin, CreateView): 
    model = Equipamento
    fields = '__all__'
    template_name = 'equipamentos/equipamento_form.html'
    success_url = reverse_lazy('equipamentos:lista')

class EquipamentoDetailView(LoginRequiredMixin, DetailView):
    model = Equipamento
    template_name = 'equipamentos/equipamento_detalhe.html' 

class EquipamentoUpdateView(LoginRequiredMixin, UpdateView): 
    model = Equipamento
    fields = '__all__'
    template_name = 'equipamentos/equipamento_form.html'
    success_url = reverse_lazy('equipamentos;lista') 