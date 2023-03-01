from order import Order


class User:
    def __init__(self, id, name, address, phone, email):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.curr_rest = ""
        self.foodlist = []

    def update_cart(self, menuitem):
        self.foodlist.append(menuitem)

    def remove_fromcart(self, recipe):
        filter(lambda x: x.item.name != recipe, self.foodlist)

    def check_cart(self):
        for i in self.foodlist:
            print(i)

    def update_info(self):
        self.name = input("Enter new Name")
        self.address = input("enter the new address")
        self.phone = input("enter new Phone")
        self.email = input("enter new email")

    def place_order(self, rest_id):
        totalprice = 0
        for item in self.foodlist:
            totalprice += item.price
        order = Order(self.id, rest_id, "1234", "2356",
                      self.foodlist, totalprice)
        order.show_order()
