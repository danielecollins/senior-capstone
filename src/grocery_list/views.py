import this
from django.shortcuts import render
from .models import List
from grocery.models import Item

def shopping_list_view(request, *args, **kwargs):
    #Delete item from shopping list
    if request.method == "POST":
        id = request.POST.get('id')
        quantity = int(request.POST.get('quantity'))

        item_to_be_deleted = List.objects.get(id=id)

        if quantity > 1:
            item_to_be_deleted.quantity -= 1
            item_to_be_deleted.save()
        else:
            item_to_be_deleted.delete()

    #Collect data for shopping list population
    grocery_list = List.objects.all()
    walmart_list = []
    broulims_list = []
    albertsons_list = []
    
    for list_obj in grocery_list:
        item = Item.objects.get(id=list_obj.item_id)
        store = list_obj.store

        if store == "walmart":
            price = item.walmart_price
        elif store == "broulims":
            price = item.broulims_price
        else:
            price = item.albertsons_price

        quantity = list_obj.quantity
        name = item.name
        id = list_obj.id

        list_item = {"store": store, "quantity":quantity, "name": name,"price": price, "id": id}

        if store == "walmart":
            walmart_list.append(list_item)
        elif store == "broulims":
            broulims_list.append(list_item)
        else:
            albertsons_list.append(list_item)

    

    context = {
        "walmart_list": walmart_list,
        "broulims_list": broulims_list,
        "albertsons_list": albertsons_list,
    }
    return render(request, "shopping_list.html", context)