from handler import Common
import requests

def set_bot_token():
    return Common.set_config().get("SLACK", "bot_token")

def set_bot_username():
    return Common.set_config().get("SLACK", "bot_username")

def set_bot_channel():
    return Common.set_config().get("SLACK", "bot_channel")

def set_bot_post_uri():
    return Common.set_config().get("SLACK", "bot_post_uri")


def bot_post(uri, channel, username, token, text):
    if not uri and not isinstance(uri, str):
        return 400

    if not channel and not isinstance(channel, str):
        return 400

    if not username and not isinstance(username, str):
        return 400

    if not token and not isinstance(token, str):
        return 400

    if not text and not isinstance(text, list):
        return 400


    try:
        payload = {'token' : token, 'channel' : channel, 'text': "\n".join(text),'username' : username}
        requests.post(uri, data=payload)
        rc = 200

    except Exception as e:
        raise


    return rc
