
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('products/', products, name="products"),
    path('customers/', customers, name="customers"),
    path('sellers/', sellers, name="sellers"),
    path('signup/', signup, name="signup"),

    path('productFrom/', productsForm, name="productForm"),
    path('productFrom2/', productsForm2, name="productForm2"),

    path('buscar_producto/', buscarProducto, name="buscar_producto"),
    path('buscar2/', buscar2, name="buscar2"),
]
