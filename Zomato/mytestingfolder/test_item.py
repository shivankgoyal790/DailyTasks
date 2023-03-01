from item import Item


def test_cancreateobject():
    item = Item('1', "dosa", 5)
    print(item)


def test_candisplayitem():
    item = Item('1', "dosa", 5)
    item.display_item()
