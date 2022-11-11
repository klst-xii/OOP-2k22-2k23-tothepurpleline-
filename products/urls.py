from django.urls import re_path
from .views import ProductDetailView, ProductDetailSlugView, ProductListView

app_name = 'products'

urlpatterns = [
    re_path(r'^$', ProductListView.as_view(), name='product_list'),
    # re_path(r'^<int:pk>/$', ProductDetailView.as_view(), name='detailed'),
    # re_path(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
]