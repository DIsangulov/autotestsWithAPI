import json
import random

from req.Helpers.base_req import BaseReq
from resourses.credentials import DbName

API_AUTO_TEST_ = "API_AUTO_TEST_"

query_id = []           # 'id' sql запроса
report_id = []          # 'id' отчета
visualisation_id = []   # 'id' визуализации


class Visualisation(BaseReq):

    def _get_user_id(self) -> int:
        """Возвращает 'user_id' текущего пользователя"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/profile", headers=header, verify=False)
        dct = json.loads(resp.text)
        return dct['res']['user_id']

    def _get_query_id(self) -> int:
        self.visualisation_query_get()              # запрос на получение списка всех 'query'
        if len(query_id) == 0:                      # global query_id
            self.visualisation_query_save_post()    # если нет, создай новый
            # FIXME: после создания, добавлять id в список 'query_id'
        return query_id[-1]

    def _get_report_id(self) -> int:
        self.visualisation_reports_get()            # запрос на получение списка всех отчетов
        if len(report_id) == 0:                     # global report_id
            self.visualisation_reports_post()       # если нет, создать новый
            # FIXME: после создания, добавлять id в список 'report_id'
        return report_id[-1]

    def _get_visualisation_id(self) -> int:
        self.visualisation_visualisation_get()      # запрос на получение списка всех визуализаций
        if len(visualisation_id) == 0:              # global visualisation_id
            self.visualisation_visualisation_post()     # создание новой визуализации
            # FIXME: после создания, добавлять id в список 'visualisation_id'
        return visualisation_id[-1]

    def visualisation_query_get(self):
        """process GET req for getting query list"""
        # front: при создании визуализации > добавить серию > источник данных
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/query", headers=header, verify=False)

        query_info_rows = json.loads(resp.text)
        for _row in query_info_rows['res']:
            if str(_row['name']).startswith(API_AUTO_TEST_):
                query_id.append(int(_row['id']))

        return resp

    def visualisation_query_do_query_id_post(self):
        """process POST req with filters for executing query with id = query_id."""
        _query_id = self._get_query_id()
        header = {'token': self.token}
        data = {"data": None}
        resp = self.sess.post(f"{self.host}/back/dp.visualisation/query/do/" + str(_query_id), headers=header, json=data, verify=False)
        return resp

    def visualisation_query_save_post(self):
        """process POST req for creating/editing query by id"""

        random_num = random.randint(0, 999)
        self_user_id = self._get_user_id()                                  # Получить свой 'user_id'
        # db_picker_tables = self._get_db_id_by_name(DbName.picker_tables)    # Получить 'id' хранилища 'picker_tables'
        db_picker_tables = self.get_db_id_by_name(DbName.picker_tables)

        header = {'token': self.token}
        data = {
            "db_id": db_picker_tables,
            "name": API_AUTO_TEST_ + str(random_num),
            "description": API_AUTO_TEST_ + str(random_num),
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

        resp = self.sess.post(f"{self.host}/back/dp.visualisation/query/save", headers=header, json=data, verify=False)
        return resp

    def visualisation_query_do_query_usage_id_get(self):
        _query_id = self._get_query_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/query/usage/" + str(_query_id), headers=header, verify=False)
        return resp

    def visualisation_query_do_query_id_get(self):
        _query_id = self._get_query_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/query/" + str(_query_id), headers=header, verify=False)
        return resp

    def visualisation_query_do_query_id_delete(self):
        """process DELETE req for deleting query by id"""
        _query_id = self._get_query_id()
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.visualisation/query/" + str(_query_id), headers=header, verify=False)
        return resp

    def visualisation_reports_post(self):
        random_num = random.randint(100, 999)
        self_user_id = self._get_user_id()  # получить свой 'user_id'
        header = {'token': self.token}
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
        resp = self.sess.post(f"{self.host}/back/dp.visualisation/reports", headers=header, json=data, verify=False)
        return resp

    def visualisation_reports_get(self):
        """process GET req for getting reports list"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/reports", headers=header, verify=False)

        report_id_info_rows = json.loads(resp.text)['res']
        for _row in report_id_info_rows:
            # print(_row)
            if str(_row['name']).startswith(API_AUTO_TEST_):
                report_id.append(int(_row['id']))

        return resp

    def visualisation_reports_report_id_get(self):
        _rep_id = self._get_report_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/reports/" + str(_rep_id), headers=header, verify=False)
        return resp

    def visualisation_reports_report_id_delete(self):
        _rep_id = self._get_report_id()
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.visualisation/reports/" + str(_rep_id), headers=header, verify=False)
        return resp

    def visualisation_visualisation_post(self):
        """process POST req for creating/editing visualisation by id"""
        self_user_id = self._get_user_id()  # получить свой 'user_id'
        header = {'token': self.token}
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
        resp = self.sess.post(f"{self.host}/back/dp.visualisation/visualisation", headers=header, json=data, verify=False)
        return resp

    def visualisation_visualisation_get(self):
        """process GET req for getting visualisations list"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/visualisation", headers=header, verify=False)

        vis_id_info_rows = json.loads(resp.text)['res']
        for _row in vis_id_info_rows:
            if str(_row['name']).startswith(API_AUTO_TEST_):
                visualisation_id.append(int(_row['id']))
        # print(f"vis_id is: {visualisation_id}")

        return resp

    def visualisation_visualisation_dataseries_visualisation_id_post(self):
        _vis_id = self._get_visualisation_id()
        _query_id = self._get_query_id()
        header = {'token': self.token}
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
        resp = self.sess.post(f"{self.host}/back/dp.visualisation/visualisation/dataseries/" + str(_vis_id), headers=header, json=data, verify=False)
        return resp

    def visualisation_visualisation_types_get(self):
        # front: создание визуализации > добавить серию > тип элемента
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/visualisation/types", headers=header, verify=False)
        return resp

    def visualisation_visualisation_usage_visualisation_id_get(self):
        """process GET req for getting visualisation usages in reports by id"""
        _vis_id = self._get_visualisation_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/visualisation/usage/" + str(_vis_id), headers=header, verify=False)
        return resp

    def visualisation_visualisation_visualisation_id_get(self):
        """process GET req for getting visualisation by id"""
        _vis_id = self._get_visualisation_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/visualisation/" + str(_vis_id), headers=header, verify=False)
        return resp

    def visualisation_visualisation_visualisation_id_delete(self):
        """process DELETE req for deleting visualisation by id"""
        _vis_id = self._get_visualisation_id()
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.visualisation/visualisation/" + str(_vis_id), headers=header, verify=False)
        return resp
