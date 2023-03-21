from zomato import Zomato
from restaurant import Restaurant
from user import User
from delivery_boy import Deliveryboy
from interaction.ineractive_user import user_interactive_display
from interaction.interactive_res import res_interactive
from interaction.interactive_delivery_boy import delivery_interactive
from helper.emailchecker import validemailcheck
from helper.password_checker import password_checker
import random
from colorama import Back, Style, Fore

print(Style.RESET_ALL)
z = Zomato()

newrest = Restaurant("201", "Mc Donalds", "sector 142",
                     "mcd@gmail.com", "12345678")
newrest.create_menu()
menuitem1 = newrest.create_new_menuitem()
menuitem2 = newrest.create_new_menuitem()
z.list_of_items.append(menuitem1)
z.list_of_items.append(menuitem2)

z.list_of_restaurant.append(newrest)

deliveragent1 = Deliveryboy(random.randint(
    5000, 6000), "sam", "9897653285", "sam@gmail.com", "12345678")
deliveragent2 = Deliveryboy(random.randint(
    5000, 6000), "rakesh", "9897653285", "rakesh@gmail.com", "12345678")

z.list_of_delivery_boy.append(deliveragent1)
z.list_of_delivery_boy.append(deliveragent2)


def main():

    ch = '0'

    while (ch != '9'):
        print("\n")
        print("\n\nWELCOME TO SASTA ZOMATO")
        print("\n")
        z.display_restaurants()
        print(Back.RED)
        print("\nENTER 1 TO LOGIN")
        print("ENTER 2 TO SIGN UP\n\n")
        choice = input("ENTER CHOICE ")
        print(Style.RESET_ALL)

        if (choice == '1'):

            email = validemailcheck()
            password = password_checker()

            ch = "1"
            while (ch != "2"):

                entity = z.authenticate(email, password)

                if (isinstance(entity, Restaurant)):
                    ch = "2"
                    res_interactive(entity, z)
                elif (isinstance(entity, User)):
                    ch = "2"
                    user_interactive_display(entity, z)
                elif (isinstance(entity, Deliveryboy)):
                    ch = "2"
                    delivery_interactive(entity, z)
                else:
                    print(Back.YELLOW+Fore.BLACK)
                    print("\nINVALID LOGIN CREDENTIALS\n")
                    print(Style.RESET_ALL)
                    break
        else:

            print("IF YOU ARE A USER SELECT 1 ")
            print("IF YOU ARE A RESTAURANT SELECT 2 ")
            choice = input()

            if (choice == '1'):
                user = z.register("customer")
            else:
                user = z.register("restaurant")


main()
