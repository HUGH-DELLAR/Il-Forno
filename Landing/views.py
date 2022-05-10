from django.shortcuts import render
from Administration.models import Category, Dish

# Create your views here.
def index(request):
    return render(request, 'index.html')

def menu(request):
    print([i for i in Category.objects.all()])
    return render(request, 'menu.html', {'categories': Category.objects.all(), 'dishes': Dish.objects.all()})