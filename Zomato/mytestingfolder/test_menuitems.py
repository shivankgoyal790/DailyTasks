from menuitems import Menuitems
from item import Item


def test_can_create_obj():
    item = Item("1", "Dosa", 2)
    Menuitem = Menuitems(item, 100)
    assert True


def test_candisplayitem():
    item = Item("1", "Dosa", 2)
    Menuitem = Menuitems(item, 100)
    Menuitem.display_menuitem()
    assert True
