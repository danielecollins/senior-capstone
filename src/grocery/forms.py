from ast import Try
from tkinter import Variable
from django import forms
from .models import Item

class AddItemForm(forms.ModelForm):
    name = forms.CharField(label="Item Name:", widget=forms.TextInput(attrs={"placeholder": "Item Name"}))
    quantity = forms.CharField(required=False)
    walmart_price = forms.DecimalField(required=False, label="Walmart Price:", widget=forms.NumberInput(attrs={"placeholder": 0.00}))
    broulims_price = forms.DecimalField(required=False, label="Broulim's Price:", widget=forms.NumberInput(attrs={"placeholder": 0.00}))
    albertsons_price = forms.DecimalField(required=False, label="Albertsons Price:", widget=forms.NumberInput(attrs={"placeholder": 0.00}))

    class Meta:
        model = Item
        fields = [
            'name',
            'quantity',
            'walmart_price',
            'broulims_price',
            'albertsons_price'
        ]
    
    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get("name")
        name = name.lower()

        try:
            if Item.objects.get(name=name) != None:
                raise forms.ValidationError("This item is already in the database.")
        except:
            return name        