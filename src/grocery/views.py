from venv import create
from django.shortcuts import render
from .models import Item
from grocery_list.models import List
from .forms import AddItemForm
from pattern.text.en import singularize

def home_view(request, *args, **kwargs):
    # Render the search/home page
    context = {
    }
    return render(request, "home.html", context)

def search_results_view(request, *args, **kwargs):
    # Search functionality
    search = request.GET['search']
    search = search.lower().strip(' ')

    query = singularize(search)
    items = Item.objects.filter(name__contains=query)

    # Pull data to put into shopping list
    if request.method == "POST":
        id = request.POST.get('id')

        item = Item.objects.get(id=id)
        if item.broulims_price is None and item.albertsons_price is None or item.walmart_price <= item.broulims_price and item.walmart_price <= item.albertsons_price:
            store = "walmart"
        elif item.albertsons_price is None or item.broulims_price < item.albertsons_price:
            store = "broulims"
        else:
            store = "albertsons"

        # Populate/Update shopping list
        try:
            list_item = List.objects.get(item_id=id)
            current_quantity = list_item.quantity
            list_item.quantity = current_quantity + 1
            list_item.save()
        except:
            new_list_item = List(store=store, quantity=1, item_id=id)
            new_list_item.save()

    context = {
        "items": items,
        "search": search,
    }
    return render(request, "search_results.html", context)

def add_item_view(request, *args, **kwargs):
    # Pass over the item name from the search results
    try:
        name = request.GET['name']
    except:
        name = None

    # Create a new item
    form = AddItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AddItemForm()

    context = {
        'form': form,
        'name': name,
    }
    return render(request, "add_item.html", context)

def update_price_view(request, *args, **kwargs):
    # Need to fix update statements
    # Get the item that needs a price update from the shopping list page
    if request.method == "GET":
        item = request.GET['item']

        if request.GET['store'] == "Broulims":
            store = "Broulim's"
        else:
            store = request.GET['store']

    # Update the prices
    if request.method == "POST":
        new_price = request.POST.get('price')
        if store == "Walmart":
            Item.objects.update(walmart_price=new_price)
        elif store == "Broulim's":
            Item.objects.update(broulims_price=new_price)
        elif store == "Albertsons":
            Item.objects.update(albertsons_price=new_price)

    context = {
        "store": store,
        "item": item,
    }
    return render(request, "update_price.html", context)