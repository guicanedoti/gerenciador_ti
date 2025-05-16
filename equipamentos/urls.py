from django.urls import path
from .views import EquipamentoListView

urlpatterns = [
    path('', EquipamentoListView.as_view(), name='equipament_list'),  # página inicial
]
