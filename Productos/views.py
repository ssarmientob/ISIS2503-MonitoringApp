from django.shortcuts import render
from .forms import ProductoForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .logic.logic_producto import create_producto, get_productos, edit_producto, delete_producto
from django.contrib.auth.decorators import login_required
import requests
from abc import ABC
from social_core.backends.oauth import BaseOAuth2


def getRole(request):
    user = request.user
    auth0user = user.social_auth.get(provider="auth0")
    accessToken = auth0user.extra_data['access_token']
    url = "https://isis2503-miguelmunoz2019.auth0.com/userinfo"
    headers = {'authorization': 'Bearer ' + accessToken}
    resp = requests.get(url, headers=headers)
    userinfo = resp.json()
    role = userinfo['https://isis2503-miguelmunoz2019:auth0:com/role']
    return role


def producto_list(request):
    productos = get_productos()
    context = {
        'producto_list': productos
    }
    return render(request, 'Producto/productos.html', context)


@login_required
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            create_producto(form)
            messages.add_message(request, messages.SUCCESS, 'Producto create successful')
            return HttpResponseRedirect(reverse('productoCreate'))
        else:
            print(form.errors)
    else:
        form = ProductoForm()

    context = {
        'form': form,
    }

    return render(request, 'Producto/ProductoCreate.html', context)


@login_required
def producto_edit(request):
    if request.method == 'PUT':
        form = ProductoForm(request.PUT)
        if form.is_valid():
            edit_producto(form)
            messages.add_message(request, messages.SUCCESS, 'Producto edit successful')
            return HttpResponseRedirect(reverse('productoEdit'))
        else:
            print(form.errors)
    else:
        form = ProductoForm()

    context = {
        'form': form,
    }

    return render(request, 'Producto/ProductoEdit.html', context)


@login_required
def producto_delete(request, id):
    productos = delete_producto(id)
    context = {
        'producto_list': productos
    }
    return render(request, 'Producto/productos.html', context)

@login_required
def admin_list(request):
    role = getRole(request)
    if role == "Administracion Antusu":
        productos = get_productos()
        context = {
            'producto_list': productos
        }
        return render(request, 'Producto/productosAdmin.html', context)
    else:
        return HttpResponse("Unauthorized User")
