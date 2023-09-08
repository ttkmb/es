from src.keyboard import Keyboard


def test_keyboard_func():
    kb = Keyboard('Logitech G pro X', 13000, 10)
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang().change_lang()
    assert kb.language == "RU"
    kb.change_lang().change_lang().change_lang()
    assert kb.language == "EN"


def test_str_keyboard():
    kb = Keyboard('Logitech G pro X', 13000, 10)
    assert str(kb.name) == 'Logitech G pro X'
