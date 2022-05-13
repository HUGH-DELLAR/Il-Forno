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
    print(cart)
    n_cart = [[Dish.objects.get(pk=int(id)), value] for id, value in cart.items()]
    sum_total = sum([int(id.price * value) for id, value in n_cart])
    return render(request, 'cart.html', {'cart': n_cart, 'sum_total': sum_total})

def add_product(request, id):
    session = request.session
    try:
        session['cart'][str(id)] += 1
    except Exception as ex:
        try:
            session['cart'][str(id)] = 1
        except Exception as ex:
            session['cart'] = {str(id): 1}
    finally:
        request.session.modified = True
    print(session['cart'])
    return HttpResponse('<script type="text/javascript">window.close()</script>')  

def remove_product(request, id):
    session = request.session
    del session['cart'][str(id)]
    request.session.modified = True
    print(session['cart'])
    return HttpResponse('<script type="text/javascript">window.location.href = "/cart"</script>')