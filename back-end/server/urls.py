from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/', include('core.urls')),
    path('api/voluntarios/', include('voluntarios.urls')),
    path('api/vitimas/', include('vitimas.urls')),
    path('api/grutas/', include('grutas.urls')),
    path('api/atendimentos/', include('atendimentos.urls')),
]