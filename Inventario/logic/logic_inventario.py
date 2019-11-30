from ..models import Inventario

def get_inventarios():
    queryset = Inventario.objects.all().order_by('nombre')[:10]
    return (queryset)

def create_inventario(form):
    inventario = form.save()
    inventario.save()
    return ()

def edit_inventario(form):
    inventario = form.save()
    inventario.save()
    return ()


def delete_inventario(id):
    Inventario.objects.all.remove(id)
    queryset = Inventario.objects.all().order_by('nombre')
    return (queryset)