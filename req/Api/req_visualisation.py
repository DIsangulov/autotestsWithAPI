import json

from req.Helpers.base_req import BaseReq

query_id = None
rep_id = None
vis_id = None
at_uid = None
pt_id = None


class Visualisation(BaseReq):

    def peopler_users_at_uid_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/users", headers=header, verify=False)
        name = 'dataplan_qaa@ngrsoftlab.ru'
        users = json.loads(resp.text)['res']
        uid = next((user for user in users if user['name'] == name), None)
        global at_uid
        at_uid = uid['id']
        return resp

    def id_picker_table_get(self):  # забираем id таблицы picker_table
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/db",
                             headers=header, verify=False)
        json_data = json.loads(resp.text)
        global pt_id
        for item in json_data['res']:
            if item['name'] == 'picker_tables':
                pt_id = item['id']
        print(pt_id)
        return resp

    def visualisation_query_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/query", headers=header, verify=False)
        dct = json.loads(resp.text)
        global query_id
        query_id = dct['res'][0]['id']  # получили id sql запроса
        return resp

    def visualisation_query_do_query_id_post(self):
        header = {'token': self.token}
        data = {"data": None}
        resp = self.sess.post(f"{self.host}/back/dp.visualisation/query/do/" + str(query_id), headers=header,
                              json=data, verify=False)
        return resp

    def visualisation_query_save_post(self):
        header = {'token': self.token}
        data = {
            "db_id": pt_id,
            "name": "TestApi",
            "description": "TestApi",
            "published": False,
            "opened": False,
            "settings": {
                "base_id": None,
                "tab_name": "ad_groups_ngr",
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
            "db_name": "picker_tables",
            "query": "",
            "auto": True,
            "editor_id": at_uid,
            "editor": "dataplan_qaa@ngrsoftlab.ru",
            "created": "2023-03-09T06:37:20Z",
            "modified": "2023-03-09T06:37:20Z",
            "author_id": at_uid,
            "author": "dataplan_qaa@ngrsoftlab.ru"
        }
        resp = self.sess.post(f"{self.host}/back/dp.visualisation/query/save", headers=header,
                              json=data, verify=False)
        return resp

    def visualisation_query_do_query_usage_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/query/usage/" + str(query_id), headers=header,
                             verify=False)
        return resp

    def visualisation_query_do_query_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/query/" + str(query_id), headers=header,
                             verify=False)
        return resp

    def visualisation_query_do_query_id_delete(self):
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.visualisation/query/" + str(query_id), headers=header,
                                verify=False)
        return resp

    def visualisation_reports_post(self):
        header = {'token': self.token}
        data = {
            "name": "TestApiReport",
            "description": "TestApiReport",
            "created": "2023-03-09T07:20:34.318Z",
            "modified": "2023-03-09T07:20:34.318Z",
            "author_id": at_uid,
            "editor": "dataplan_qaa@ngrsoftlab.ru",
            "editor_id": at_uid,
            "published": False
        }
        resp = self.sess.post(f"{self.host}/back/dp.visualisation/reports", headers=header,
                              json=data, verify=False)
        return resp

    def visualisation_reports_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/reports", headers=header, verify=False)
        dct = json.loads(resp.text)
        global rep_id
        rep_id = dct['res'][0]['id']  # получили id отчета
        return resp

    def visualisation_reports_report_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/reports/" + str(rep_id), headers=header, verify=False)
        return resp

    def visualisation_reports_report_id_delete(self):
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.visualisation/reports/" + str(rep_id), headers=header,
                                verify=False)
        return resp

    def visualisation_visualisation_post(self):
        header = {'token': self.token}
        data = {
            "name": "TestApiVis",
            "description": "TestApiVis",
            "published": False,
            "opened": False,
            "author_id": at_uid,
            "editor_id": at_uid,
            "author": "dataplan_qaa@ngrsoftlab.ru",
            "editor": "dataplan_qaa@ngrsoftlab.ru",
            "created": "2023-03-09T07:42:21.722Z",
            "modified": "2023-03-09T07:42:21.722Z",
            "grid": [],
            "snapshot": "",
            "base_image": "",
            "settings": {}
        }
        resp = self.sess.post(f"{self.host}/back/dp.visualisation/visualisation", headers=header,
                              json=data, verify=False)
        return resp

    def visualisation_visualisation_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/visualisation", headers=header, verify=False)
        dct = json.loads(resp.text)
        global vis_id
        vis_id = dct['res'][0]['id']  # получили id визуализации
        return resp

    def visualisation_visualisation_dataseries_visualisation_id_post(self):
        header = {'token': self.token}
        data = {
            "name": "DataSerTestApi",
            "description": "DataSerTestApi",
            "element_type": 1,
            "query_id": query_id,
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
        resp = self.sess.post(f"{self.host}/back/dp.visualisation/visualisation/dataseries/" + str(vis_id),
                              headers=header, json=data, verify=False)
        return resp

    def visualisation_visualisation_types_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/visualisation/types", headers=header, verify=False)
        return resp

    def visualisation_visualisation_usage_visualisation_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/visualisation/usage/" + str(vis_id), headers=header,
                             verify=False)
        return resp

    def visualisation_visualisation_visualisation_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.visualisation/visualisation/" + str(vis_id), headers=header,
                             verify=False)
        return resp

    def visualisation_visualisation_visualisation_id_delete(self):
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.visualisation/visualisation/" + str(vis_id), headers=header,
                                verify=False)
        return resp
