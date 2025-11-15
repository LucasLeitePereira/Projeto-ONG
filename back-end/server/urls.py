from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api/voluntarios/', include('voluntarios.urls')),
    path('api/vitimas/', include('vitimas.urls')),
    path('api/atendimentos/', include('atendimentos.urls')),
]