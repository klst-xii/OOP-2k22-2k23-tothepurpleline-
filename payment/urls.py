from django.urls import re_path
from payment.views import checkout

app_name = 'payment'

urlpatterns = [
    re_path(r'^checkout/$', checkout, name='checkout'),
]