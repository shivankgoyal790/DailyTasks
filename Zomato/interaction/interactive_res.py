from colorama import Back, Style


def res_interactive(res, z):
    ch = '0'
    while (ch != "6"):

        print("\n CHECK OUR MENU")
        res.display_rest()
        print("\n")
        res.show_menu()
        print("\n\n\n")
        print(Back.RED)
        print("\nENTER 1 TO ADD A NEW ITEM IN MENU")
        print("ENTER 2 TO CHECK ORDERS")
        print("ENTER 3 TO ADD ALREADY CREATED RECIPE")
        print("ENTER 4 TO UPDATE YOUR STATUS")
        print("ENTER 5 TO DELETE ITEM FROM MENU")
        print("ENTER 6 TO EXIT")
        ch = input("ENTER CHOICE ")
        print(Style.RESET_ALL)
        if (ch == "1"):
            menuitem = res.create_new_menuitem()
            z.list_of_items.append(menuitem)

        elif (ch == "2"):
            res.check_orders()

        elif (ch == "3"):

            z.display_all_items()
            index = int(input("\nENTER THE INDEX OF THE ITEM TO ADD"))
            item = 0
            while (item == 0):
                item = z.find_item(index)
            price = int(input("\nENTER THE PRICE OF ITEM "))
            res.add_item_from_existing_list(item, price)

        elif (ch == "4"):
            res.update_status()

        elif (ch == "5"):
            x = res.deleteitem_from_menu()
            if (x):
                print("\nITEM DELETED FROM MENU")
