from django.shortcuts import render
from .models import Item
from .forms import AddItemForm
from pattern.text.en import singularize

# Create your views here.
def home_view(request, *args, **kwargs):
    context = {
    }
    return render(request, "home.html", context)

def search_results_view(request, *args, **kwargs):
    search = request.GET['search']
    search = search.lower().strip(' ')

    query = singularize(search)
    items = Item.objects.filter(name__contains=query)

    context = {
        "items": items,
        "search": search,
    }
    return render(request, "search_results.html", context)

def add_item_view(request, *args, **kwargs):
    try:
        name = request.GET['name']
    except:
        name = None

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
    if request.method == "GET":
        item = request.GET['item']

        if request.GET['store'] == "Broulims":
            store = "Broulim's"
        else:
            store = request.GET['store']

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

def shopping_list_view(request, *args, **kwargs):
    context = {
        "walmart_list": [],
        "broulims_list": ["Lays Potato Chips", "Salsa"],
        "albertsons_list": ["Ham", "Doritos", "Milk", "Eggs"],
    }
    return render(request, "shopping_list.html", context)