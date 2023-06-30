from req.Helpers.base_req import BaseReq


class Licenser(BaseReq):

    def licenser_activate_post(self):  # кидаем кривой ключ и ждем что его отобъет
        """process POST req for activating license with text key"""
        body = {
            "key": "123-456-789"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.licenser/activate", headers=header, json=body, verify=False)
        return resp

    # TODO: [POST] /back/dp.licenser/file_activate

    def licenser_license_info_get(self):
        """process GET req for getting current license info"""
        header = {'token': self.token, 'skey': "ANGARA"}
        resp = self.sess.get(f"{self.host}/back/dp.licenser/license_info", headers=header, verify=False)
        return resp

    # TODO: [POST] /back/dp.licenser/set_company
