from ..models import Producto

def get_productos():
    queryset = Producto.objects.all().order_by('nombre')[:10]
    return (queryset)

def create_producto(form):
    producto = form.save()
    producto.save()
    return ()

def edit_producto(form):
    producto = form.save()
    producto.save()
    return ()


def delete_producto(id):
    Producto.objects.all.remove(id)
    queryset = Producto.objects.all().order_by('nombre')
    return (queryset)