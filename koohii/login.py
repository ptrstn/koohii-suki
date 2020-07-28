import bugmenot
import requests

from koohii.settings import REQUEST_HEADERS

KANJI_KOOHII_LOGIN_URL = "https://kanji.koohii.com/login"


def bugmenot_login_to_kanjii_koohi(url=KANJI_KOOHII_LOGIN_URL):
    credentials = bugmenot.get_credentials(url)
    for credential in credentials:
        username = credential.get("username")
        password = credential.get("password")
        try:
            return login_to_kanji_koohii(username=username, password=password)
        except ValueError:
            pass
    raise Exception("No valid credentials available.")


def login_to_kanji_koohii(username, password):
    session = requests.session()
    payload = {
        "referer": "@homepage",
        "username": username,
        "password": password,
        "commit": "Sign In",
    }
    login_response = session.post(
        KANJI_KOOHII_LOGIN_URL, data=payload, headers=REQUEST_HEADERS
    )
    if "Invalid username" in login_response.text:
        raise ValueError("Invalid username and/or password.")
    return session
