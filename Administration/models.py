from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    current_volume = models.IntegerField()
    min_av_volume = models.IntegerField()
    cost_per_1_kg = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=50)
    descritpion = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    weight = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    dishes = models.ManyToManyField(Dish)
    last_time_changed = models.DateTimeField()
    
    def __str__(self):
        return self.name