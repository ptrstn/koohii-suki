from bs4 import BeautifulSoup

from koohii.settings import REQUEST_HEADERS
from koohii.utils import to_unicode_decimal, to_integer

STORIES_URL = "https://kanji.koohii.com/study/SharedStoriesList"


def get_kanji_stories(koohii_session, kanji_character, number_of_stories=10):
    ucs_id = to_unicode_decimal(kanji_character)

    stories_data = {
        "ucsId": str(ucs_id),
        "rows": str(number_of_stories),
    }

    stories_response = koohii_session.post(
        STORIES_URL, headers=REQUEST_HEADERS, data=stories_data
    )
    stories_json = stories_response.json()
    assert "errors" not in stories_json, stories_json.get("errors")

    stories_html = stories_json.get("html")
    soup = BeautifulSoup(stories_html, "html.parser")
    story_divs = soup.findAll("div", {"class": "sharedstory"})

    return [
        {
            "kanji": kanji_character,
            "story": story_div.find("div", {"class": "story"}).text,
            "stars": to_integer(story_div.find("a", {"class": "JsStar"}).text),
            "reports": to_integer(story_div.find("a", {"class": "JsReport"}).text),
        }
        for story_div in story_divs
    ]
