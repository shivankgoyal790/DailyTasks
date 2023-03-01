class Order:
    def __init__(self, id, restid, customerid, delivery_boy_id, price, foodlist):
        self.id = id
        self.restid = restid
        self.customerid = customerid
        self.delivery_boy_id = delivery_boy_id
        self.itemlist = foodlist
        self.totalpayment = price
        self.status = "not delivered"

    def show_order(self):
        pass
