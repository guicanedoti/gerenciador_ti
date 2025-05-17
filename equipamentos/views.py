from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Departamento, Sala, Responsavel, Equipamento, Alocacao 
from django.shortcuts import render 

def home(request):
    return render(request, 'home.html')

# Departamento
class DepartamentoListView(LoginRequiredMixin, ListView):
    model = Departamento
    template_name = 'departamento/list.html'
    context_object_name = 'departamentos'

class DepartamentoCreateView(LoginRequiredMixin, CreateView):
    model = Departamento
    fields = ['nome']
    template_name = 'departamento/form.html'
    success_url = reverse_lazy('departamento_list')

class DepartamentoDetailView(LoginRequiredMixin, DetailView):
    model = Departamento
    template_name = 'departamento/detail.html'

class DepartamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Departamento
    fields = ['nome']
    template_name = 'departamento/form.html'
    success_url = reverse_lazy('departamento_list')

class DepartamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Departamento
    template_name = 'departamento/confirm_delete.html'
    success_url = reverse_lazy('departamento_list')

# Sala
class SalaListView(LoginRequiredMixin, ListView):
    model = Sala
    template_name = 'sala/list.html'
    context_object_name = 'salas'

class SalaCreateView(LoginRequiredMixin, CreateView):
    model = Sala
    fields = ['nome', 'departamento']
    template_name = 'sala/form.html'
    success_url = reverse_lazy('sala_list')

class SalaDetailView(LoginRequiredMixin, DetailView):
    model = Sala
    template_name = 'sala/detail.html'

class SalaUpdateView(LoginRequiredMixin, UpdateView):
    model = Sala
    fields = ['nome', 'departamento']
    template_name = 'sala/form.html'
    success_url = reverse_lazy('sala_list')

class SalaDeleteView(LoginRequiredMixin, DeleteView):
    model = Sala
    template_name = 'sala/confirm_delete.html'
    success_url = reverse_lazy('sala_list')

# Responsavel
class ResponsavelListView(LoginRequiredMixin, ListView):
    model = Responsavel
    template_name = 'responsavel/list.html'
    context_object_name = 'responsaveis'

class ResponsavelCreateView(LoginRequiredMixin, CreateView):
    model = Responsavel
    fields = ['nome', 'matricula']
    template_name = 'responsavel/form.html'
    success_url = reverse_lazy('responsavel_list')

class ResponsavelDetailView(LoginRequiredMixin, DetailView):
    model = Responsavel
    template_name = 'responsavel/detail.html'

class ResponsavelUpdateView(LoginRequiredMixin, UpdateView):
    model = Responsavel
    fields = ['nome', 'matricula']
    template_name = 'responsavel/form.html'
    success_url = reverse_lazy('responsavel_list')

class ResponsavelDeleteView(LoginRequiredMixin, DeleteView):
    model = Responsavel
    template_name = 'responsavel/confirm_delete.html'
    success_url = reverse_lazy('responsavel_list')

# Equipamento
class EquipamentoListView(LoginRequiredMixin, ListView):
    model = Equipamento
    template_name = 'equipamento/list.html'
    context_object_name = 'equipamentos'

class EquipamentoCreateView(LoginRequiredMixin, CreateView):
    model = Equipamento
    fields = ['tipo', 'marca', 'modelo', 'numero_patrimonio', 'status', 'descricao']
    template_name = 'equipamento/form.html'
    success_url = reverse_lazy('equipamento_list')

class EquipamentoDetailView(LoginRequiredMixin, DetailView):
    model = Equipamento
    template_name = 'equipamento/detail.html'

class EquipamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Equipamento
    fields = ['tipo', 'marca', 'modelo', 'numero_patrimonio', 'status', 'descricao']
    template_name = 'equipamento/form.html'
    success_url = reverse_lazy('equipamento_list')

class EquipamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Equipamento
    template_name = 'equipamento/confirm_delete.html'
    success_url = reverse_lazy('equipamento_list')

# Alocacao
class AlocacaoListView(LoginRequiredMixin, ListView):
    model = Alocacao
    template_name = 'alocacao/list.html'
    context_object_name = 'alocacoes'

class AlocacaoCreateView(LoginRequiredMixin, CreateView):
    model = Alocacao
    fields = ['equipamento', 'responsavel', 'sala']
    template_name = 'alocacao/form.html'
    success_url = reverse_lazy('alocacao_list')

class AlocacaoDetailView(LoginRequiredMixin, DetailView):
    model = Alocacao
    template_name = 'alocacao/detail.html'

class AlocacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Alocacao
    fields = ['equipamento', 'responsavel', 'sala']
    template_name = 'alocacao/form.html'
    success_url = reverse_lazy('alocacao_list')

class AlocacaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Alocacao
    template_name = 'alocacao/confirm_delete.html'
    success_url = reverse_lazy('alocacao_list')
