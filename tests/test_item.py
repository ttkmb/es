"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

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

