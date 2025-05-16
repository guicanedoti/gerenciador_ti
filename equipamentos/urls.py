from django.urls import path
from . import views

app_name = 'equipamentos'

urlpatterns = [
    path('', views.EquipamentoListView.as_view(), name='lista'),
    path('novo/', views.EquipamentoCreateView.as_view(), name='novo'),
    path('<int:pk>/', views.EquipamentoDetailView.as_view(), name='detalhe'),
    path('<int:pk>/editar/', views.EquipamentoUpdateView.as_view(), name='editar'),
]
