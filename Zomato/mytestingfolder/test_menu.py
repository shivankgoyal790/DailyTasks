from menu import Menu


def test_can_create_obj():
    menu = Menu("123", "456")


def test_can_display_allitems():
    menu = Menu("123", "456")
    menu.display_allitems()
