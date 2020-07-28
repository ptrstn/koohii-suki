import json
import re

import requests

from koohii.settings import REQUEST_HEADERS

KANJI_KOHII_WORDS_URL = "https://kanji.koohii.com/revtk/study/keywords-rtk-1.js"


def _extract_word_list(text):
    pattern = r"kwlist=(\[\".*\"\]);"
    words_string = re.search(pattern, text).groups()[0]
    return json.loads(words_string)


def _extract_kanji_list(text):
    pattern = r"kklist='(.*)';"
    kanji_string = re.search(pattern, text).groups()[0]
    return [glyph for glyph in kanji_string]


def get_kanji_word_list(url=KANJI_KOHII_WORDS_URL):
    response = requests.get(url, headers=REQUEST_HEADERS)
    response.raise_for_status()

    response_text = response.text.replace("\n", "")

    words = _extract_word_list(response_text)
    kanjis = _extract_kanji_list(response_text)

    return [
        {"kanji": kanji, "definition": words[index]}
        for index, kanji in enumerate(kanjis)
    ]
