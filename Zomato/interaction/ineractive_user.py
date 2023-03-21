from colorama import Back, Style


def user_choice_interaction():
    print("\n\n")
    print(Back.RED)
    print("ENTER 1 TO SELECT ANY RESTAURANT")
    print("ENTER 2 TO CHECK YOUR CART")
    print("ENTER 3 TO REMOVE ITEM FROM CART")
    print("ENTER 4 TO PLACE YOUR ORDER")
    print("ENTER 5 TO CHECK YOUR ORDERS")
    print("ENTER 6 TO RATE A RESTAURANT")
    print("ENTER 7 TO RATE ANY ITEM")
    print("ENTER 8 TO EXIT OR LOGOUT")
    print(Style.RESET_ALL)


def user_choice_interaction2():
    print("\n\n")
    print(Back.RED)
    print("ENTER 1 to add any item to cart ")
    print("ENTER 2 to remove item from cart ")
    print("ENTER 3 to place your order ")
    print("ENTER 4 to select another restaurant ")
    print(Style.RESET_ALL)


def remove_from_cart(user):
    if (len(user.foodlist) == 0):
        print(Back.YELLOW)
        print("\nNothing to Remove Your Cart is Empty")
        print(Style.RESET_ALL)
    else:
        index = 0
        while (index == 0):
            index = int(input(
                "\n\nEnter the valid of the item you want to remove "))

        user.remove_fromcart(index)
        user.check_cart()


def update_cart(user, rest):
    if (user.curr_rest != rest.rest_id):
        user.curr_rest = rest.rest_id
        user.foodlist = []

    menuitem = 0
    while (menuitem == 0):
        index = int(input(
            "\nEnter the valid index of the item you want to Add "))
        menuitem = rest.find_item(index)

        if (menuitem):
            user.update_cart(menuitem)
            user.check_cart()


def place_order(user, z, rest):
    if (len(user.foodlist) == 0):
        print(Back.YELLOW)
        print("YOUR CART IS EMPTY PLEASE ADD SOMETHING TO CONTINUE")
        print(Style.RESET_ALL)
    else:
        agent = z.assign_delivery()
        agent.update_status()
        z.place_order(user, rest, agent)
        print("\n WANT TO RATE THE CURRENT RESTAURANT ?")
        print("ENTER Y/y TO CONTINUE OR N/n TO RETURN TO HOMEPAGE")
        mych = input("ENTER CHOICE")
        if (mych == 'Y' or mych == 'y'):
            rate = int(input("ENTER THE RATING BETWEEN 0-5 "))
            while (rate < 0 or rate > 5):
                rate = int(input("ENTER A VALID RATING BETWEEN 0-5 "))
            rest = user.curr_rest
            z.rate_current_rest(rest, rate)


def user_interactive_display(user, z):

    ch = '0'
    while (ch != "8"):
        print("\nHELLO!! HERE IS THE LIST OF RESTRAUNTS CURRENTLY ACCEPTING ORDERS")
        z.display_restaurants()

        user_choice_interaction()
        ch = input("ENTER CHOICE ")

        if (ch == "1"):

            index = int(input(
                "\nENTER THE INDEX TO CHECK MENU OF THAT RESTAUTANT "))
            rest = z.find_restaurant(index)

            mychoice = "1"
            while (mychoice != "4"):

                if (rest):
                    print("\n\nCheck Our Menu")
                    rest.show_menu()
                user_choice_interaction2()
                mychoice = input()

                if (mychoice == "1"):
                    update_cart(user, rest)

                elif (mychoice == '2'):
                    remove_from_cart(user)

                elif (mychoice == "3"):
                    place_order(user, z, rest)

        elif (ch == '2'):
            if (user):
                user.check_cart()

        elif (ch == "3"):
            remove_from_cart(user)

        elif (ch == "4"):
            if (len(user.foodlist) == 0):
                print(Back.YELLOW)
                print("YOUR CART IS EMPTY PLEASE ADD SOMETHING TO CONTINUE")
                print(Style.RESET_ALL)
            else:
                place_order(user, z, rest)

        elif (ch == "5"):
            user.check_order()

        elif (ch == "6"):
            index = int(input("ENTER THE INDEX OF RESTAURANT TO RATE "))
            rate = int(input("ENTER THE RATING BETWEEN 0-5 "))
            while (rate < 0 or rate > 5):
                rate = int(input("ENTER THE RATING BETWEEN 0-5 "))
            z.update_rest_rating(index, rate)

        elif (ch == "7"):
            z.display_all_items()
            index = int(input("ENTER THE INDEX OF ITEM TO RATE "))
            rate = int(input("ENTER THE RATING BETWEEN 0-5 "))
            while (rate < 0 or rate > 5):
                rate = int(input("ENTER THE RATING BETWEEN 0-5 "))
            z.update_item_rating(index, rate)
