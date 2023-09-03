from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('signup/', signup, name="signup"),
    path('about_me/', about_me, name="about_me"),

    #Product view and product lookup
    path('productFrom/', productsForm, name="productForm"),
    path('productFrom2/', productsForm2, name="productForm2"),
    path('SearchProduct/', SearchProduct, name="SearchProduct"),
    path('search2/', search2, name="search2"),
    path('products/', products, name="products"),

    #------Class based views#

    #------Customers#
    path('customers/', Customer_list.as_view(), name="customers"),
    path('create_customer/', CustomerCreate.as_view(), name="create_customer"),
    path('update_customer/<int:pk>', CustomerUpdate.as_view(), name="update_customer"),
    path('delete_customer/<int:pk>', CustomerDelete.as_view(), name="delete_customer"),

    #------categories#
    path('categories/', Category_list.as_view(), name="categories"),
    path('create_category/', CategoryCreate.as_view(), name="create_category"),
    path('update_category/<int:pk>', CategoryUpdate.as_view(), name="update_category"),
    path('delete_category/<int:pk>', CategoryDelete.as_view(), name="delete_category"),

    #------sellers#
    path('sellers/', Seller_list.as_view(), name="sellers"),
    path('create_seller/', SellerCreate.as_view(), name="create_seller"),
    path('update_seller/<int:pk>', SellerUpdate.as_view(), name="update_seller"),
    path('delete_seller/<int:pk>', SellerDelete.as_view(), name="delete_seller"),

    #login
    path('aplicacion/login/', login_request, name="login"),
    path('aplicacion/logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('registry/', register, name="registry"),
    path('edit_profile/', editProfile, name="edit_profile"),
    path('add_avatar/', addAvatar, name="add_avatar"),

]
