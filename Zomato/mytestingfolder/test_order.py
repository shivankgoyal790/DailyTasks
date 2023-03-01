from order import Order


def test_createobj():
    order = Order('113', "123", "1234", "2356",
                  [], 100)


def test_showobj():
    order = Order('113', "123", "1234", "2356",
                  [], 100)
    order.show_order()
