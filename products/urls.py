from django.urls import path
import products
from . import views


urlpatterns = [
    path('',  views.index, name='index'),
    path('new/', views.new),
    path('cart/', views.cart_detail, name='cart_detail'),
    # path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('checkout/', views.checkout, name='checkout'),
    # path('products/', views.product_list, name='product_list'),
    path('payment-confirmation/<str:payment_type>/', views.payment_confirmation, name='payment_confirmation'),
]