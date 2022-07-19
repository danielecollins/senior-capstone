import django
from django.shortcuts import render
from .models import Item
from .forms import AddItemForm, UpdateWalmartPriceForm, UpdateBroulimsPriceForm, UpdateAlbertsonsPriceForm

# Create your views here.
def home_view(request, *args, **kwargs):
    context = {

    }
    return render(request, "home.html", context)

def search_results_view(request, *args, **kwargs):
    # Needs fixing, doesn't work if the search isn't in the database.
    search = request.GET['q']
    item = Item.objects.get(name=search)
    if item is None:
        item = 0
    context = {
        "item": item
    }
    return render(request, "search_results.html", context)

def add_item_view(request, *args, **kwargs):
    form = AddItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AddItemForm()

    context = {
        'form': form,
    }
    return render(request, "add_item.html", context)

def update_price_view(request, *args, **kwargs):
    walmart_form = UpdateWalmartPriceForm(request.POST or None)
    if walmart_form.is_valid():
        walmart_form.save()
        walmart_form = UpdateWalmartPriceForm()

    broulims_form = UpdateBroulimsPriceForm(request.POST or None)
    if broulims_form.is_valid():
        broulims_form.save()
        broulims_form = UpdateBroulimsPriceForm()

    albertsons_form = UpdateAlbertsonsPriceForm(request.POST or None)
    if albertsons_form.is_valid():
        albertsons_form.save()
        albertsons_form = UpdateAlbertsonsPriceForm()
    
    context = {
        'walmart_form': walmart_form,
        'broulims_form': broulims_form,
        'albertsons_form': albertsons_form,
    }
    return render(request, "update_price.html", context)

def shopping_list_view(request, *args, **kwargs):
    context = {
        "walmart_list": [],
        "broulims_list": ["Lays Potato Chips", "Salsa"],
        "albertsons_list": ["Ham", "Doritos", "Milk", "Eggs"],
    }
    return render(request, "shopping_list.html", context)