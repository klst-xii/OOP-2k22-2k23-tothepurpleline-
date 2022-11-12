from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.views import Product


# def cart_home(request):
#     cart_obj = Cart.objects.new_or_get(request)
#     return render(request, "carts/home.html")
def cart_home(request):
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, purchased=False)
        orders = Order.objects.filter(user=request.user, ordered=False)
        if carts.exists() and orders.exists():
            order = orders[0]
            print(order)
            context = {
                'carts': carts,
                'order': order
            }
            return render(request, 'carts/home.html', context)
        else:
            return render(request, "carts/home.html")
    else:
        return redirect('login')


def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(products=item, user=request.user)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(products=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, "This item quantity was updated!")
            return redirect('products:product_list')
        else:
            order.orderitems.add(order_item[0])
            messages.info(request, "This item was added to your cart!")
            return redirect('products:product_list')
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request, "This item was added to your cart!")
        return redirect('products:product_list')


def remove_from_cart(request, pk): #ito ba yung post niyo kumbaga?
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(products=item).exists():
            order_item = Cart.objects.filter(products=item, user=request.user)[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            messages.warning(request, "This item was removed from your cart")
            return redirect('cart:cart-home')
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('products:product_list')
    else:
        messages.info(request, "You don't have an active order")
        return redirect('products:product_list')


@login_required
def increase_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, order=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(products=item).exists():
            order_item = Cart.objects.filter(products=item, user=request.user)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                return redirect('cart:cart-home')
        else:
            return redirect('products:product_list')
    else:
        return redirect('products:product_list')


@login_required
def decrease_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(products=item).exists():
            order_item = Cart.objects.filter(products=item, user=request.user)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                return redirect('cart')
            else:
                order.orderitems.remove(order_item)
                order_item.delete
                return redirect('cart')
        else:
            return redirect('products:product_list')
    else:
        return redirect('products:product_list')
