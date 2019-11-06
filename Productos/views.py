from django.shortcuts import render
from .forms import ProductoForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .logic.logic_producto import create_producto, get_productos, edit_producto, delete_producto
from django.contrib.auth.decorators import login_required



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

    productos =delete_producto(id)
    context = {
        'producto_list': productos
    }
    return render(request, 'Producto/productos.html', context)

@login_required
def admin_list(request):
   
        return HttpResponse("Unauthorized User")




