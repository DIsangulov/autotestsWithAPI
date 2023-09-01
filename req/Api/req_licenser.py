import requests

from req.Helpers.base_req import BaseReq


class Licenser(BaseReq):

    def licenser_activate_post(self, data):
        """process POST req for activating license with text key"""
        return self.sess.post(f"{self.host}/back/dp.licenser/activate", json=data)

    def licenser_file_activate_post(self, files):
        """process POST req for activating license with file key"""
        return self.sess.post(f"{self.host}/back/dp.licenser/file_activate", files=files)

    def licenser_license_info_get(self):
        """process GET req for getting current license info"""
        return self.sess.get(f"{self.host}/back/dp.licenser/license_info")

    def licenser_set_company_post(self, data):
        """process POST req for setting company name"""
        return self.sess.post(f"{self.host}/back/dp.licenser/set_company", json=data)
