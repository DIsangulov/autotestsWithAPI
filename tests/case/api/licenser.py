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
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_licenser_license_info_get(self):
        req = Licenser(self.sess, self.host)
        req.sess.headers.update({'skey': "ANGARA"})

        resp = req.licenser_license_info_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)
