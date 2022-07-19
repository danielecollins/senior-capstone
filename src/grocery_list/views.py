from django.shortcuts import render
from .models import List

def shopping_list_view(request, *args, **kwargs):
    if item.walmart_price <= item.broulims_price and item.walmart_price <= item.albertsons_price:
        price = item.walmart_price
    elif item.broulims_price < item.albertsons_price:
        price = item.broulims_price
    else:
        price = item.albertsons_price

    walmart_list = []
    broulims_list = []
    albertsons_list = []

    context = {
        "walmart_list": walmart_list,
        "broulims_list": broulims_list,
        "albertsons_list": albertsons_list,
    }
    return render(request, "shopping_list.html", context)