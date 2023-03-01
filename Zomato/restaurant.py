from menu import Menu
from item import Item
from menuitems import Menuitems


class Restaurant:

    def __init__(self, id, name, address):
        self.rest_id = id
        self.name = name
        self.address = address
        self.status = "open"
        self.rating = 5
        self.curr_orders = []

    def create_menu(self, id):
        mymenu = Menu(id, self.rest_id)
        self.menu = mymenu

    def create_new_menuitem(self):
        item = Item(1, "Shahi Paneer", 5)
        price = int(input("enter the price of the dish"))
        newitem = Menuitems(item, price)
        self.menu.menuitemlist.append(newitem)

    def add_item_from_existing_list(self, item, price):
        newitem = Menuitems(item, price)
        self.menu.menuitemlist.append(newitem)

    def deleteitem_from_menu(self):
        dish = input("Enter the name of dish to delete")
        filter(lambda x: x.item.name != dish, self.menu.menuitemlist)

    def update_status(self):
        if (self.status == "open"):
            self.status = "closed"
        else:
            self.status = "open"

    def check_orders(self):
        for i in self.curr_orders:
            print(i)
