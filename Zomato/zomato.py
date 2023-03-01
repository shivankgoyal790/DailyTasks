# Service class
from registration import Registration


class Zomato:
    def __init__(self):
        self.list_of_orders = []
        self.list_of_restaurant = []
        self.list_of_users = []
        self.list_of_delivery_boy = []

    def Register(self, type):
        if (type == 'customer'):
            pass
        elif (type == "restuarnt"):
            pass
        elif (type == "deliverboy"):
            pass

    def display_restaurants(self):
        pass

    def authenticate_user(self):
        pass

    def check_orders(self):
        pass

    def update_listoforders(self):
        pass
