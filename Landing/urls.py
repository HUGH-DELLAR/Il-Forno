from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('menu/', views.menu),
    path('cart/', views.cart),
    path('add/<int:id>/', views.add_product),
    path('remove/<int:id>/', views.remove_product),
    path('new_order/', views.new_order),
    path('reservation/', views.reservation),
]