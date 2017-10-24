# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render



def get_index(request):
    return render(request, 'index.html')



# Get Contact Thank You Page
def get_contact_thanks(request):
   return render(request, 'contacts/contact_thanks.html')

# Get About page
def get_About(request):
   return render(request, 'About/About.html')

# Get product page
def get_products(request):
   return render(request, 'products/products.html')

# Get product page
def get_paypal_cancel(request):
   return render(request, 'paypal/paypal_cancel.html')

# Get product page
def get_paypal_return(request):
   return render(request, 'paypal/paypal_return.html')

