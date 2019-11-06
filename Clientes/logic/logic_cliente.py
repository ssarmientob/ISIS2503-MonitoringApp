from ..models import Cliente

def get_clientes():
    queryset = Cliente.objects.all().order_by('nombre')[:10]
    return (queryset)

def create_cliente(form):
    cliente = form.save()
    cliente.save()
    return ()

