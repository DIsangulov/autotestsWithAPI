import json
import random

from req.Helpers.base_req import BaseReq

rand = None
rep_id = None
at_uid = None


class Reporter(BaseReq):

    def peopler_users_at_uid_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/users", headers=header, verify=False)
        name = 'dataplan_qaa@ngrsoftlab.ru'
        users = json.loads(resp.text)['res']
        uid = next((user for user in users if user['name'] == name), None)
        global at_uid
        at_uid = uid['id']
        return resp

    def reporter_mailing_post(self, token):
        global rand
        rand = random.randint(1200, 12500)
        data = {
            "name": "TestAPIReport" + str(rand),
            "description": "",
            "type": 0,
            "author_id": at_uid,
            "status": False,
            "report_id": 158,
            "email": True,
            "elements": [
                282
            ],
            "receivers": [
                1212
            ],
            "settings": {
                "text": "TestAPIReport",
                "topic": "TestAPIReport",
                "report_settings": {
                    "file_format": 1
                },
                "criterion": []
            }
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.reporter/mailing", headers=header, json=data, verify=False)
        return resp

    def reporter_mailing_sample_post(self, token):
        data = {
            "settings": {
                "report_settings": {
                    "file_format": 1
                },
                "text": "АПИтест1",
                "topic": "АПИтест1"
            },
            "type": 0,
            "name": "АПИтест1",
            "report_id": 158,
            "elements": [
                282
            ],
            "editor_id": at_uid
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.reporter/mailing/sample", headers=header, json=data, verify=False)
        return resp

    def reporter_mailing_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.reporter/mailing", headers=header, verify=False)
        dct = json.loads(resp.text)
        global rep_id
        rep_id = dct['res'][0]['id']  # получили id отчета
        print(rep_id)
        return resp

    def reporter_mailing_put(self, token):
        global rand
        rand = random.randint(1200, 12500)
        data = {
            "id": rep_id,
            "name": "TestAPIReport3813",
            "description": "",
            "published": False,
            "opened": False,
            "author_id": at_uid,
            "author_name": "dataplan_qaa@ngrsoftlab.ru",
            "editor_id": at_uid,
            "editor_name": "dataplan_qaa@ngrsoftlab.ru",
            "created": "2023-03-02T12:10:19.252188Z",
            "edited": "2023-03-02T12:10:19.252188Z",
            "type": 0,
            "status": False,
            "syslog": False,
            "email": True,
            "db_id": None,
            "report_id": 157,
            "settings": {
                "sampled": False,
                "text": "TestAPIReport",
                "topic": "TestAPIReport",
                "ip": "",
                "port": 0,
                "protocol": "",
                "report_settings": {
                    "file_format": 1
                },
                "data_settings": {
                    "time_column": "",
                    "table_name": ""
                }
            },
            "elements": [
                282
            ],
            "receivers": [
                1212
            ]
        }
        header = {'token': token}
        resp = self.sess.put(f"{self.host}/back/dp.reporter/mailing", headers=header, json=data, verify=False)
        return resp

    def reporter_mailing_type_0_1_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.reporter/mailing/typed/0_1", headers=header, verify=False)
        return resp

    def reporter_mailing_type_2_3_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.reporter/mailing/typed/2_3", headers=header, verify=False)
        return resp

    def reporter_mailing_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.reporter/mailing/" + str(rep_id), headers=header, verify=False)
        return resp

    def reporter_screener_fast_png_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.reporter/screener/fast/png/158", headers=header,
                             verify=False)
        return resp

    def reporter_screener_fast_pdf_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.reporter/screener/fast/pdf/158", headers=header,
                             verify=False)
        return resp

    def reporter_screener_fast_xlsx_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.reporter/screener/fast/xlsx/158", headers=header,
                             verify=False)
        return resp

    def reporter_visualisation_cached_role_report_report_id_role_id_post(self, token):
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.reporter/visualisation_cached/role_report/158/1",
                              headers=header, verify=False)
        return resp

    def reporter_mailing_id_delete(self, token):
        header = {'token': token}
        resp = self.sess.delete(f"{self.host}/back/dp.reporter/mailing/" + str(rep_id), headers=header, verify=False)
        return resp

    def reporter_visualisation_cached_user_report_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.reporter/visualisation_cached/user_report", headers=header,
                             verify=False)
        return resp

    def reporter_visualisation_cached_user_report_report_id_post(self, token):
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.reporter/visualisation_cached/user_report/158", headers=header,
                              verify=False)
        return resp
