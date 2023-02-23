# Method voilating the dependency inversion principle
#which states that high level and low level modules should only depend on abstraction and not bewteen themselves

# class Paymentprocessor():
#     def __init__(self):
#         self.payment_gateway = Paymentgateway()
#     def calc_payment(self,amount):
#         self.payment_gateway.calc_payment(amount)


# class Paymentgateway():
#     def __init__(self):
#         pass
#     def calc_payment(self,amount):
#         print(amount*100)


# p = Paymentprocessor()
# p.calc_payment(100)




# method 2 preventing voilation of DIP

class Paymentprocessor():
    def __init__(self,payment_obj):
        self.payment_gateway = payment_obj
    def calc_payment(self,amount):
        self.payment_gateway.calc_payment(amount)

class Payment():
        def calc_payment(self,amount):
            pass

class Paymentgateway(Payment):
    def __init__(self):
        pass
    def calc_payment(self,amount):  
        print(amount*100)



p1 = Paymentgateway()
p = Paymentprocessor(p1)
p.calc_payment(100)
