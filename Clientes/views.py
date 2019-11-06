from django.shortcuts import render
from .forms import ClienteForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_cliente import create_cliente, get_clientes

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

