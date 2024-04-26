from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from .models import Product, Cart, CartItem
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    search_query = request.GET.get('search', '')  # Get the search parameter from the URL
    if search_query:
        products = Product.objects.filter(name__icontains=search_query) | Product.objects.filter(description__icontains=search_query)
    else:
        products = Product.objects.all()  # No search query, show all products
    
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('Welcome to Licia store New Arrivals')

def cart_detail(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    cart, created = Cart.objects.get_or_create(session_key=session_key)
    return render(request, 'cart_details.html', {'cart': cart})

def cart_add(request, product_id):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    cart, created = Cart.objects.get_or_create(session_key=session_key)
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

def cart_remove(request, product_id):
    session_key = request.session.session_key
    cart = get_object_or_404(Cart, session_key=session_key)
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')

def checkout(request):
    # Initialize default context with None or default values
    payment_type = None
    
    if request.method == 'POST':
        # Get the payment type from POST request data
        payment_type = request.POST.get('payment_type')
        # Add any necessary logic based on the payment type
        return redirect('payment_confirmation', payment_type=payment_type)
    
    # Ensure that payment_type or any other necessary data is included in the context
    context = {
        'payment_type': payment_type,  # This will be None on GET requests
    }
    return render(request, 'checkout.html', context)


def payment_confirmation(request, payment_type):
    # Ensure the template gets the payment_type correctly
    return render(request, 'payment_confirmation.html', {'payment_type': payment_type})

# def product_list(request):
#     search_query = request.GET.get('search', '')  # Get the search parameter from the URL
#     if search_query:
#         # Filter products based on the search query
#         products = Product.objects.filter(name__icontains=search_query) | Product.objects.filter(description__icontains=search_query)
#     else:
#         products = Product.objects.all()  # No search query, show all products
    
#     return render(request, 'index.html', {'products': products})
