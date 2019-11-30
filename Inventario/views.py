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


def inventario_list(request):
    inventarios = get_inventarios()
    context = {
        'inventario_list': inventarios
    }
    return render(request, 'Inventario/inventarios.html', context)


@login_required
def inventario_create(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            create_inventario(form)
            messages.add_message(request, messages.SUCCESS, 'Inventario create successful')
            return HttpResponseRedirect(reverse('inventarioCreate'))
        else:
            print(form.errors)
    else:
        form = InventarioForm()

    context = {
        'form': form,
    }

    return render(request, 'Inventario/InventarioCreate.html', context)


@login_required
def inventario_edit(request):
    if request.method == 'PUT':
        form = InventarioForm(request.PUT)
        if form.is_valid():
            edit_inventario(form)
            messages.add_message(request, messages.SUCCESS, 'Inventario edit successful')
            return HttpResponseRedirect(reverse('inventarioEdit'))
        else:
            print(form.errors)
    else:
        form = InventarioForm()

    context = {
        'form': form,
    }

    return render(request, 'Inventario/InventarioEdit.html', context)


@login_required
def inventario_delete(request, id):
    inventarios = delete_inventario(id)
    context = {
        'inventario_list': inventarios
    }
    return render(request, 'Inventario/inventarios.html', context)

@login_required
def admin_list(request):
    role = getRole(request)
    if role == "Administracion Antusu":
        inventarios = get_inventarios()
        context = {
            'inventario_list': inventarios
        }
        return render(request, 'Inventario/inventariosAdmin.html', context)
    else:
        return HttpResponse("Unauthorized User")
