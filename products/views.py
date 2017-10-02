from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

@login_required
def all_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})

