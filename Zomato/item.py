class Item:
    def __init__(self, id, name, rating):
        self.id = id
        self.name = name
        self.rating = rating

    def display_item(self):
        print(self.id, self.name, self.rating)
