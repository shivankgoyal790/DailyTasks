class Menu:
    def __init__(self, id, rest_id):
        self.id = id
        self.menuitemlist = []
        self.rest_id = rest_id

    def display_allitems(self):
        print(self.id)
        for item in self.menuitemlist:
            print(item.item.display_item())
            print(item.price)
