from requests_oauthlib import OAuth1Session
from __init__ import Swooper


def set_config():
    return Swooper.load_config()

def create_oauth1_session(service):
    config = set_config()
    CK = config.get(service, "consumer_key")
    CS = config.get(service, "consumer_secret")
    AT = config.get(service, "access_token")
    ATS = config.get(service, "access_token_secret")

    return OAuth1Session(CK, CS, AT, ATS)
