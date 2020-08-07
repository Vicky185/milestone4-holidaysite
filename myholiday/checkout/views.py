from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "there's nothing in your cart at the moment")
        return redirect(reverse('packages'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HAIE2KM1us24aM9vfOHClJG14Xatx3oNqkfvZG4hpJYCGO2KIidZjGvrD81I8iHn4tstj5WppOjkU25rnrxyBVU00hUuVJSKU',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)