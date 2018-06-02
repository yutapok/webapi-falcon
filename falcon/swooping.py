import sys
import re
import falcon
import json
import requests
import configparser
from resources.sns import SnsTwHandleResource
from resources.sns import SnsSlackHandleResource

app = falcon.API()
app.add_route("/hook.pokkun.rss-update-tw", SnsTwHandleResource())
app.add_route("/hook.pokkun.rss-update-slack", SnsSlackHandleResource())
