# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def get_index(request):
    return render(request, 'index.html')

# Get Contact Page
def get_contact(request):
   return render(request, 'contacts/contact.html')


# Get Contact Thank You Page
def get_contact_thanks(request):
   return render(request, 'contacts/contact_thanks.html')