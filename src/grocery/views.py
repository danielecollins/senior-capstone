import django
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def search_results_view(request, *args, **kwargs):
    return render(request, "search_results.html", {})

def add_item_view(request, *args, **kwargs):
    return render(request, "add_item.html", {})

def shopping_list_view(request, *args, **kwargs):
    return render(request, "shopping_list.html", {})