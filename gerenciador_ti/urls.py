from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views 
from equipamentos.views import home  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipamentos/', include('equipamentos.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    
    path('', home, name='home'),  
    
    
]
