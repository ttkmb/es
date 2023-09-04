import pytest
from src.phone import Phone
from src.item import Item


def test_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2


def test_phone_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    try:
        phone1.number_of_sim = 0
    except ValueError:
        assert True
    else:
        assert False, "Ожидалось, что будет возбуждено исключение ValueError"

def test_add_function():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item('Телефон', 16000, 50)
    assert phone1 + item1 == 55
    with pytest.raises(TypeError):
        assert phone1 + 50000 is None


def test_number_of_SIM():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    with pytest.raises(ValueError, match='Количество физических SIM-карт должно быть целым числом больше нуля'):
        phone1.number_of_sim = 0