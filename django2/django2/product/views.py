from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'
