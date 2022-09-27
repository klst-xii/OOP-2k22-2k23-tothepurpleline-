from django.shortcuts import render
from products.models import Product
# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView


class ProductFeaturedListView(ListView):
    template_name = "product/list.html"
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/detail.html"
        
     def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/detail.html"
    
