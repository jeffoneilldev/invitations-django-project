from django.shortcuts import render, redirect, reverse

# My shopping cart views...

def view_cart(request):
    """Shows contents of the cart page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add quantity of specific invitation to the cart"""
    
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """Adjust quantity of specific invitation by another amount"""
    
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    