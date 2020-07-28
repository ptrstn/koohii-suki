import pytest

from koohii.login import bugmenot_login_to_kanjii_koohi, login_to_kanji_koohii


def test_bugmenot_login_to_kanjii_koohi():
    with pytest.raises(Exception):
        bugmenot_login_to_kanjii_koohi("kanshudo.com")
    assert bugmenot_login_to_kanjii_koohi()


def test_login_to_kanji_koohii():
    with pytest.raises(ValueError):
        login_to_kanji_koohii("Bobby", "Tales")
