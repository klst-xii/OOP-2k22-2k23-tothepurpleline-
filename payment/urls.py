from django.urls import re_path
from payment.views import checkout, payment

app_name = 'payment'

urlpatterns = [
    re_path(r'^checkout/$', checkout, name='checkout'),
    re_path(r'^final/$', payment, name='payments'),
]