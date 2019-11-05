from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('productos/', views.producto_list),
    path('productosAdmin/', views.admin_list),
    path('productocreate/', csrf_exempt(views.producto_create), name='productoCreate'),
    path('productoedit/', csrf_exempt(views.producto_edit), name='productoEdit'),
]