import abc
from user import User
from delivery_boy import Deliveryboy
from restaurant import Restaurant
import random
from helper.emailchecker import validemailcheck
from helper.password_checker import password_checker
from helper.phonechecker import phonechecker


class Registration():
    @abc.abstractmethod
    def Register(self):
        pass


class CreateRestaurant(Registration):

    def Register(self):

        id = random.randint(3000, 4000)
        name = input("Enter Your Restaurant Name ")
        address = input("Enter Your Address ")
        email = validemailcheck()
        password = password_checker()
        res = Restaurant(id, name, address, email, password)
        res.create_menu()
        return res


class CreateDeliveryBoy(Registration):

    def Register(self):

        id = random.randint(5000, 6000)
        name = input("ENTER NAME OF AGENT ")
        phone = phonechecker()
        email = validemailcheck()
        password = password_checker()
        agent = Deliveryboy(id, name, phone, email, password)

        return agent


class CreateUser(Registration):

    def Register(self):

        id = random.randint(4000, 5000)
        name = input("ENTER YOUR NAME ")
        address = input("ENTER YOUR ADDRESS ")
        phone = phonechecker()
        email = validemailcheck()
        password = password_checker()
        user = User(id, name, address, phone, email, password)

        print("\nYOU ARE SUCCESSFULLY REGISTERED\n")

        return user
