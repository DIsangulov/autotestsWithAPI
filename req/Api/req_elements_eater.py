import os

from req.Helpers.base_req import BaseReq


class ElementsEater(BaseReq):

    def elements_eater_reports_export_post(self):
        """process POST req for exporting reports by ids"""
        data = {"mode": "id", "report_ids": ["153"]}
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.elements_eater/reports/export", headers=header, json=data, verify=False)
        return resp     # {"res":{"version":"1.10"}}

    # FIXME: AssertionError: Ошибка, код 400, {"error":{"code":400,"msg":"Найдены несовместимые версии"}}
    def elements_eater_reports_import_post(self):
        """process POST req for importing reports into platform"""
        header = {'token': self.token}
        filepath = os.path.dirname(
            os.path.dirname(__file__)) + "/Files/reportsData.json"  # filepath = "./путь до файла"

        print(f"filepath is :{filepath}")
        print(os.path.exists(filepath))

        # with open(filepath, 'rb') as f:
        #     resp = self.sess.post(f"{self.host}/back/dp.elements_eater/reports/import", headers=header, files={'file': f}, verify=False)
        # return resp
        return None