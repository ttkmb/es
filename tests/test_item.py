"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

def test_item():
    some_item = Item('тест', 15000, 5)
    assert some_item.calculate_total_price() == 75000

def test_discount():
    smartphone = Item('Samsung', 40000, 60)
    assert smartphone.apply_discount() == smartphone.price
