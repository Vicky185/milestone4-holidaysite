from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from packages.models import Package


# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'shoppingcart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """
    package = get_object_or_404(Package, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated your travels to include {package.name}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {package.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)

def adjust_cart(request, item_id):
    """Adjust the quantity of the specified items to specific amount"""
    package = get_object_or_404(Package, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated your travels to {cart[item_id]}')
    else:
        del cart[item_id]
        if not cart[item_id]:
            cart.pop(item_id)
        messages.success(request, f'Removed {package.name} from your travels')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_from_cart(request, item_id):
    """ Remove item from the cart """
    cart = request.session.get('cart', {})
    package = get_object_or_404(Package, pk=item_id)

    if item_id in cart:
        del cart[item_id]
    messages.success(request, f'Removed {package.name} from your travels')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
