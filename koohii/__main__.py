import datetime
import time

import pandas

from koohii.kanji import get_kanji_word_list
from koohii.login import bugmenot_login_to_kanjii_koohi
from koohii.settings import CSV_FILE_NAME, SECONDS_TO_WAIT
from koohii.stories import get_kanji_stories


def scrape_kanji_stories():
    koohii_session = bugmenot_login_to_kanjii_koohi()
    kanji_word_list = get_kanji_word_list()
    kanji_characters = [entry["kanji"] for entry in kanji_word_list]

    stories_lists = []
    for idx, kanji in enumerate(kanji_characters):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S:%f")
        print(
            f"{timestamp} Retrieving stories for kanji {idx + 1}/{len(kanji_characters)}: {kanji} "
        )
        stories_lists.append(get_kanji_stories(koohii_session, kanji))
        time.sleep(SECONDS_TO_WAIT)

    stories = [story for stories in stories_lists for story in stories]
    stories_df = pandas.DataFrame(stories)
    kanji_df = pandas.DataFrame(kanji_word_list)
    return pandas.merge(stories_df, kanji_df, on="kanji")


def main():
    print("Scraping stories for all kanjis from https://kanji.koohii.com/")
    stories = scrape_kanji_stories()
    print(f"Saving stories as {CSV_FILE_NAME}...")
    stories.to_csv(CSV_FILE_NAME, index=False)


if __name__ == "__main__":
    main()
