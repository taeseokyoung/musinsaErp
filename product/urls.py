from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.product_list, name='list'),
    path('create/', views.product_create, name='create'),
]
