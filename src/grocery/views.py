import django
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Price Pal</h1>")

def search_results_view(*args, **kwargs):
    return HttpResponse("<h1>Search Results</h1>")

def add_item_view(*args, **kwargs):
    return HttpResponse("<h1>Add an Item</h1>")

def shopping_list_view(*args, **kwargs):
    return HttpResponse("<h1>Shopping List</h1>")