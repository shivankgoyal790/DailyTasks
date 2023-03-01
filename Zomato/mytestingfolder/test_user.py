from user import User
from menuitems import Menuitems
from item import Item
import pytest


@pytest.fixture()
def setup():
    user = User("1221", "shivank", "sector 134",
                "7906558590", "goyal@gmail.com")
    return user


def test_can_createobj():
    user = User("1221", "shivank", "sector 134",
                "7906558590", "goyal@gmail.com")


def test_can_updatecart(setup):
    item = Item("124", "pasta", 2)
    menuitem = Menuitems(item, 100)
    setup.update_cart(menuitem)


def test_checkcart(setup):
    setup.check_cart()


def test_removefromcart(setup):
    item = Item("124", "pasta", 2)
    menuitem = Menuitems(item, 100)
    setup.remove_fromcart(menuitem)


def test_place_order(setup):
    item = Item("124", "pasta", 2)
    menuitem = Menuitems(item, 100)
    setup.update_cart(menuitem)
    setup.place_order("456")
