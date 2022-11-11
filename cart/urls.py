from django.urls import path, re_path
from cart.views import add_to_cart, cart_home, decrease_cart, increase_cart, remove_from_cart

app_name = 'cart'

urlpatterns = [
    re_path(r'^$', cart_home, name='cart-home'),
    # re_path(r'^decrease-item/<int:pk>/$', decrease_cart, name='decrease-item'),
    # re_path(r'^increase-item/<int:pk>/$', increase_cart, name='increase-item'),
    # re_path(r'^remove-item/int<int:pk>/$', remove_from_cart, name='remove-item'),
    # re_path(r'^add/<int:pk>/$', add_to_cart, name='add'),

]