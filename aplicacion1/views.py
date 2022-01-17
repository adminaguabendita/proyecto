from typing import Any
from django.shortcuts import render, HttpResponse, redirect
from aplicacion1.forms import FormTiendas
from aplicacion1.models import Tienda
from django.contrib import messages

# Create your views here.


def index(request):
   

    return render(request, 'index.html', {
        'title' : 'Inicio'
    })

def tiendas(request):
    formulario = FormTiendas()
    tiendas = get_tiendas(request)
    return render(request, 'tiendas.html', {
        'title' : 'Crear tienda',
        'title2' : 'Tiendas',
        'form': formulario,
        'tiendas': tiendas
    })


# Vista para recibir datos desde un formulario
def save_tienda(request):
    #Para recibir datos por el boton Guardar
    if request.method == "POST":   
        co = request.POST['co']
        descripcion = request.POST['descripcion']
        
        # Se definen los campos a llevar a la tabla
        tienda = Tienda(
            co = co,
            descripcion = descripcion            
        )
        # Se guarda en la tabla de la BD
        
        tienda.save()
        #return HttpResponse(f"Articulo creado: <strong>{articulo.title} {articulo.content}")
        # Redireccion al nombre de la página
        #return HttpResponse("<h2>Se ha creado el articulo</h2>")

        #Crear mensaje flash
        messages.success(request, f'Elemento guardado: {tienda.co}')
        return redirect('tiendas')
        



def get_tiendas(request):
    # Se consultan toda la info de la tabla
    tiendas = Tienda.objects.all().order_by("co")

    return tiendas

def delete_tienda(request, co):
    tienda = Tienda.objects.get(co=co)
    
    tienda.delete()
    messages.success(request, f'Elemento eliminado: {co}')
    # Redireccion al nombre de la página
    return redirect('tiendas')
    