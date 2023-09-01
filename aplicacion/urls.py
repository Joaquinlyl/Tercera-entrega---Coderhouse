from django.urls import path,include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('products/', products, name="products"),


    path('signup/', signup, name="signup"),

    path('productFrom/', productsForm, name="productForm"),
    path('productFrom2/', productsForm2, name="productForm2"),

    path('customerForm/', customerForm, name="customerForm"),
    path('customerForm2/', customerForm2, name="customerForm2"),

    path('sellerFrom/', sellerForm, name="sellerForm"),
    path('sellerFrom2/', sellerForm2, name="sellerForm2"),

    path('SearchProduct/', SearchProduct, name="SearchProduct"),
    path('search2/', search2, name="search2"),

    #------ bad way to do it#
    path('sellers/', sellers, name="sellers"),


    #------based views#
    path('customers/', Customer_list.as_view(), name="customers"),
    path('create_customer/', CustomerCreate.as_view(), name="create_customer"),
    path('update_customer/<int:pk>', CustomerUpdate.as_view(), name="update_customer"),
    path('delete_customer/<int:pk>', CustomerDelete.as_view(), name="delete_customer"),

    #login
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('registry/', register, name="registry"),
    path('edit_profile/', editProfile, name="edit_profile"),
    path('add_avatar/', addAvatar, name="add_avatar"),

]
