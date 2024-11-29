from words_to_int import parse_int


def test_input():
    """Проверяем соответствие выходных данных функции parse_int и ответа"""

    assert parse_int('seven hundred thousand') == 700_000
    assert parse_int('six hundred sixty-six thousand six hundred sixty-six') == 666_666
    assert parse_int('one million fifteen thousand forty-eight') == 1_015_048
    assert parse_int('one million') == 1_000_000
    assert parse_int('one million one') == 1_000_001
    assert parse_int('one') == 1
