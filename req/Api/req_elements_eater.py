import os

from req.Helpers.base_req import BaseReq


class ElementsEater(BaseReq):

    def elements_eater_reports_export_post(self):
        data = {"mode": "id", "report_ids": ["153"]}
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.elements_eater/reports/export", headers=header, json=data, verify=False)
        return resp

    def elements_eater_reports_import_post(self):
        header = {'token': self.token}
        filepath = os.path.dirname(
            os.path.dirname(__file__)) + "/Files/reportsData.json"  # filepath = "./путь до файла"
        with open(filepath, 'rb') as f:
            resp = self.sess.post(f"{self.host}/back/dp.elements_eater/reports/import", headers=header, files={'file': f}, verify=False)
        return resp
