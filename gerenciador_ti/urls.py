from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('equipamentos.urls')),  # ✅ Redireciona para as URLs do app "equipamentos"
]
