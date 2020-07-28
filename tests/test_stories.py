from koohii.login import bugmenot_login_to_kanjii_koohi
from koohii.stories import get_kanji_stories


def test_get_kanji_stories():
    number_of_stories = 10
    kanji_character = "五"

    koohii_session = bugmenot_login_to_kanjii_koohi()
    stories = get_kanji_stories(
        koohii_session=koohii_session,
        kanji_character=kanji_character,
        number_of_stories=number_of_stories,
    )

    assert len(stories) == number_of_stories
    assert "story" in stories[0]
    assert "stars" in stories[0]
    assert "reports" in stories[0]
    assert stories[0].get("story")
    assert stories[0].get("stars") >= 0
    assert stories[0].get("reports") >= 0
