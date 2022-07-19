from django import forms
from .models import Item

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'name',
            'quantity',
            'walmart_price',
            'broulims_price',
            'albertsons_price'
        ]

class UpdateWalmartPriceForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'name',
            'walmart_price'
        ]

class UpdateBroulimsPriceForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'name',
            'broulims_price'
        ]

class UpdateAlbertsonsPriceForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'name',
            'albertsons_price'
        ]