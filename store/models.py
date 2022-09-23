from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):

        return self.name


class Menu(models.Model):
    item_name = models.CharField(max_length=200)
    price = models.FloatField(default=0.00)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):

        return self.item_name
    

class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):

        return self.name
    
