import django
from django.shortcuts import render
from .models import Item

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "grocery/home.html", {})

def search_results_view(request, *args, **kwargs):
    item = Item.objects.get(id=1)
    context = {
        "item": item
    }
    return render(request, "grocery/search_results.html", context)

def add_item_view(request, *args, **kwargs):
    return render(request, "grocery/add_item.html", {})

def shopping_list_view(request, *args, **kwargs):
    context = {
        "walmart_list": [],
        "broulims_list": ["Lays Potato Chips", "Salsa"],
        "albertsons_list": ["Ham", "Doritos", "Milk", "Eggs"],
    }
    return render(request, "grocery/shopping_list.html", context)