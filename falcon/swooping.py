import sys
import re
import falcon
import json
import requests
import configparser
from resources.sns import SnsTwHandleResource

app = falcon.API()
app.add_route("/hook.pokkun.rss-update", SnsTwHandleResource())
