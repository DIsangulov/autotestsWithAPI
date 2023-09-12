import json
import random

from req.Helpers.user_session import UserSession
from req.Api.req_visualisation import Visualisation
from resourses.constants import DB_picker_tables, API_AUTO_TEST_

query_id = set()           # 'id' sql запроса
report_id = set()          # 'id' отчета
visualisation_id = set()   # 'id' визуализации

# look: есть подозрения, что бек не отрабатывает иногда запросы со значением smth_id = None


class VisualisationCase(UserSession):

    def _collect_query_id(self):
        resp = Visualisation(self.sess, self.host).visualisation_query_get()
        assert resp.status_code == 200, f"assert::visualisation_query_get, failed. status_code: {resp.status_code}, text: {resp.text}"

        if resp.text == '{"res":null}\n':
            return None

        query_info_rows = json.loads(resp.text)
        for _row in query_info_rows['res']:
            if str(_row['name']).startswith(API_AUTO_TEST_):
                query_id.add(int(_row['id']))

    def get_query_id(self) -> int:
        if len(query_id) == 0:
            self._collect_query_id()

        if len(query_id) == 0:                                          # global query_id
            r_new_query = self.case_visualisation_query_save_post()     # если нет, создай новый
            new_query_id = json.loads(r_new_query.text)['res']
            return int(new_query_id)

        return query_id.pop()

    def _collect_report_id(self):
        resp = Visualisation(self.sess, self.host).visualisation_reports_get()
        assert resp.status_code == 200, f"assert::visualisation_reports_get, failed. status_code: {resp.status_code}, text: {resp.text}"

        if resp.text == '{"res":null}\n':
            return None

        report_id_info_rows = json.loads(resp.text)['res']
        for _row in report_id_info_rows:
            if str(_row['name']).startswith(API_AUTO_TEST_):
                report_id.add(int(_row['id']))

    def get_report_id(self) -> int:
        if len(report_id) == 0:
            self._collect_report_id()

        if len(report_id) == 0:                         # global report_id
            r_new_report = self.case_visualisation_reports_post()      # если нет, создать новый
            new_report_id = json.loads(r_new_report.text)['res']
            return int(new_report_id)

        return report_id.pop()

    def _collect_visualisation_id(self):
        resp = Visualisation(self.sess, self.host).visualisation_visualisation_get()
        assert resp.status_code == 200, f"assert::visualisation_visualisation_get, failed. status_code: {resp.status_code}, text: {resp.text}"

        if resp.text == '{"res":null}\n':
            return None

        vis_info_rows = json.loads(resp.text)['res']
        for _row in vis_info_rows:
            if str(_row['name']).startswith(API_AUTO_TEST_):
                visualisation_id.add(int(_row['id']))

    def get_visualisation_id(self) -> int:
        if len(visualisation_id) == 0:
            self._collect_visualisation_id()

        if len(visualisation_id) == 0:                      # global visualisation_id
            r_new_vis = self.case_visualisation_visualisation_post()    # создание новой визуализации
            new_vis_id = json.loads(r_new_vis.text)['res']
            return int(new_vis_id)

        return visualisation_id.pop()

    def case_visualisation_query_get(self):
        req = Visualisation(self.sess, self.host)
        resp = req.visualisation_query_get()
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_visualisation_query_do_query_id_post(self):
        req = Visualisation(self.sess, self.host)
        _query_id = self.get_query_id()
        data = {"data": None}
        resp = req.visualisation_query_do_query_id_post(_query_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_query_save_post(self):
        req = Visualisation(self.sess, self.host)

        str_random_num = str(random.randint(100, 999))
        self_user_id = self.get_self_user_id()
        # todo: проверить доступ к бд, перед созданием!
        db_id = self.get_db_id_by_name(DB_picker_tables.name)
        db_tab_name = DB_picker_tables.tab_Weather_all_online
        db_col_name = DB_picker_tables.col_Gorod

        data = {
            "db_id": db_id,
            "name": API_AUTO_TEST_ + str_random_num,
            "description": API_AUTO_TEST_ + str_random_num,
            # "published": True,
            # "opened": True,
            "settings": {
                "base_id": db_id,
                "tab_name": db_tab_name,
                "columns": [
                    {
                        "name": db_col_name,
                        "type": "String"
                    }
                ],
                "groupby": [],
                "filters": [],
                "agregators": [],
                "limit": 50
            },
            "db_name": DB_picker_tables.name,
            "query": "",
            "auto": True,
            "editor_id": self_user_id,
            "editor": self.username,
            # "created": "2023-03-09T06:37:20Z",
            # "modified": "2023-03-09T06:37:20Z",
            "author_id": self_user_id,
            "author": self.username
        }
        resp = req.visualisation_query_save_post(data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        return resp

    def case_visualisation_query_usage_id_get(self):
        req = Visualisation(self.sess, self.host)
        _query_id = self.get_query_id()
        resp = req.visualisation_query_usage_id_get(_query_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_query_query_id_get(self):
        req = Visualisation(self.sess, self.host)
        _query_id = self.get_query_id()
        resp = req.visualisation_query_query_id_get(_query_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_query_id_delete(self):
        req = Visualisation(self.sess, self.host)
        _query_id = self.get_query_id()
        resp = req.visualisation_query_id_delete(_query_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_reports_get(self):
        req = Visualisation(self.sess, self.host)
        resp = req.visualisation_reports_get()
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_visualisation_reports_post(self):
        req = Visualisation(self.sess, self.host)
        random_num = random.randint(100, 999)
        self_user_id = self.get_self_user_id()  # получить свой 'user_id'
        data = {
            "name": f"{API_AUTO_TEST_}report_{random_num}",
            "description": f"{API_AUTO_TEST_}report_description",
            # "created": "2034-03-09T07:20:34.318Z",    # look: 01.01.0001, 02:30
            # "modified": "2023-03-09T07:20:34.318Z",
            "author_id": self_user_id,
            "editor": self.username,
            "editor_id": self_user_id,
            "published": True
        }
        resp = req.visualisation_reports_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)
        return resp

    def case_visualisation_reports_params_report_id_post(self):
        req = Visualisation(self.sess, self.host)

        _report_id = 0

        data = {}

        resp = req.visualisation_reports_params_report_id_post(_report_id, data)
        print(resp.text)
        assert False

    def case_visualisation_reports_report_id_get(self):
        req = Visualisation(self.sess, self.host)
        _rep_id = self.get_report_id()
        resp = req.visualisation_reports_report_id_get(_rep_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_reports_report_id_delete(self):
        req = Visualisation(self.sess, self.host)
        _rep_id = self.get_report_id()
        resp = req.visualisation_reports_report_id_delete(_rep_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_visualisation_visualisation_get(self):
        req = Visualisation(self.sess, self.host)
        resp = req.visualisation_visualisation_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_visualisation_visualisation_post(self):
        req = Visualisation(self.sess, self.host)
        str_rand_num = str(random.randint(1000, 9999))
        self_user_id = self.get_self_user_id()  # получить свой 'user_id'
        data = {
            "name": f"{API_AUTO_TEST_}visualisation_{str_rand_num}",
            "description": f"{API_AUTO_TEST_}visualisation_description",
            "published": False,
            "opened": False,
            "author_id": self_user_id,
            "editor_id": self_user_id,
            "author": self.username,
            "editor": self.username,
            # "created": "2023-03-09T07:42:21.722Z",
            # "modified": "2023-03-09T07:42:21.722Z",
            "grid": [],
            "snapshot": "",
            "base_image": "",
            "settings": {}
        }
        resp = req.visualisation_visualisation_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)
        return resp

    def case_visualisation_visualisation_dataseries_visualisation_id_post(self):
        req = Visualisation(self.sess, self.host)
        str_rand_num = str(random.randint(1000, 9999))
        _vis_id = self.get_visualisation_id()
        _query_id = self.get_query_id()
        data = {
            "name": API_AUTO_TEST_ + "data_series_" + str_rand_num,
            "description": API_AUTO_TEST_ + "data_series_description",
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

    def case_visualisation_visualisation_dataseries_visualisation_id_dataseries_id_delete(self):
        req = Visualisation(self.sess, self.host)

        vis_id = 0
        dataseries_id = 0

        data = {}

        resp = req.visualisation_visualisation_dataseries_visualisation_id_dataseries_id_delete(vis_id, dataseries_id, data)
        print(resp.text)
        assert False

    def case_visualisation_visualisation_types_get(self):
        req = Visualisation(self.sess, self.host)
        resp = req.visualisation_visualisation_types_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_visualisation_usage_visualisation_id_get(self):
        req = Visualisation(self.sess, self.host)
        _vis_id = self.get_visualisation_id()
        resp = req.visualisation_visualisation_usage_visualisation_id_get(_vis_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_visualisation_visualisation_visualisation_id_get(self):
        req = Visualisation(self.sess, self.host)
        _vis_id = self.get_visualisation_id()
        resp = req.visualisation_visualisation_visualisation_id_get(_vis_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def visualisation_visualisation_visualisation_id_delete(self):
        req = Visualisation(self.sess, self.host)
        _vis_id = self.get_visualisation_id()
        resp = req.visualisation_visualisation_visualisation_id_delete(_vis_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    # __del__
    def all_api_auto_test_entity_delete(self):
        delete_req = Visualisation(self.sess, self.host)
        self._collect_query_id()
        while len(query_id) > 0:
            delete_req.visualisation_query_id_delete(query_id.pop())

        self._collect_report_id()
        while len(report_id) > 0:
            delete_req.visualisation_reports_report_id_delete(report_id.pop())

        self._collect_visualisation_id()
        while len(visualisation_id) > 0:
            delete_req.visualisation_visualisation_visualisation_id_delete(visualisation_id.pop())
