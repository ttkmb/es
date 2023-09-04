"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone

def test_item():
    some_item = Item('тест', 15000, 5)
    assert some_item.calculate_total_price() == 75000

def test_discount():
    smartphone = Item('Samsung', 40000, 60)
    assert smartphone.apply_discount() == smartphone.price

def test_csv():
    some_item = Item('тест', 15000, 5)
    some_item.instantiate_from_csv('/Users/ttkmb/WORKHARD/V2.0/electronic_shop/src/items.csv')
    assert len(Item.all) == 5

def test_str():
    some_item = Item('тест', 15000, 5)
    assert some_item.string_to_number('67.45') == 67

def test_len_name():
    some_item = Item('12345678910111213', 15000, 5)
    with pytest.raises(AssertionError):
        assert some_item.name == '1234567891'

def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'

def test_add_function():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item('Телефон', 16000, 50)
    assert phone1 + item1 == 55
    with pytest.raises(TypeError):
        assert phone1 + 50000 is None