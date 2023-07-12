import requests

from req.Helpers.base_req import BaseReq


class ElementsEater(BaseReq):

    def elements_eater_reports_export_post(self, data) -> requests.Response:
        """process POST req for exporting reports by ids"""
        return self.sess.post(f"{self.host}/back/dp.elements_eater/reports/export", json=data)

    def elements_eater_reports_import_post(self, files) -> requests.Response:
        """process POST req for importing reports into platform"""
        # files={'file': f}
        return self.sess.post(f"{self.host}/back/dp.elements_eater/reports/import", files=files)
