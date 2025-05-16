from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipamentos/', include('equipamentos.urls')),  # já está aí
    path('', include('equipamentos.urls')),  # <-- adiciona essa linha!
]
