import os

from req.Helpers.user_session import UserSession
from req.Api.req_elements_eater import ElementsEater


class ElementsEaterCase(UserSession):

    def case_elements_eater_reports_export_post(self):
        req = ElementsEater(self.sess, self.host)

        data = {"mode": "id", "report_ids": ["153"]}
        resp = req.elements_eater_reports_export_post(data)
        # 30704 # {"res":{"version":"1.10"}}
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_elements_eater_reports_import_post(self):
        req = ElementsEater(self.sess, self.host)

        filepath = os.path.dirname(__file__) + "/../../Files/reportsData.json"

        # print(f"filepath is :{filepath}")
        # print(os.path.exists(filepath))

        with open(filepath, 'rb') as file:
            # resp = self.sess.post(f"{self.host}/back/dp.elements_eater/reports/import", headers=header, files={'file': f}, verify=False)
            resp = req.elements_eater_reports_import_post({'file': file})
        # print(resp.text)
