import pytest
from string_utils import StringUtils

string_ut = StringUtils()

'''
Для каждой функции  написаны тесты.
Тесты параметризованы.
'''

# 4 теста для функции capitilize - первую букву предложения делает заглавной
@pytest.mark.parametrize('string, result', [('skypro', 'Skypro'),
                                            ('Skypro', 'Skypro'),
                                            ('Skypro23', 'Skypro23'),
                                            ("The best music is rock", "The best music is rock")])
def test_capitilize(string, result):   # объявляем тест
    string_ut = StringUtils()          # создаем экземпляр класса
    res = string_ut.capitilize(string) # применяем функцию к передаваемому значениею (string)  и сохранем полученный результат в res
    assert res == result               # сравниваем фактический результат (res) и ожидаемый(result)


@pytest.mark.parametrize('string, result', [(' skypro', 'skypro'),
                                            (' Skypro', 'Skypro'),
                                            (' Skypro23', 'Skypro23'),
                                            (' skypro skypro', 'skypro skypro'),
                                            ('skypro', 'skypro'),
                                            ("     ", ""),
                                            ("  The best music is rock  ", "The best music is rock  ")])
def test_trim(string, result):
    string_ut = StringUtils()
    res = string_ut.trim(string)
    assert res == result


@pytest.mark.parametrize('string, delimeter, result', [('s,k,y,p,r,o', ',', ["s", "k", "y", "p", "r", "o"]),
                                                       ("1:2:3", ':', ["1", "2", "3"]),
                                                       ('', ', ', [])])
def test_list_delimeter(string, delimeter, result):
    string_ut = StringUtils()
    res = string_ut.to_list(string, delimeter)
    assert res == result


def test_default_to_list():
    string_ut = StringUtils()
    res = string_ut.to_list("12345,12345,12345")
    assert res == ["12345", "12345", "12345"]


@pytest.mark.parametrize('string, symbol, result', [('skypro', 's', True),
                                                    ('skypro', 'z', False),
                                                    ("The best music is rock", "e", True),
                                                    "The best music is rock", " ", True)])
def test_contain_is(string, symbol, result):
    string_ut = StringUtils()
    res = string_ut.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [('skypro', 's', 'kypro'),
                                                    ('skypro', '', 'skypro'),
                                                    ("The best music is rock", " ", "Thebestmusicisrock")])
def test_delete_symbol(string, symbol, result):
    string_ut = StringUtils()
    res = string_ut.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [('skypro', 's', True),
                                                    ("The best music is rock", "T", True),
                                                    (" The best music is rock ", " The", True),
                                                    (' skypro', ' ', True)])
def test_starts_with_true(string, symbol, result):
    string_ut = StringUtils()
    res = string_ut.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, symbol, result', [('skypro', 'o', True),
                                                    ("The best music is rock", "The best music is rock", True),
                                                    (" The best music is rock ", " ", True),
                                                    ('skypro ', ' ', True)])
def test_end_with_true(string, symbol, result):
    string_ut = StringUtils()
    res = string_ut.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize('string, result',[('skypro', False),
                                           ('', True),
                                           ('  ', True),
                                           (" The best music is rock ", False)])
def test_is_empty(string, result):
    string_ut = StringUtils()
    res = string_ut.is_empty(string)
    assert res == result


@pytest.mark.parametrize('string, joiner, result', [([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
                                                    (["Sky", "Pro"], ", ", "Sky, Pro"),
                                                    (["Sky", "Pro"], "-", "Sky-Pro"), (["1"], "*", "1"),
                                                    ([""], "+", "")])
def test_list_to_string(string, joiner, result):
    string_ut = StringUtils()
    res = string_ut.list_to_string(string, joiner)
    assert res == result


def test_vot_list_to_string():
    string_ut = StringUtils()
    res = string_ut.list_to_string(["Скайпро", "ну", "вот", "тут", "домашка"])
    assert res == "Скайпро, ну, вот, тут, домашка"


def test_vot2_list_to_string():
    string_ut = StringUtils()
    res = string_ut.list_to_string(["1"])
    assert res == "1"