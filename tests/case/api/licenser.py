import os

from req.Helpers.user_session import UserSession
from req.Api.req_licenser import Licenser


class LicenserCase(UserSession):

    def case_licenser_activate_post(self):
        # кидаем кривой ключ и ждем что его отобъет
        req = Licenser(self.sess, self.host)
        body = {
            "key": "123-456-789"
        }
        resp = req.licenser_activate_post(body)
        # print(resp.text)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_licenser_file_activate_post(self):
        req = Licenser(self.sess, self.host)

        filepath = os.path.dirname(__file__) + "/../../Files/correct_license.license"

        with open(filepath, 'rb') as file:
            resp = req.licenser_file_activate_post({'file': file})
            print(resp.text)
        assert False

    def case_licenser_license_info_get(self):
        req = Licenser(self.sess, self.host)
        req.sess.headers.update({'skey': "ANGARA"})

        resp = req.licenser_license_info_get()
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_licenser_set_company_post(self):
        req = Licenser(self.sess, self.host)

        data = {}

        resp = req.licenser_set_company_post(data)
        print(resp.text)
        assert False
