from koohii.utils import to_unicode_decimal, to_integer


def test_to_unicode_decimal():
    assert to_unicode_decimal("五") == 20116


def test_to_integer():
    assert to_integer("5") == 5
    assert to_integer("") == 0
    assert to_integer("-1") == -1
