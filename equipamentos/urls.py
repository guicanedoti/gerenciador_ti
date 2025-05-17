from django.urls import path
from .views import (
    DepartamentoListView, DepartamentoCreateView, DepartamentoDetailView, DepartamentoUpdateView, DepartamentoDeleteView,
    SalaListView, SalaCreateView, SalaDetailView, SalaUpdateView, SalaDeleteView,
    ResponsavelListView, ResponsavelCreateView, ResponsavelDetailView, ResponsavelUpdateView, ResponsavelDeleteView,
    EquipamentoListView, EquipamentoCreateView, EquipamentoDetailView, EquipamentoUpdateView, EquipamentoDeleteView,
    AlocacaoListView, AlocacaoCreateView, AlocacaoDetailView, AlocacaoUpdateView, AlocacaoDeleteView,
)

app_name = 'equipamentos'

urlpatterns = [
    # Departamento
    path('departamentos/', DepartamentoListView.as_view(), name='departamento_list'),
    path('departamentos/novo/', DepartamentoCreateView.as_view(), name='departamento_create'),
    path('departamentos/<int:pk>/', DepartamentoDetailView.as_view(), name='departamento_detail'),
    path('departamentos/<int:pk>/editar/', DepartamentoUpdateView.as_view(), name='departamento_update'),
    path('departamentos/<int:pk>/excluir/', DepartamentoDeleteView.as_view(), name='departamento_delete'),

    # Sala
    path('salas/', SalaListView.as_view(), name='sala_list'),
    path('salas/novo/', SalaCreateView.as_view(), name='sala_create'),
    path('salas/<int:pk>/', SalaDetailView.as_view(), name='sala_detail'),
    path('salas/<int:pk>/editar/', SalaUpdateView.as_view(), name='sala_update'),
    path('salas/<int:pk>/excluir/', SalaDeleteView.as_view(), name='sala_delete'),

    # Responsavel
    path('responsaveis/', ResponsavelListView.as_view(), name='responsavel_list'),
    path('responsaveis/novo/', ResponsavelCreateView.as_view(), name='responsavel_create'),
    path('responsaveis/<int:pk>/', ResponsavelDetailView.as_view(), name='responsavel_detail'),
    path('responsaveis/<int:pk>/editar/', ResponsavelUpdateView.as_view(), name='responsavel_update'),
    path('responsaveis/<int:pk>/excluir/', ResponsavelDeleteView.as_view(), name='responsavel_delete'),

    # Equipamento
    path('equipamentos/', EquipamentoListView.as_view(), name='equipamento_list'),
    path('equipamentos/novo/', EquipamentoCreateView.as_view(), name='equipamento_create'),
    path('equipamentos/<int:pk>/', EquipamentoDetailView.as_view(), name='equipamento_detail'),
    path('equipamentos/<int:pk>/editar/', EquipamentoUpdateView.as_view(), name='equipamento_update'),
    path('equipamentos/<int:pk>/excluir/', EquipamentoDeleteView.as_view(), name='equipamento_delete'),

    # Alocacao
    path('alocacoes/', AlocacaoListView.as_view(), name='alocacao_list'),
    path('alocacoes/novo/', AlocacaoCreateView.as_view(), name='alocacao_create'),
    path('alocacoes/<int:pk>/', AlocacaoDetailView.as_view(), name='alocacao_detail'),
    path('alocacoes/<int:pk>/editar/', AlocacaoUpdateView.as_view(), name='alocacao_update'),
    path('alocacoes/<int:pk>/excluir/', AlocacaoDeleteView.as_view(), name='alocacao_delete'),
]
