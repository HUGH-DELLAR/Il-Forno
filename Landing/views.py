from django.shortcuts import render, HttpResponse
from Administration.models import Category, Dish, Order, Ingredient
import datetime
from .forms import ReservationForm
from .models import Reservation

# Create your views here.
def index(request):
    chef = ['Филе дорадо', 'Пицца Четыре сезона на ржаном тесте', 'Фасолевый суп с крупой фаро (пост)', 'Пицца Хенрико на ржаном тесте', 'Серый хлеб с гриссини и сливочным маслом', 'Фиш энд чипс', 'Лазанья Болоньезе', 'Цыпленок Пиканте с брокколи на гриле', 'Чизкейк с лесными ягодами', 'Пицца с морепродуктами на ржаном тесте', 'Пицца с лососем на ржаном тесте', 'Пицца Руккола с креветками на ржаном тесте']
    dish_obj = [Dish.objects.get(name=i) for i in chef]
    session = request.session
    session['cart'] = {}
    request.session.modified = True
    return render(request, 'index.html', {'chef': dish_obj, 
                                          'nums1_9':[i for i in range(1,10)],
                                          'nums1_8':[i for i in range(1,9)]})

def menu(request):
    print([i for i in Category.objects.all().order_by('display_priority')])
    return render(request, 'menu.html', {'categories': Category.objects.all().order_by('display_priority'), 
                                         'categories_r': Category.objects.all().order_by('-display_priority'),
                                         'dishes': Dish.objects.all()})

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

def new_order(request):
    session = request.session
    cart = session['cart']
    order = Order(
        order_date=datetime.datetime.now(),
        order_place='Delivery',
        dishes=cart,
        order_status=0,
    )
    order.save()
    for dish, amount in cart.items():
        dish_obj = Dish.objects.get(pk=dish)
        for _ in range(amount):
            all_ings = dish_obj.ingredients.all()
            av = dish_obj.weight / (len(all_ings))
            for ing in all_ings:
                ing.current_volume -= av
                ing.save()
    return render(request, 'done.html', {'order_id': order.pk})

def reservation(request):
    form = ReservationForm(request.POST)
    print(form)
    print(form.cleaned_data)
    data = form.cleaned_data
    reserv_obj = Reservation(name=data['name'],
                             phone=data['phone'],
                             customer_num=data['customer_num'],
                             reservation_date=data['reservation_date'],
                             reservation_time=data['reservation_time'])
    reserv_obj.save()
    return HttpResponse('<script type="text/javascript">window.location.href = "/"</script>')
