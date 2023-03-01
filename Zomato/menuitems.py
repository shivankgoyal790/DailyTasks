class Menuitems:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def display_menuitem(self):
        self.item.display_item()
        print(self.price)
