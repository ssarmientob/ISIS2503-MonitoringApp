from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('inventarios/', views.inventario_list),
    path('inventriosAdmin/', views.admin_list),
    path('inventariocreate/', csrf_exempt(views.inventario_create), name='inventarioCreate'),
    path('inventarioedit/', csrf_exempt(views.inventario_edit), name='inventarioEdit'),
]
