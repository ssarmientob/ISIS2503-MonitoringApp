from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('productos/', views.producto_list),
    path('productocreate/', csrf_exempt(views.producto_create), name='productoCreate'),
]