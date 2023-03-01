from menu import Menu
from item import Item
from menuitems import Menuitems
from restaurant import Restaurant
import pytest
from io import StringIO


@pytest.fixture()
def setup():
    mymenu = Menu("123", "456")
    return mymenu


@pytest.fixture()
def setup1():
    rest = Restaurant("123", "Sagar Ratna", "GTBNagar")
    return rest


def test_can_create_obj():
    rest = Restaurant("123", "Sagar Ratna", "GTBNagar")


def test_can_create_menu():
    mymenu = Menu("123", "456")


def test_can_add_item_in_menu(setup):
    item = Item(1, "Shahi Paneer", 5)
    newitem = Menuitems(item, 100)
    setup.menuitemlist.append(newitem)


def test_can_remove_item(setup1, monkeypatch):
    number_inputs = StringIO('Shahi Paneer\n')
    monkeypatch.setattr('sys.stdin', number_inputs)
    setup1.create_menu("1234")
    setup1.deleteitem_from_menu()


def test_checklist_of_orders(setup1):
    setup1.check_orders()


def test_can_update_status(setup1):
    setup1.update_status()
