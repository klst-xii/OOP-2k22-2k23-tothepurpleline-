from django.shortcuts import render
from products.models import Product
# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "product/list.html"
    
class ProductDetailView(DetailView):
     queryset = Product.objects.all()
     template_name = "products/detail.html"
        
