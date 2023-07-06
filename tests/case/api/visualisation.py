import json
import random

from req.Helpers.base_req import BaseReq
from req.Api.req_visualisation import Visualisation
from resourses.credentials import DbName

API_AUTO_TEST_ = "API_AUTO_TEST_"

query_id = []           # 'id' sql запроса
report_id = []          # 'id' отчета
visualisation_id = []   # 'id' визуализации

# TODO: есть подозрения, что бек не отрабатывает иногда запросы со значением smth_id = None


class VisualisationCase(BaseReq):

    def _get_query_id(self) -> int:
        self.case_visualisation_query_get()             # запрос на получение списка всех 'query'
        if len(query_id) == 0:                          # global query_id
            self.case_visualisation_query_save_post()   # если нет, создай новый
            # FIXME: после создания, добавлять id в список 'query_id'
        return query_id[-1]

    def _get_report_id(self) -> int:
        self.case_visualisation_reports_get()           # запрос на получение списка всех отчетов
        if len(report_id) == 0:                         # global report_id
            self.case_visualisation_reports_post()      # если нет, создать новый
            # FIXME: после создания, добавлять id в список 'report_id'
        return report_id[-1]

    def _get_visualisation_id(self) -> int:
        self.case_visualisation_visualisation_get()         # запрос на получение списка всех визуализаций
        if len(visualisation_id) == 0:                      # global visualisation_id
            self.case_visualisation_visualisation_post()    # создание новой визуализации
            # FIXME: после создания, добавлять id в список 'visualisation_id'
        return visualisation_id[-1]

    def case_visualisation_query_get(self):
        req = Visualisation(self.sess, self.host)
        resp = req.visualisation_query_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

        # FIXME: перенести в _get_query_id
        query_info_rows = json.loads(resp.text)
        for _row in query_info_rows['res']:
            if str(_row['name']).startswith(API_AUTO_TEST_):
                query_id.append(int(_row['id']))

        return resp

    def case_visualisation_query_do_query_id_post(self):
        req = Visualisation(self.sess, self.host)
        _query_id = self._get_query_id()
        data = {"data": None}
        resp = req.visualisation_query_do_query_id_post(_query_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_query_save_post(self):
        req = Visualisation(self.sess, self.host)

        str_random_num = str(random.randint(100, 999))
        self_user_id = self.get_self_user_id()                              # Получить свой 'user_id'
        db_picker_tables = self.get_db_id_by_name(DbName.picker_tables)     # Получить 'id' хранилища 'picker_tables'

        data = {
            "db_id": db_picker_tables,
            "name": API_AUTO_TEST_ + str_random_num,
            "description": API_AUTO_TEST_ + str_random_num,
            "published": False,
            "opened": False,
            "settings": {
                "base_id": None,
                "tab_name": "ad_groups_ngr",            # FIXME:    ?
                "columns": [
                    {
                        "name": "canonicalName",
                        "type": "String"
                    }
                ],
                "groupby": [],
                "filters": [],
                "agregators": [],
                "limit": 50
            },
            "db_name": DbName.picker_tables,
            "query": "",
            "auto": True,
            "editor_id": self_user_id,
            "editor": self.username,
            "created": "2023-03-09T06:37:20Z",        # FIXME: дата устанавливается > подцепать 'текущую дату'
            "modified": "2023-03-09T06:37:20Z",       # FIXME: дата устанавливается
            "author_id": self_user_id,
            "author": self.username
        }
        resp = req.visualisation_query_save_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_query_do_query_usage_id_get(self):
        req = Visualisation(self.sess, self.host)
        _query_id = self._get_query_id()
        resp = req.visualisation_query_do_query_usage_id_get(_query_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_query_query_id_get(self):
        req = Visualisation(self.sess, self.host)
        _query_id = self._get_query_id()
        resp = req.visualisation_query_query_id_get(_query_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_query_do_query_id_delete(self):
        req = Visualisation(self.sess, self.host)
        _query_id = self._get_query_id()
        resp = req.visualisation_query_do_query_id_delete(_query_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_reports_get(self):
        req = Visualisation(self.sess, self.host)
        resp = req.visualisation_reports_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)


        # FIXME: перенести в _get_report_id
        report_id_info_rows = json.loads(resp.text)['res']
        for _row in report_id_info_rows:
            # print(_row)
            if str(_row['name']).startswith(API_AUTO_TEST_):
                report_id.append(int(_row['id']))

        return resp

    def case_visualisation_reports_post(self):
        req = Visualisation(self.sess, self.host)
        random_num = random.randint(100, 999)
        self_user_id = self.get_self_user_id()  # получить свой 'user_id'
        data = {
            "name": f"{API_AUTO_TEST_}report_{random_num}",
            "description": f"{API_AUTO_TEST_}report_description",
            "created": "2023-03-09T07:20:34.318Z",
            "modified": "2023-03-09T07:20:34.318Z",
            "author_id": self_user_id,
            "editor": self.username,
            "editor_id": self_user_id,
            "published": False
        }
        resp = req.visualisation_reports_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_reports_report_id_get(self):
        req = Visualisation(self.sess, self.host)
        _rep_id = self._get_report_id()
        resp = req.visualisation_reports_report_id_get(_rep_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_reports_report_id_delete(self):
        req = Visualisation(self.sess, self.host)
        _rep_id = self._get_report_id()
        resp = req.visualisation_reports_report_id_delete(_rep_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_visualisation_get(self):
        req = Visualisation(self.sess, self.host)
        resp = req.visualisation_visualisation_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

        # FIXME: перенести в _get_visualisation_id
        vis_id_info_rows = json.loads(resp.text)['res']
        for _row in vis_id_info_rows:
            if str(_row['name']).startswith(API_AUTO_TEST_):
                visualisation_id.append(int(_row['id']))
        # print(f"vis_id is: {visualisation_id}"
        return resp

    def case_visualisation_visualisation_post(self):
        req = Visualisation(self.sess, self.host)
        self_user_id = self.get_self_user_id()  # получить свой 'user_id'
        data = {
            "name": f"{API_AUTO_TEST_}visualisation",
            "description": f"{API_AUTO_TEST_}visualisation",
            "published": False,
            "opened": False,
            "author_id": self_user_id,
            "editor_id": self_user_id,
            "author": self.username,
            "editor": self.username,
            "created": "2023-03-09T07:42:21.722Z",  # FIXME: ??
            "modified": "2023-03-09T07:42:21.722Z",
            "grid": [],
            "snapshot": "",
            "base_image": "",
            "settings": {}
        }
        resp = req.visualisation_visualisation_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_visualisation_dataseries_visualisation_id_post(self):
        req = Visualisation(self.sess, self.host)
        _vis_id = self._get_visualisation_id()
        _query_id = self._get_query_id()
        data = {
            "name": API_AUTO_TEST_ + "data_series",
            "description": API_AUTO_TEST_ + "data_series desc",
            "element_type": 1,
            "query_id": _query_id,
            "data": "",
            "stage_num": 1,
            "dataset": {
                "x": None,
                "y": [
                    None
                ]
            },
            "settings": {
                "chart": {
                    "fill": False,
                    "showLine": False,
                    "tension": 0
                },
                "interaction": {
                    "mode": "point"
                },
                "plugins": {
                    "tooltip": {
                        "enabled": False
                    },
                    "legend": {
                        "display": False,
                        "position": "top"
                    }
                },
                "annotations": False
            },
            "subquery_id": None,
            "subquery_field": ""
        }
        resp = req.visualisation_visualisation_dataseries_visualisation_id_post(_vis_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_visualisation_types_get(self):
        req = Visualisation(self.sess, self.host)
        resp = req.visualisation_visualisation_types_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_visualisation_usage_visualisation_id_get(self):
        req = Visualisation(self.sess, self.host)
        _vis_id = self._get_visualisation_id()
        resp = req.visualisation_visualisation_usage_visualisation_id_get(_vis_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_visualisation_visualisation_id_get(self):
        req = Visualisation(self.sess, self.host)
        _vis_id = self._get_visualisation_id()
        resp = req.visualisation_visualisation_visualisation_id_get(_vis_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def visualisation_visualisation_visualisation_id_delete(self):
        req = Visualisation(self.sess, self.host)
        _vis_id = self._get_visualisation_id()
        resp = req.visualisation_visualisation_visualisation_id_delete(_vis_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)
