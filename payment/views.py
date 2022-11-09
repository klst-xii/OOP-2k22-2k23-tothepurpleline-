from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.

from carts.models import Order, Cart
from payment.forms import BillingAddressForm
from payment.models import BillingAddress


def checkout(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    form = BillingAddressForm(instance=saved_address)
    if request.method == 'POST':
        form = BillingAddressForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingAddressForm(instance=saved_address)

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_items = order_qs[0].orderitems.all()
    order_total = order_qs[0].get_totals()
    context = {
        'form' = form,
        'order_items': order_items,
        'order_total': order_total,
        'saved_address': saved_address
    }
    return render(request, 'payment/checkout.html', context)


def payment(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    if not saved_address.is_fully_fulfilled():
        messages.info(request, "please complete shipping address")
        return redirect('payment:checkout')

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    for order in order_qs:
        order.ordered = True
        order.save()
    cart_items = Cart.objects.filter(user=request.user, purchased=False)
    for item in cart_items:
        item.purchased = True
        item.save()

    return redirect('cart:cart_home')