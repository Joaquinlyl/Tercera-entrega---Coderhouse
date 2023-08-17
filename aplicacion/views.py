from django.shortcuts import render
from django.http import HttpResponse

from .models import *


# Create your views here.
def home(request):
    return render(request,"aplicacion/home.html")

def products(request):
    contexto = {'products': product.objects.all()}
    return render(request,"aplicacion/products.html",contexto)
def customers(request):
    return render(request,"aplicacion/customers.html")
def sellers(request):
    return render(request,"aplicacion/sellers.html")
def signup(request):
    return render(request,"aplicacion/signup.html")

def productsForm(request):
    if request.method == "POST":
        curso = product(product_name = request.POST['product_name'], product_price = request.POST['product_price'])

        curso.save()
        return HttpResponse("Se guardo el producto con exito")
    return render( request, "aplicacion/productsForm.html")

def productsForm2(request):
    if request.method == "POST":
        miform = productsForm(request.POST)
        if miform.is_valid():
            proudcts_name = miform.cleaned_data.get('name')
            proudct_price = miform.cleaned_data.get('price')
            curso = product(name = proudcts_name, price = proudct_price)

            curso.save()
            return  render(request, "aplicacion/base.html")

    else:
        miForm: productsForm()

    return render(request, "aplicacion/curso2.html", {"form": miForm} )

def buscarProducto(request):
    return render(request, "aplicacion/buscarProducto.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        productos = product.objects.filter(product_name__icontains=patron)
        contexto = {"productos": productos}
        return render(request,"aplicacion/products.html",contexto)

    return HttpResponse ("No se encontro nada en la busqueda")
