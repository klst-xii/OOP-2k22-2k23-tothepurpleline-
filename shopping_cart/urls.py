from django.urls import re_path

from .views import add_to_cart, delete_from_cart, order_details, checkout, process_payment, update_transaction_records, success

app_name = 'shopping_cart'

urlpatterns = [
    re_path(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    re_path(r'^order-summary/$', order_details, name="order_summary"),
    re_path(r'^success/$', success, name='purchase_success'),
    re_path(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    re_path(r'^checkout/$', checkout, name='checkout'),
    re_path(r'^payment/(?P<order_id>[-\w]+)/$', process_payment, name='process_payment'),
    re_path(r'^update-transaction/(?P<order_id>[-\w]+)/$', update_transaction_records, name='update_records'),
]