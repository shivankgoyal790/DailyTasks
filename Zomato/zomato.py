# Service class
from registration import CreateDeliveryBoy
from registration import CreateUser
from registration import CreateRestaurant
import random
from colorama import Back, Style
from order import Order


class Zomato:
    def __init__(self):

        self.list_of_orders = []
        self.list_of_restaurant = []
        self.list_of_users = []
        self.list_of_items = []
        self.list_of_delivery_boy = []

    def register(self, type):

        if (type == 'customer'):
            user = CreateUser()
            myuser = user.Register()
            self.list_of_users.append(myuser)
        elif (type == "restaurant"):
            res = CreateRestaurant()
            myrest = res.Register()
            self.list_of_restaurant.append(myrest)
        elif (type == "deliverboy"):
            agent = CreateDeliveryBoy()
            myagent = agent.Register()
            self.list_of_delivery_boy.append(myagent)

    def display_restaurants(self):

        for i in self.list_of_restaurant:

            if (i.status == 'open'):
                print(self.list_of_restaurant.index(i) + 1, end="  ")
                i.display_rest()

    def authenticate(self, email, password):
        for i in self.list_of_delivery_boy:
            if (i.email == email and i.password == password):
                return i
        for i in self.list_of_restaurant:
            if (i.email == email and i.password == password):
                return i
        for i in self.list_of_users:
            if (i.email == email and i.password == password):
                return i
        return 0

    def check_orders(self):

        for i in self.list_of_orders:
            i.show_order()

    def assign_delivery(self):
        return random.choice(self.list_of_delivery_boy)

    def update_listoforders(self, order):
        self.list_of_orders.append(order)

    def find_restaurant(self, index):

        if (index > len(self.list_of_restaurant)):
            return 0
        return self.list_of_restaurant[index-1]

    def place_order(self, user, rest, agent):
        print("\nOrder Placed")
        totalprice = 0
        for item in user.foodlist:
            totalprice += item.price
        order = Order(random.randint(6000, 7000),
                      user, rest, agent, totalprice)
        order.show_order()
        user.curr_orders.append(order)
        self.list_of_orders.append(order)
        rest.curr_orders.append(order)
        agent.myorders.append(order)
        user.foodlist = []

    def find_item(self, index):
        if (index > len(self.list_of_items)):
            return 0
        return self.list_of_items[index - 1].item

    def display_all_items(self):
        for i in self.list_of_items:
            print(self.list_of_items.index(i) + 1, end=" ")
            i.display_menuitem()

    def update_rest_rating(self, index, rate):
        while (index > len(self.list_of_restaurant)):
            index = int(input("ENTER A VALID INDEX AGAIN"))
        rest = self.list_of_restaurant[index - 1]
        avg = (rest.rating*(rest.no_of_ratings) + rate) / \
            (rest.no_of_ratings + 1)
        rest.no_of_ratings += 1
        rest.rating = avg
        print(Back.YELLOW)
        print("\nRATING UPDATED")
        print(Style.RESET_ALL)

    def update_item_rating(self, index, rate):
        while (index > len(self.list_of_items)):
            index = int(input("ENTER A VALID INDEX AGAIN"))
        item = self.list_of_items[index - 1]
        avg = (item.rating*(item.no_of_ratings) + rate) / \
            (item.no_of_ratings + 1)
        item.no_of_ratings += 1
        item.rating = avg
        print(Back.YELLOW)
        print("\nRATING UPDATED")
        print(Style.RESET_ALL)

    def rate_current_rest(self, rest, rate):
        res = 0
        for i in self.list_of_restaurant:
            if i.rest_id == rest:
                res = i
                break

        avg = (res.rating*(res.no_of_ratings) + rate) / \
            (res.no_of_ratings + 1)
        res.no_of_ratings += 1
        res.rating = avg
        print(Back.YELLOW)
        print("\nRATING UPDATED")
        print(Style.RESET_ALL)
