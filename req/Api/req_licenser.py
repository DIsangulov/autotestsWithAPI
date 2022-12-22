from req.Helpers.base_req import BaseReq


class Licenser(BaseReq):

    def licenser_activate(self, token):  # кидаем кривой ключ и ждем что его отобъет
        body = {
            "key": "123-456-789"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.licenser/activate", headers=header, json=body, verify=False)
        return resp

    def licenser_license_info(self, token):
        header = {'token': token, 'skey': "ANGARA"}
        resp = self.sess.get(f"{self.host}/back/dp.licenser/license_info", headers=header, verify=False)
        return resp
