from django.contrib import admin
from django.db.models import F

from .models import Supplier, Ingredient, Dish, Category, Order


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['diff', 'name', 'current_volume', 'min_av_volume', 'cost_per_1_kg', 'supplier']

    def get_queryset(self, request):
        qs = super(IngredientAdmin, self).get_queryset(request)
        qs = qs.annotate(diff = F('current_volume') - F('min_av_volume'))
        return qs
    
    def diff(self, obj):
        return obj.diff
    

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'descritpion', 'get_ing', 'weight', 'price']
    
    def get_ing(self, obj):
        return len(obj.ingredients.all())
    
    get_ing.short_description = 'Ingredients num'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_dish', 'last_time_changed', 'display_priority']
    
    def get_dish(self, obj):
        return len(obj.dishes.all())
    
    get_dish.short_description = 'Dishes num'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'order_place', 'executor', 'get_dishes', 'get_order_status']