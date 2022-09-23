from django import forms
from .models import Customer, Store, Menu
 
 
# creating a form
class StoreForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Store
 
        # specify fields to be used
        fields = [
            "name",
            "address",
        ]
        
# creating a form
class MenuForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = Menu
 
        # specify fields to be used
        fields = [
            "item_name",
            "price",
        ]
        
class OrderForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Customer
 
        # specify fields to be used
        fields = [
            "name",
            "address",
        ]