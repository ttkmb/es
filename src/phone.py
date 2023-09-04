from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        elif isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError('Складывать можно только с экземплярами `Phone` или `Item`классов')

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_value):
        if int(new_value) > 0:
            self.__number_of_sim = new_value
        raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
