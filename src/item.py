import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __str__(self):
        return (f'{self.__name}\n'
                f'Цена {self.price}\n'
                f'Кол-во {self.quantity}\n'
                f'---------------')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name

        else:
            self.__name = new_name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls, path):
        items = []
        cls.all.clear()
        with open(path, 'r', newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)
                items.append(item)
        return items

    @staticmethod
    def string_to_number(str):
        if '.' in str:
            str_float = float(str)
            str_int = int(str_float)
        else:
            str_int = int(str)
        return str_int

