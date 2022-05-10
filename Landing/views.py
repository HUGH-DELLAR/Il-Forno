from django.shortcuts import render, HttpResponse
from Administration.models import Category, Dish

# Create your views here.
def index(request):
    return render(request, 'index.html')

def menu(request):
    print([i for i in Category.objects.all()])
    return render(request, 'menu.html', {'categories': Category.objects.all(), 'dishes': Dish.objects.all()})

def cart(request):
    cart = request.session['cart']
    cart = [Dish.objects.get(pk=id) for id in cart]
    return render(request, 'cart.html', {'cart': cart})

def add_product(request, id):
    session = request.session
    try:
        session['cart'].append(id)
    except:
        session['cart'] = [id]
    return HttpResponse('<script type="text/javascript">window.close()</script>')  