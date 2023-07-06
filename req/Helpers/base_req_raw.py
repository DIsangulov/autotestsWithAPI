import requests


class BaseReqRaw:
    def __init__(self, sess: requests.Session, host):
        self.sess = sess
        self.host = host
