from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ProductForm


# @login_required
def product_list(request):
    # if request.method == 'GET':
    #     form = ProductForm()
    return render(request, 'product/list.html')


# @login_required
def product_create(request):
    form = ProductForm()
    return render(request, 'product/product_create.html')


# , {'form': form}
