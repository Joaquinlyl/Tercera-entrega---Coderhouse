from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, "aplicacion/home.html")

@login_required
def products(request):
    contexto = {'products': Product.objects.all()}
    return render(request, "aplicacion/products.html", contexto)


@login_required
def customers(request):
    return render(request, "aplicacion/customers.html")

@login_required
def signup(request):
    return render(request, "aplicacion/signup.html")

@login_required
def productsForm(request):
    if request.method == "POST":
        curso = Product(product_name=request.POST['product_name'], product_price=request.POST['product_price'])

        curso.save()
        return HttpResponse("Se guardo el producto con exito")
    return render(request, "aplicacion/productsForm.html")

@login_required
def productsForm2(request):
    if request.method == "POST":
        miform = productsForm(request.POST)
        if miform.is_valid():
            proudcts_name = miform.cleaned_data.get('name')
            proudct_price = miform.cleaned_data.get('price')
            curso = Product(name=proudcts_name, price=proudct_price)

            curso.save()
            return render(request, "aplicacion/base.html")

    else:
        miForm: productsForm()

    return render(request, "aplicacion/curso2.html", {"form": miForm})

@login_required
def sellerForm(request):
    if request.method == "POST":
        curso = Seller(username=request.POST['username'], password=request.POST['password'])

        curso.save()
        return HttpResponse("Se guardo el vendedor con exito")
    return render(request, "aplicacion/sellerForm.html")

@login_required
def sellerForm2(request):
    if request.method == "POST":
        miform = sellerForm(request.POST)
        if miform.is_valid():
            username = miform.cleaned_data.get('username')
            password = miform.cleaned_data.get('password')
            curso = Product(username=username, password=password)

            curso.save()
            return render(request, "aplicacion/base.html")

    else:
        miForm: productsForm()

    return render(request, "aplicacion/curso2.html", {"form": miForm})

@login_required
def customerForm(request):
    if request.method == "POST":
        curso = Seller(username=request.POST['username'], password=request.POST['password'])

        curso.save()
        return HttpResponse("Se guardo el cliente con exito")
    return render(request, "aplicacion/customer_form.html")

@login_required
def customerForm2(request):
    if request.method == "POST":
        miform = sellerForm(request.POST)
        if miform.is_valid():
            username = miform.cleaned_data.get('username')
            password = miform.cleaned_data.get('password')
            curso = Product(username=username, password=password)

            curso.save()
            return render(request, "aplicacion/base.html")

    else:
        miForm: productsForm()

    return render(request, "aplicacion/customer_form.html", {"form": miForm})

@login_required
def SearchProduct(request):
    return render(request, "aplicacion/buscarProducto.html")

@login_required
def search2(request):
    if request.GET['buscar']:
        pattern = request.GET['buscar']
        products = Product.objects.filter(product_name__icontains=pattern)
        context = {"products": products}
        return render(request, "aplicacion/products.html", context)

    return HttpResponse("No se encontro nada en la busqueda")


# ------------------------------# 28/08
@login_required
def sellers(request):
    context = {'sellers': Seller.objects.all()}
    return render(request, "aplicacion/sellers.html", context)


# class based view


class Customer_list(LoginRequiredMixin,ListView):
    model = Customer
class CustomerCreate(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ['username', 'password']
    success_url = reverse_lazy('customers')
class CustomerUpdate(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ['username', 'password']
    success_url = reverse_lazy('customers')
class CustomerDelete(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('customers')

#-----------------------------------------------#

class Category_list(LoginRequiredMixin,ListView):
    model = Category
class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['Category_name']
    success_url = reverse_lazy('categories')
class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['Category_name']
    success_url = reverse_lazy('categories')
class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('categories')




# Login/Logout/register

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            username = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar
                return render(request, "aplicacion/base.html", {'message': f'Welcome to our site!'})
            else:
                return render(request, "aplicacion/login.html",
                              {'form': miForm, 'mensaje': f'The username or password are not valid'})

        else:
            return render(request, "aplicacion/login.html",
                              {'form': miForm, 'mensaje': f'The username or password are not valid'})

    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = UserRegistryForm(request.POST)
        if miForm.is_valid():
            user = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = UserRegistryForm()
    return render(request, "aplicacion/registry.html", {"form":miForm})

@login_required
def editProfile(request):
    user = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            user.email = form.cleaned_data.get('email')
            user.password1 = form.cleaned_data.get('password1')
            user.password2 = form.cleaned_data.get('password2')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            return render(request,"aplicacion/base.html")
        else:
            return render(request,"aplicacion/editProfile.html", {'form': form, 'usuario': user.username})
    else:
        form = UserEditForm(instance=user)
    return render(request, "aplicacion/editProfile.html", {'form': form, 'usuario': user.username})


#Avatar
@login_required
def addAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)

            # ____ Delete old avatar
            oldAvatar = Avatar.objects.filter(user=u)
            if len(oldAvatar) > 0:
                for i in range(len(oldAvatar)):
                    oldAvatar[i].delete()

            # ____ Save new
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___ Make URL
            image = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = image
            return render(request,"aplicacion/base.html")
    else:
        form = AvatarForm()
    return render(request, "aplicacion/addAvatar.html", {'form': form})
