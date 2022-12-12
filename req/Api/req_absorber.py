import json

import pytest
import random

from req.Helpers.base_req import BaseReq


rand = None
con_id = None
logo_id = None
rand_logo_id = None


class Absorber(BaseReq):

    def library_columns(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.absorber/library/columns", headers=header, verify=False)
        return resp

    def library_conn_type(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.absorber/library/conn_type", headers=header, verify=False)
        return resp

    def library_conn_type_id(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.absorber/library/conn_type/1", headers=header, verify=False)
        return resp

    def library_connector(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.absorber/library/connector", headers=header, verify=False)
        dct = json.loads(resp.text)
        global con_id
        con_id = dct['res'][1]['id']  # получили id коннекта
        print(con_id)
        return resp

    def library_connector_post(self, token):
        global rand
        rand = random.randint(1200, 12500)
        header = {'token': token}
        data = {
            "name": str(rand),
            "description": "",
            "published": True,
            "opened": True,
            "params": None,
            "conn_type_id": 2,
            "data": "test",
            "order_column": "src",
            "is_system": False,
            "logo_id": None,
            "mapping": [
                {
                    "storage_name": "src",
                    "event_name": "src",
                    "type": "String"
                },
                {
                    "storage_name": "spt",
                    "event_name": "spt",
                    "type": "String"
                },
                {
                    "storage_name": "dst",
                    "event_name": "dst",
                    "type": "String"
                },
                {
                    "storage_name": "dpt",
                    "event_name": "dpt",
                    "type": "String"
                }
            ],
            "author_id": 28,
            "editor_id": 28,
            "created": "2022-01-13T12:13:46.668Z",
            "modified": "2022-01-13T12:13:46.668Z"
        }
        resp = self.sess.post(f"{self.host}/back/dp.absorber/library/connector", headers=header, json=data,
                              verify=False)
        return resp

    def library_connector_put(self, token):
        header = {'token': token}
        data = {
            "id": str(con_id),
            "name": str(rand) + str(2),
            "description": "",
            "published": False,
            "opened": False,
            "author_id": None,
            "author_name": "",
            "editor_id": 28,
            "editor_name": "Снытко Татьяна",
            "created": "0001-01-01T00:00:00Z",
            "edited": "2022-02-07T15:17:11.612497Z",
            "params": None,
            "conn_type_id": 2,
            "data": "test",
            "order_column": "src",
            "is_system": False,
            "logo_id": None,
            "mapping": [
                {
                    "storage_name": "src",
                    "event_name": "src",
                    "type": "String"
                },
                {
                    "storage_name": "spt",
                    "event_name": "spt",
                    "type": "String"
                },
                {
                    "storage_name": "dst",
                    "event_name": "dst",
                    "type": "String"
                },
                {
                    "storage_name": "dpt",
                    "event_name": "dpt",
                    "type": "String"
                }
            ],
            "modified": "2022-02-08T16:36:29.335Z"
        }
        resp = self.sess.put(f"{self.host}/back/dp.absorber/library/connector", headers=header, json=data, verify=False)
        return resp

    def library_connector_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.absorber/library/connector/" + str(con_id), headers=header,
                             verify=False)
        return resp

    def library_connector_delete(self, token):
        header = {'token': token}
        resp = self.sess.delete(f"{self.host}/back/dp.absorber/library/connector/" + str(con_id), headers=header,
                                verify=False)
        return resp

    def library_logo_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.absorber/library/logo", headers=header, verify=False)
        dct = json.loads(resp.text)
        global logo_id
        logo_id = dct['res'][1]['id']  # получили id лого
        print(logo_id)
        return resp

    def library_logo_post(self, token):  # тут начались косячки проверить на сваггере, возможен баг
        global rand_logo_id
        rand_logo_id = random.randint(120000, 1250000)
        header = {'token': token}
        data = {
            "name": str(rand_logo_id),
            "editor_id": 28,
            "id": rand_logo_id,
            "is_system": False,
            "data": None
        }
        resp = self.sess.post(f"{self.host}/back/dp.absorber/library/logo", headers=header, json=data, verify=False)
        print(rand_logo_id)
        return resp

    def library_logo_put(self, token):  # тут начались косячки проверить на сваггере, возможен баг
        header = {'token': token}
        data = {"data": None,
                "edited": "2022-12-07T14:30:46.313631Z",
                "editor_id": 1238,
                "editor_name": "Трыков Никита",
                "id": 1110,
                "is_system": False,
                "name": "630244"
                }
        resp = self.sess.put(f"{self.host}/back/dp.absorber/library/logo", headers=header, json=data, verify=False)
        print(rand_logo_id)
        return resp

    def library_logo_delete(self, token):
        header = {'token': token}
        resp = self.sess.delete(f"{self.host}/back/dp.absorber/library/logo/" + str(logo_id), headers=header,
                                verify=False)
        return resp

    def source_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.absorber/source", headers=header, verify=False)
        return resp

    def source_post(self, token):
        header = {'token': token}
        data = {"author_id": 1238,
                "conn_type_id": 6,
                "data": None,
                "db_id": 108,
                "description": "TestAPI",
                "editor_id": 1238,
                "is_on": False,
                "logo": None,
                "mapping": None,
                "name": "TestAPI",
                "node": 0,
                "now": True,
                "order_column": "syncTimestamp",
                "params": None,
                "sys_info": {"ip": "127.0.0.1", "version": "1"},
                "ip": "127.0.0.1",
                "version": "1",
                "table_create_flag": 0,
                "table_name": "TestAPI",
                "workers_count": 2
                }
        resp = self.sess.put(f"{self.host}/back/dp.absorber/source", headers=header, json=data, verify=False)
        return resp
