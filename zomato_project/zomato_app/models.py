class Dish:
    def __init__(self, dish_id, dish_name, price, availability):
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.price = price
        self.availability = availability

class Order:
    order_id_counter = 1
    
    def __init__(self, customer_name, dish_ids):
        self.order_id = Order.order_id_counter
        Order.order_id_counter += 1
        self.customer_name = customer_name
        self.status = 'received'
        self.dish_ids = dish_ids
