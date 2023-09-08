from src.item import Item

class MixinKeyboard:
    def __init__(self, name, price, quantity, lang='EN'):
        super().__init__(name, price, quantity)
        self.__lang = lang

    def change_lang(self):
        if self.__lang == 'EN':
            self.__lang = 'RU'
        elif self.__lang == 'RU':
            self.__lang = 'EN'
        return self

    @property
    def language(self):
        return self.__lang



class Keyboard(MixinKeyboard, Item):
    def __str__(self):
        return f'{self.name}'


