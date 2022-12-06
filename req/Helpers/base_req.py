import json


class BaseReq:
    def __init__(self, sess, host):
        self.sess = sess
        self.host = host

    def auth(self, username="dataplan_qaa@ngrsoftlab.ru", password="fHNHQBc7jEKfaO0kywZz!"):
        data = {
            "username": username,
            "password": password
        }
        resp = self.sess.post(f"{self.host}/back/dp.auth/login", json=data, verify=False)
        return resp

