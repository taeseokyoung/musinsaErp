from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import UserForm


# Create your views here.


def sign_up_view(request):

    if request.method == 'GET':
        form = UserForm()
        return render(request, 'user/signup.html', {'form': form})

    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
        else:
            return render(request, 'user/signup.html', {'form': form})


def sign_in_view(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            login(request, form)
        return render(request, 'product/list.html', {'form': form})

    elif request.method == 'GET':
        form = UserForm()
        return render(request, 'user/signin.html', {'form': form})
