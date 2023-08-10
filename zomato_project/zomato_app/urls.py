from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('take_order/', views.take_order, name='take_order'),
    path('update_order_status/', views.update_order_status, name='update_order_status'),
]
