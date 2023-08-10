from django.shortcuts import render, redirect
from .models import Dish, Order

dishes = [ {'dish_id': 1, 'dish_name': 'Margherita Pizza', 'price': 10.99, 'availability': True},
    {'dish_id': 2, 'dish_name': 'Chicken Tikka Masala', 'price': 12.99, 'availability': True},
    {'dish_id': 3, 'dish_name': 'Pasta Alfredo', 'price': 9.99, 'availability': False},
    {'dish_id': 4, 'dish_name': 'Chocolate Brownie', 'price': 5.99, 'availability': True},]

def get_dish_by_id(dish_id):
    for dish in dishes:
        if dish.dish_id == dish_id:
            return dish
    return None

def menu(request):
    return render(request, 'menu.html', {'dishes': dishes})

def add_dish(request):
    if request.method == 'POST':
        dish_name = request.POST.get('dish_name')
        price = float(request.POST.get('price'))
        availability = request.POST.get('availability') == 'yes'
        dish_id = len(dishes) + 1
        dish = Dish(dish_id, dish_name, price, availability)
        dishes.append(dish)
        return redirect('menu')
    return render(request, 'add_dish.html')

def take_order(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        dish_ids = [int(dish_id) for dish_id in request.POST.getlist('dish_ids')]
        order = Order(customer_name, dish_ids)
        return redirect('menu')
    return render(request, 'take_order.html', {'dishes': dishes})

def update_order_status(request):
    if request.method == 'POST':
        order_id = int(request.POST.get('order_id'))
        new_status = request.POST.get('new_status')
        # Update order status, etc.
        return redirect('menu')
    return render(request, 'update_order_status.html')
