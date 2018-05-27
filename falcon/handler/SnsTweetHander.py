from handler import Common
from requests_oauthlib import OAuth1Session

def set_end_url_upd():
    return Common.set_config().get("TWITTER", "end_point_upd")

def create_session_form():
    return Common.create_oauth1_session("TWITTER")

def tweet_post(sesseion, text, end_url):
    if not isinstance(sesseion, OAuth1Session):
        raise

    if not text:
        raise

    if not end_url:
        raise
 
    res = session.post(end_url, params = {"status" : text})
    return res.status_code
