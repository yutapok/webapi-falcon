import json
import redis
import falcon
from resources import CommonResource
from handler import SnsTweetHander
from handler import SnsSlackHandler
import Queueing

class SnsTwHandleResource(CommonResource):

    def __init__(self):
        self.tw_handle = SnsTweetHander
        self.tw_session = SnsTweetHander.create_session_form()
        self.end_url = SnsTweetHander.set_end_url_upd()
        self.redis_cli = Queueing.set_redis_cli()
        self.dequeue = Queueing.dequeue(self.redis_cli)

    def on_post(self, req, res):
        res.status = falcon.HTTP_200
        body = req.stream.read()
        data = json.loads(body.decode('utf-8'))
        key = data.get('key')
        if key:
            text = self.dequeue(key)
            result = self.tw_handle.tweet_post(self.tw_session, text, self.end_url)
        else:
            result = "not found tweet-queue"

        msg = {
            "tw_status": result ,
              }

        res.media = msg

class SnsSlackHandleResource(CommonResource):

    def __init__(self):
        self.slack_handle = SnsSlackHandler
        self.slack_token= self.slack_handle.set_bot_token()
        self.slack_usrname= self.slack_handle.set_bot_username()
        self.slack_channel= self.slack_handle.set_bot_channel()
        self.slack_uri= self.slack_handle.set_bot_post_uri()
        self.redis_cli = Queueing.set_redis_cli()
        self.dequeue = Queueing.dequeue(self.redis_cli)

    def on_post(self, req, res):
        res.status = falcon.HTTP_200
        body = req.stream.read()
        data = json.loads(body.decode('utf-8'))
        key = data.get('key')
        if key:
            text = self.dequeue(key)
            text_list = text.decode('utf-8').split('') if text else None
            result = self.slack_handle.bot_post(
                          self.slack_uri,
                          self.slack_channel,
                          self.slack_usrname,
                          self.slack_token,
                          text_list
                     )
        else:
            result = "not found slack-post--queue"

        msg = {
            "slack_status": result ,
              }

        res.media = msg



