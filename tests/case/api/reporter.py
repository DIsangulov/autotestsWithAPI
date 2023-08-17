import json
import random

from req.Helpers.user_session import UserSession
from req.Api.req_reporter import Reporter
from tests.case.api.visualisation import VisualisationCase

API_AUTO_TEST_ = "API_AUTO_TEST_"

mailing_id = set()     # 'id' рассылок


class ReporterCase(UserSession):

    def get_report_id(self):
        return VisualisationCase().get_report_id()

    def _collect_mailing_id(self):
        resp = Reporter(self.sess, self.host).reporter_mailing_get()
        assert resp.status_code == 200, f"assert::reporter_mailing_get, failed. status_code: {resp.status_code}, text: {resp.text}"

        if resp.text != '{"res":null}\n':
            mailing_info_rows = json.loads(resp.text)['res']
            for _row in mailing_info_rows:
                if str(_row['name']).startswith(API_AUTO_TEST_):
                    mailing_id.add(int(_row['id']))
        # print(f"mailing_id is now: {mailing_id}")

    def get_mailing_id(self) -> int:
        if len(mailing_id) == 0:
            self._collect_mailing_id()

        if len(mailing_id) == 0:
            r_new_mailing = self.case_reporter_mailing_post()
            new_mailing_id = json.loads(r_new_mailing.text)['res']
            return int(new_mailing_id)

        return mailing_id.pop()

    def case_reporter_mailing_get(self):
        req = Reporter(self.sess, self.host)
        resp = req.reporter_mailing_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_reporter_mailing_put(self):
        req = Reporter(self.sess, self.host)
        str_random_num = str(random.randint(100, 999))
        _mailing_id = self.get_mailing_id()
        self_user_id = self.get_self_user_id()
        data = {
            "id": _mailing_id,
            "name": API_AUTO_TEST_ + str_random_num,
            "description": API_AUTO_TEST_ + str_random_num + "description",
            "published": False,
            "opened": False,
            # "author_id": at_uid,
            # "author_id": self_user_id,
            # "author_name": "dataplan_qaa@ngrsoftlab.ru",
            # "editor_id": at_uid,
            "editor_id": self_user_id,
            # "editor_name": "dataplan_qaa@ngrsoftlab.ru",
            # "created": "2023-03-02T12:10:19.252188Z",
            # "edited": "2023-03-02T12:10:19.252188Z",
            "type": 0,
            "status": False,
            "syslog": False,
            "email": True,
            "db_id": None,
            # "report_id": 526,
            "settings": {
                "sampled": False,
                "text": API_AUTO_TEST_ + "edit_text",
                "topic": API_AUTO_TEST_ + "edit_topic",
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
                # 282
            ],
            "receivers": [
                4870    # "s.yezhov@ngrsoftlab.ru"
            ]
        }
        resp = req.reporter_mailing_put(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_reporter_mailing_post(self):
        req = Reporter(self.sess, self.host)
        str_random_num = str(random.randint(100, 999))
        self_user_id = self.get_self_user_id()
        data = {
            # "id":           435,                              # 'id' самой рассылки
            "name":         API_AUTO_TEST_ + str_random_num,            # имя рассылки
            "description":  "описание рассылки",                # описание рассылки
            "published":    True,
            "opened":       True,
            "author_id":    self_user_id,                       # 'id' автора
            # "author_name":  "Владимир Даль",                  # >> по идее, имя автора
            # "editor_id":    self_user_id,                     # 'id' редактора >> 'id' автора
            # "editor_name":  "Владимир Даль",
            # "created":      "2023-06-21T12:04:39.021816Z",
            # "edited":       "2023-06-21T12:11:56.296546Z",
            "type":         0,
            "status":       True,
            "syslog":       False,
            "email":        True,
            "db_id":        None,
            "report_id":    self.get_report_id(),               # 'id' отчета, из которой делается рассылка >> выпадающий список "Отчет"
            "settings":
                {
                    "sampled":          False,
                    "text":             API_AUTO_TEST_ + "text",                            # Текст письма
                    "topic":            API_AUTO_TEST_ + "topic",             # Тема письма
                    "ip":               "",
                    "port":             0,
                    "protocol":         "",
                    "report_settings":  {"file_format": 1},
                    "data_settings":    {"time_column": "","table_name": ""}
                },
            "elements": None,   # >> видимо 'Элементы отчета' >> int
            "receivers": [      # 'id' получателей
                4870    # "s.yezhov@ngrsoftlab.ru"
            ]
        }
        resp = req.reporter_mailing_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)  # {"res":12345}
        return resp

    def case_reporter_mailing_sample_post(self):
        req = Reporter(self.sess, self.host)
        _report_id = self.get_mailing_id()
        data = {
            "settings": {
                "report_settings": {
                    "file_format": 1
                },
                "text": API_AUTO_TEST_ + "text",
                "topic": API_AUTO_TEST_ + "topic"
            },
            "type": 0,  # 0 - report by schedule 1 - report by criterion 2 - new data mailing 3 - mailing by trigger
            "name": API_AUTO_TEST_ + "name",
            "report_id": _report_id,
            "elements": [
                # 282
            ],
            "editor_id": self.get_self_user_id()
        }
        resp = req.reporter_mailing_sample_post(data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_reporter_mailing_typed_0_1_get(self):
        req = Reporter(self.sess, self.host)
        _type = "0_1"
        resp = req.reporter_mailing_typed_type_get(_type)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_reporter_mailing_typed_2_3_get(self):
        req = Reporter(self.sess, self.host)
        _type = "2_3"
        resp = req.reporter_mailing_typed_type_get(_type)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_reporter_mailing_id_get(self):
        req = Reporter(self.sess, self.host)
        _mailing_id = self.get_mailing_id()
        resp = req.reporter_mailing_id_get(_mailing_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_reporter_mailing_id_delete(self):
        req = Reporter(self.sess, self.host)
        _mailing_id = self.get_mailing_id()

        resp = req.reporter_mailing_id_delete(_mailing_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_reporter_screener_fast_png_post(self):
        req = Reporter(self.sess, self.host)
        data = {
            "format": "png",
            # "need_page": "/report/" + str(_rep_id)
            "need_page": "/report"
        }
        resp = req.reporter_screener_fast_post(data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_reporter_screener_fast_pdf_post(self):
        req = Reporter(self.sess, self.host)
        data = {
            "format": "pdf",
            # "need_page": "/report/" + str(_rep_id)
            "need_page": "/report"
        }
        resp = req.reporter_screener_fast_post(data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # __del__
    def all_api_auto_test_mailing_delete(self):
        delete_req = Reporter(self.sess, self.host)
        self._collect_mailing_id()
        while len(mailing_id) > 0:
            delete_req.reporter_mailing_id_delete(mailing_id.pop())
