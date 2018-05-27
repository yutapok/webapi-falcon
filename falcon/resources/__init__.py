from __init__ import Swooper

class CommonResource(object):
    def __init__(self):
        self.config = Swooper.load_config()
