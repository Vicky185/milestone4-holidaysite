from django.shortcuts import render

# Create your views here.
def view_cart(request):
    """ a view that renders the shopping cart contents page """
    return render(request, 'shoppingcart/cart.html')
    