from koohii.kanji import get_kanji_word_list


def test_get_kanjii_word_list():
    kanji_word_list = get_kanji_word_list()
    first_word = kanji_word_list[0]
    assert first_word
    assert "definition" in first_word
    assert "kanji" in first_word
    assert first_word["kanji"] == "一"
    assert first_word["definition"] == "one"
    assert len(kanji_word_list) >= 3000
