import json

import allure
import pytest
import requests
import testit
import urllib3

from self import self

from req.Api.req_auth import AuthApi
from req.Helpers.base_req import BaseReq
from req.Api.req_absorber import Absorber
from req.Api.req_alarmer import Alarmer
from req.Api.req_core import Core
from req.Api.req_licenser import Licenser
from req.Api.req_peopler import Peopler
from utilities.logger import Logger
from req.Api.req_permitter import Permitter

urllib3.disable_warnings()
# ________Constants________
sess = requests.Session()
host = "https://10.130.0.22"
# ________Constants________

# _________Globals_________
auth_token = None
uid = None
user_id = None


# _________Globals_________
class TestFor:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']
        print(auth_token)

    # ____________________________________________________________

    def test_permitter_db_watcher_all_db(self):
        req = Permitter(sess, host)
        resp = req.permitter_db_watcher_all_db(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_all_tables(self):
        req = Permitter(sess, host)
        resp = req.permitter_db_watcher_all_tables(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
