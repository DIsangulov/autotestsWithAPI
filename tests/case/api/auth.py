import json
import random

from req.Helpers.base_req import BaseReq
from req.Api.req_auth import AuthApi, AuthApiNew

API_AUTO_TEST_ = "API_AUTO_TEST_"


class AuthApiCase(BaseReq):

    def case_auth_ad_struct_get(self):
        req = AuthApiNew(self.host, self.token)
        resp = req.auth_ad_struct_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        print(resp.text)
        return resp
