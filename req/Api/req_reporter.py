import json
import random

from req.Helpers.base_req import BaseReq

mailing_id = []     # 'id' рассылок


class Reporter(BaseReq):

    def _get_mailing_id(self) -> int:
        if len(mailing_id) == 0:
            self.reporter_mailing_get()
        # FIXME: список рассылок mailing_id всё ещё может остаться пустым
        return mailing_id[-1]

    def reporter_mailing_get(self):
        """process GET req for getting all mailings from library"""
        # получение всех рассылок (*редактором которых является запросивший)
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.reporter/mailing", headers=header, verify=False)

        # FIXME: перенести в _get_mailing_id
        dct = json.loads(resp.text)
        for _row in dct['res']:
            # print(_row)
            mailing_id.append(int(_row['id']))
        # print(f"report_id is now: {rep_id}")
        return resp

    def reporter_mailing_put(self):
        """process PUT req for changing mailing"""
        _mailing_id = self._get_mailing_id()
        self_user_id = self.get_self_user_id()
        data = {
            "id": _mailing_id,
            "name": "TestAPIReport_auto_edit_" + str(random.randint(0, 999)),
            "description": "test_api_report_edit",
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
                "text": "test_api_edit_text",
                "topic": "test_api_edit_topic",
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
                # 1212
            ]
        }
        header = {'token': self.token}
        resp = self.sess.put(f"{self.host}/back/dp.reporter/mailing", headers=header, json=data, verify=False)
        return resp

    def reporter_mailing_post(self):
        """process POST req for adding new mailing"""
        # исп: создание рассылки из отчета
        # на фронте видны у того, кто является "автором" рассылки
        self_user_id = self.get_self_user_id()
        data = {
            # "id":           435,                              # 'id' самой рассылки
            "name":         "TestAPIReport_auto_" + str(random.randint(0, 999)),            # имя рассылки
            "description":  "описание рассылки",                # описание рассылки
            "published":    False,
            "opened":       False,
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
            # "report_id":    526,                            # 'id' отчета, из которой делается рассылка >> выпадающий список "Отчет"
            "settings":
                {
                    "sampled":          False,
                    "text":             "текст",                            # Текст письма
                    "topic":            "тема измененная тема",             # Тема письма
                    "ip":               "",
                    "port":             0,
                    "protocol":         "",
                    "report_settings":  {"file_format": 1},
                    "data_settings":    {"time_column": "","table_name": ""}
                },
            "elements": None,   # >> видимо 'Элементы отчета' >> int
            "receivers": [      # 'id' получателей
                # 1234
            ]
        }

        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.reporter/mailing", headers=header, json=data, verify=False)
        # print(resp.text)  # {"res":12345}
        return resp

    def reporter_mailing_sample_post(self):
        """process POST req for getting mailing data sample from storage"""
        # исп: "Отправить тестовое письмо себе"
        _report_id = 408    # несуществующий 'report_id', статус код 200; письмо не придет
        data = {
            "settings": {
                "report_settings": {
                    "file_format": 1
                },
                "text": "api_test_auto_text",
                "topic": "api_test_auto_topic"
            },
            "type": 0,
            "name": "api_test_auto_name",
            "report_id": _report_id,
            "elements": [
                # 282
            ],
            # "editor_id": 4870
            "editor_id": self.get_self_user_id()
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.reporter/mailing/sample", headers=header, json=data, verify=False)
        return resp

    # TODO: [GET] /back/dp.reporter/mailing/typed/{type}

    def reporter_mailing_type_0_1_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.reporter/mailing/typed/0_1", headers=header, verify=False)
        return resp

    def reporter_mailing_type_2_3_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.reporter/mailing/typed/2_3", headers=header, verify=False)
        return resp

    def reporter_mailing_id_get(self):
        """process GET req for getting mailing by id"""
        _mailing_id = self._get_mailing_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.reporter/mailing/{_mailing_id}", headers=header, verify=False)
        return resp

    def reporter_mailing_id_delete(self):
        """process DELETE req for deleting mailing"""
        # исп: удалить рассылку
        _mailing_id = self._get_mailing_id()
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.reporter/mailing/{_mailing_id}", headers=header, verify=False)
        return resp

    # TODO: [POST] /back/dp.reporter/screener/fast

    def reporter_screener_fast_png_post(self):
        # https://tasks.ngrsoftlab.ru/browse/DAT-4983
        # _rep_id = get_rep_id  # _rep_id = 10

        data = {
            "format": "png",
            # "need_page": "/report/" + str(_rep_id)
            "need_page": "/report"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.reporter/screener/fast", headers=header, json=data, verify=False)
        return resp

    def reporter_screener_fast_pdf_post(self):
        # https://tasks.ngrsoftlab.ru/browse/DAT-4983
        # _rep_id = get_rep_id  # _rep_id = 10

        data = {
            "format": "pdf",
            # "need_page": "/report/" + str(_rep_id)
            "need_page": "/report"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.reporter/screener/fast", headers=header, json=data, verify=False)
        return resp

    # FIXME: нет описания [GET] /back/dp.reporter/screener/fast/{type}/{id}
    def reporter_screener_fast_xlsx_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.reporter/screener/fast/xlsx/158", headers=header, verify=False)
        return resp

    # FIXME: +front>usage // you can use _report_id where _report['published']==true?
    def reporter_visualisation_cached_role_report_report_id_role_id_post(self):
        """process POST req for setting report-role"""
        _report_id = 10
        _role_id = 1
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.reporter/visualisation_cached/role_report/{_report_id}/{_role_id}", headers=header, verify=False)
        return resp

    def reporter_visualisation_cached_user_report_get(self):
        """process GET req for getting report by id"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.reporter/visualisation_cached/user_report", headers=header, verify=False)
        return resp

    # FIXME: хардкод
    def reporter_visualisation_cached_user_report_report_id_post(self):
        """process POST req for setting report-user"""
        # исп: на странице отчета >> прикрепить к главной странице
        _report_id = 10    # _report_id = 0 >> открепить от главной страницы
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.reporter/visualisation_cached/user_report/{_report_id}", headers=header, verify=False)
        return resp
