from django.shortcuts import render
from .models import List

def shopping_list_view(request, *args, **kwargs):
    
    walmart_list = []
    broulims_list = []
    albertsons_list = []

    context = {
        "walmart_list": walmart_list,
        "broulims_list": broulims_list,
        "albertsons_list": albertsons_list,
    }
    return render(request, "shopping_list.html", context)