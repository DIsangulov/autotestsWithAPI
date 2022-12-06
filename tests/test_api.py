import json
import pytest
import requests
import urllib3
from self import self

from req.Api.req_auth import AuthApi
from req.Helpers.base_req import BaseReq

urllib3.disable_warnings()
# ________Constants________
sess = requests.Session()
host = "https://10.130.0.22"
# ________Constants________

# _________Globals_________
auth_token = None
uid = None


# _________Globals_________


class TestAuth:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']

    def test_ad_struct(self):
        req = AuthApi(sess, host)
        resp = req.ad_struct(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_ou_users(self):
        req = AuthApi(sess, host)
        resp = req.ou_users(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions(self):
        req = AuthApi(sess, host)
        resp = req.sessions(auth_token)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions_uid(self):
        req = AuthApi(sess, host)
        resp = req.sessions_uid(auth_token)

        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions_one_sid_del(self):  # sid вкорячен в req_auth в метод sessions_one_sid_del
        req = AuthApi(sess, host)
        resp = req.sessions_one_sid_del(auth_token)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions_all_uid_del(self):
        self.test_get_token()
        req = AuthApi(sess, host)
        resp = req.sessions_all_uid_del(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # __________________________________LOGOUT_______________________________________

    def test_logout(self):
        self.test_get_token()
        req = AuthApi(sess, host)
        resp = req.sessions(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
