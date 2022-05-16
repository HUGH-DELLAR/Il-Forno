from django.db import models
from picklefield.fields import PickledObjectField
from django.contrib.auth.models import User

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
    photo = models.ImageField(null=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    dishes = models.ManyToManyField(Dish)
    last_time_changed = models.DateTimeField()
    display_priority = models.IntegerField()
    
    def __str__(self):
        return self.name

class Order(models.Model):
    order_date = models.DateTimeField()
    order_place = models.CharField(max_length=25)
    executor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dishes = PickledObjectField()
    order_status = models.IntegerField()
    
    def get_dishes(self):
        st = lambda x,y: f'{x}: {y}шт.'
        return '\n'.join([str(st(x,y)+"\n") for x,y in self.dishes.items()])

    def get_order_status(self):
        if self.order_status == 0:
            return 'Оформлен'
        elif self.order_status == 1:
            return 'В исполнении'
        elif self.order_status == 2:
            return 'Завершен'
        else:
            return 'Ошибка в оформлении заказа'
    
    def __str__(self):
        return f'{str(self.order_date)} - {self.pk}'