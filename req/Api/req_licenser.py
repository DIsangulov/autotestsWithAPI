import requests

from req.Helpers.base_req_raw import BaseReqRaw


class Licenser(BaseReqRaw):

    def licenser_activate_post(self, body) -> requests.Response:
        """process POST req for activating license with text key"""
        return self.sess.post(f"{self.host}/back/dp.licenser/activate", json=body)

    # TODO: [POST] /back/dp.licenser/file_activate

    def licenser_license_info_get(self) -> requests.Response:
        """process GET req for getting current license info"""
        return self.sess.get(f"{self.host}/back/dp.licenser/license_info")

    # TODO: [POST] /back/dp.licenser/set_company
