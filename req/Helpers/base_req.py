import json
import os


class BaseReq:

    def __init__(self, sess, host):
        self.sess = sess
        self.host = host

    def auth(self):
        username = os.environ.get('TARGET_API_USER', "dataplan_qaa@ngrsoftlab.ru")
        password = os.environ.get('TARGET_API_PASSWORD', "fHNHQBc7jEKfaO0kywZz!!")
        data = {
            "username": username,
            "password": password
        }
        resp = self.sess.post(f"{self.host}/back/dp.auth/login", json=data, verify=False)
        return resp
