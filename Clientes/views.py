from django.shortcuts import render
from .forms import ClienteForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .logic.logic_cliente import create_cliente, get_clientes
from django.contrib.auth.decorators import login_required
import requests


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


def cliente_list(request):
    clientes = get_clientes()
    context = {
        'cliente_list': clientes
    }
    return render(request, 'Cliente/clientes.html', context)


def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            create_cliente(form)
            messages.add_message(request, messages.SUCCESS, 'Cliente create successful')
            return HttpResponseRedirect(reverse('clienteCreate'))
        else:
            print(form.errors)
    else:
        form = ClienteForm()

    context = {
        'form': form,
    }

    return render(request, 'CLiente/ClienteCreate.html', context)


def admin_list(request):
    clientes  = get_clientes()
    context = {
        'cliente_list': clientes
    }
    return render(request, 'Cliente/clienteAdmin.html', context)


@login_required
def cliente_indv(request):
    role = getRole(request)
    if role == "Cliente Antusu":
        return render(request, 'Cliente/clienteIndividual.html')
    else:
        return HttpResponse("Unauthorized User")


