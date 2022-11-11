from django.urls import path, re_path
from .views import ProductListView, ProductDetailSlugView, ProductFeaturedDetailView, ProductDetailView, ProductFeaturedListView

app_name = 'products'

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),

]