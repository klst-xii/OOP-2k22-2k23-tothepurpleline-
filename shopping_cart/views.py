from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http.response import HttpResponseRedirect

from products.models import Product
from socials.models import UserProfile

from django.urls import reverse_lazy
import datetime
from django.contrib import messages
from shopping_cart.extras import generate_order_id
from shopping_cart.models import OrderItem, Order
from django.contrib.auth.decorators import login_required

def get_user_pending_order(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=True)
    if order.exists():
        return order[0]
    return 0

# Create your views here.
@login_required()
def add_to_cart(request, **kwargs):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    if product in request.user.profile.materials.all():
        messages.info(request, 'You already own this ebook')
        return redirect(reverse('products:product-list'))
    order_item, status = OrderItem.objects.get_or_create(product=product)
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=True)
    user_order.items.add(order_item)
    if status:
        user_order.ref_code = generate_order_id()
        user_order.save()
    messages.info(request, "item added to cart")
    return redirect(reverse('products:product-list'))


@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('shopping_cart:order_summary'))


@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/order_summary.html', context)


@login_required()
def checkout(request):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order,
    }
    return render(request, 'shopping_cart/checkout.html', context)


@login_required()
def process_payment(request, order_id):
    return redirect(reverse('shopping_cart:update_records',
                            kwargs={
                                'order_id': order_id,
                            })
                        )


@login_required()
def update_transaction_records(self, request, order_id):
    order_to_purchase = Order.objects.filter(pk=order_id).first()
    order_to_purchase.is_ordered=True
    order_to_purchase.date_ordered=datetime.datetime.now()
    order_to_purchase.save()

    order_items = order_to_purchase.items.all()
    order_items.update(is_ordered=True, date_ordered=datetime.datetime.now())

    user_profile = get_object_or_404(UserProfile, user=request.user)
    order_products = [item.product for item in order_items]
    user_profile.materials.add(*order_products)
    user_profile.save()

    messages.info(request, "Items have been added to your profile successfully!")
    return HttpResponseRedirect(reverse_lazy('profile', kwargs={'order_id': pk}))


def success(request, **kwargs):
    return render(request, 'shopping_cart/purchase_success.html', pk=generate_order_id() )


