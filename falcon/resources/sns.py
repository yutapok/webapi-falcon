import json
import redis
import falcon
from resources import CommonResource
from handler import SnsTweetHander
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

