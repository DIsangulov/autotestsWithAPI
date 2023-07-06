import requests

from req.Helpers.base_req_raw import BaseReqRaw


class ElementsEater(BaseReqRaw):

    def elements_eater_reports_export_post(self, data) -> requests.Response:
        """process POST req for exporting reports by ids"""
        return self.sess.post(f"{self.host}/back/dp.elements_eater/reports/export", json=data)

    def elements_eater_reports_import_post(self, files) -> requests.Response:
        """process POST req for importing reports into platform"""
        # files={'file': f}
        return self.sess.post(f"{self.host}/back/dp.elements_eater/reports/import", files=files)
