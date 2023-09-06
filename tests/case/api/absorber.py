import json
import os
import random
import base64

from req.Helpers.user_session import UserSession
from req.Api.req_absorber import Absorber
from resourses.constants import DB_picker_tables, API_AUTO_TEST_

logo_id = set()
source_id = set()      # 'id' источника данных
connector_id = set()   # 'id' коннектора


class ConnType:
    t_default = 1
    t_syslog = 2
    t_beats = 3
    t_jdbc = 4
    t_python = 5
    t_python_ad = 6
    t_tcp_udp = 7
    t_python_clickhouse = 8


class AbsorberCase(UserSession):

    def _collect_source_id(self):
        resp = Absorber(self.sess, self.host).absorber_source_get()
        assert resp.status_code == 200, f"assert::absorber_source_get, failed. status_code: {resp.status_code}, text: {resp.text}"

        source_info_rows = json.loads(resp.text)['res']
        for _row in source_info_rows:
            if str(_row['name']).startswith(API_AUTO_TEST_):
                source_id.add(_row['id'])

    def _get_source_id(self) -> int:
        """get from global source_id: API_AUTO_TEST_x"""
        if len(source_id) == 0:
            self._collect_source_id()

        if len(source_id) == 0:                                 # global source_id
            r_new_source = self.case_absorber_source_post()     # если нет источника - создай новый
            new_source_id = json.loads(r_new_source.text)['res']
            return int(new_source_id)

        return source_id.pop()

    def _collect_connector_id(self):
        resp = Absorber(self.sess, self.host).absorber_library_connector_get()
        assert resp.status_code == 200, f"assert::absorber_library_connector_get, failed. status_code: {resp.status_code}, text: {resp.text}"

        connector_info_rows = json.loads(resp.text)['res']
        for _row in connector_info_rows:
            if str(_row['name']).startswith(API_AUTO_TEST_):
                connector_id.add(_row['id'])

    def _get_connector_id(self) -> int:
        if len(connector_id) == 0:
            self._collect_connector_id()

        if len(connector_id) == 0:                                          # global connector_id
            r_new_connector = self.case_absorber_library_connector_post()   # если нет - создай новый
            new_connector_id = json.loads(r_new_connector.text)['res']
            return int(new_connector_id)

        return connector_id.pop()

    def _collect_logo_id(self):
        resp = Absorber(self.sess, self.host).absorber_library_logo_get()
        assert resp.status_code == 200, f"assert::absorber_library_logo_get, failed. status_code: {resp.status_code}, text: {resp.text}"

        logo_info_rows = json.loads(resp.text)['res']
        for _row in logo_info_rows:
            if str(_row['name']).startswith(API_AUTO_TEST_):
                logo_id.add(_row['id'])

    def _get_logo_id(self) -> int:
        if len(logo_id) == 0:
            self._collect_logo_id()

        if len(logo_id) == 0:                                       # global logo_id
            r_new_logo = self.case_absorber_library_logo_post()     # если нет - создай новый
            new_logo_id = json.loads(r_new_logo.text)['res']
            return int(new_logo_id)

        return logo_id.pop()

    def case_absorber_library_columns_get(self):
        req = Absorber(self.sess, self.host)
        resp = req.absorber_library_columns_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_absorber_library_conn_type_get(self):
        req = Absorber(self.sess, self.host)
        resp = req.absorber_library_conn_type_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_absorber_library_conn_type_id_get(self):
        req = Absorber(self.sess, self.host)

        # << [GET] /library/conn_type
        conn_type_id = ConnType.t_syslog
        resp = req.absorber_library_conn_type_id_get(conn_type_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_absorber_library_connector_get(self):
        req = Absorber(self.sess, self.host)
        resp = req.absorber_library_connector_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_absorber_library_connector_put(self):
        req = Absorber(self.sess, self.host)

        str_rand_num = str(random.randint(1000, 9999))
        _con_id = self._get_connector_id()
        self_user_id = self.get_self_user_id()

        data = {
            "id": str(_con_id),
            "name": API_AUTO_TEST_ + "changed_" + str_rand_num,
            "description": API_AUTO_TEST_ + "changed desc",
            "published": False,
            "opened": False,
            # "author_id": None,
            # "author_name": "",
            "editor_id": self_user_id,
            # "editor_name": self.username,
            # "created": "0001-01-01T00:00:00Z",
            # "edited": "2022-02-07T15:17:11.612497Z",
            "params": None,
            "conn_type_id": 2,
            "data": "test",     # fixme: <<<<
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
            # "modified": "2022-02-08T16:36:29.335Z"
        }
        resp = req.absorber_library_connector_put(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_absorber_library_connector_post(self):
        req = Absorber(self.sess, self.host)

        rand_num = random.randint(1000, 9999)

        self_user_id = self.get_self_user_id()      # получить свой 'user_id'

        data = {
            "name": API_AUTO_TEST_ + str(rand_num),
            "description": API_AUTO_TEST_ + "description",
            "published": True,
            "opened": True,
            "params": None,
            "conn_type_id": ConnType.t_syslog,
            "data": "test",                                     # FIXME: <<<<
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
            "author_id": self_user_id,
            # "editor_id": self_user_id,
            # "created": "2022-01-13T12:13:46.668Z",
            # "modified": "2022-01-13T12:13:46.668Z"
        }

        resp = req.absorber_library_connector_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_absorber_library_connector_id_get(self):
        req = Absorber(self.sess, self.host)

        con_id = self._get_connector_id()
        resp = req.absorber_library_connector_id_get(con_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_absorber_library_connector_id_delete(self):
        req = Absorber(self.sess, self.host)

        con_id = self._get_connector_id()
        resp = req.absorber_library_connector_id_delete(con_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # TODO: [POST] /back/dp.absorber/library/external/{type}
    def case_absorber_library_external_driver_post(self):
        req = Absorber(self.sess, self.host)

        _type = "driver"
        file = None
        resp = req.absorber_library_external_type_post(_type, file)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        print(resp.text)

    # TODO: [POST] /back/dp.absorber/library/external/{type}
    def case_absorber_library_external_pattern_post(self):
        req = Absorber(self.sess, self.host)

        _type = "pattern"
        file = None
        resp = req.absorber_library_external_type_post(_type, file)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        print(resp.text)

    def case_absorber_library_logo_get(self):
        req = Absorber(self.sess, self.host)

        resp = req.absorber_library_logo_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_absorber_library_logo_put(self):
        req = Absorber(self.sess, self.host)

        str_rand_num = str(random.randint(1000, 9999))
        _logo_id = self._get_logo_id()
        self_user_id = self.get_self_user_id()

        file_path = os.path.dirname(__file__) + "/../../Files/img/d_01.jpg"
        with open(file_path, 'rb') as f:
            bytes_image = f.read()
        sample_image = base64.b64encode(bytes_image).decode("utf8")

        data = {
            "name": API_AUTO_TEST_ + "changed_" + str_rand_num,
            "id": _logo_id,
            "data": f"data:image/jpeg;base64," + sample_image,
            "editor_id": self_user_id,
            # "editor_name": "Тестов Датаплан",
            # "is_system": False,
            # "edited": "2022-12-07T14:30:46.313631Z",
        }

        resp = req.absorber_library_logo_put(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_absorber_library_logo_post(self):
        req = Absorber(self.sess, self.host)

        str_rand_num = str(random.randint(1000, 9999))
        self_user_id = self.get_self_user_id()

        file_path = os.path.dirname(__file__) + "/../../Files/img/d_00.jpg"
        with open(file_path, 'rb') as f:
            bytes_image = f.read()
        sample_image = base64.b64encode(bytes_image).decode("utf8")

        data = {
            "name": API_AUTO_TEST_ + str_rand_num,
            "editor_id": self_user_id,
            # "id": rand_logo_id,
            # "is_system": False,
            "data": f"data:image/jpeg;base64," + sample_image,
        }

        resp = req.absorber_library_logo_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_absorber_library_logo_id_get(self):
        req = Absorber(self.sess, self.host)

        _logo_id = self._get_logo_id()
        resp = req.absorber_library_logo_id_get(_logo_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_absorber_library_logo_delete(self):
        req = Absorber(self.sess, self.host)

        _logo_id = self._get_logo_id()
        resp = req.absorber_library_logo_delete(_logo_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_absorber_source_get(self):
        req = Absorber(self.sess, self.host)

        resp = req.absorber_source_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_absorber_source_put(self):
        req = Absorber(self.sess, self.host)

        str_rand_num = str(random.randint(1000, 9999))
        _source_id = self._get_source_id()
        self_user_id = self.get_self_user_id()
        db_picker_tables = self.get_db_id_by_name(DB_picker_tables.name)

        file_path = os.path.dirname(__file__) + "/../../Files/img/d_01.jpg"
        with open(file_path, 'rb') as f:
            bytes_image = f.read()
        sample_image = base64.b64encode(bytes_image).decode("utf8")

        data = {
            "now": True,
            "name": f"{API_AUTO_TEST_}changed_{str_rand_num}",
            "description": f"{API_AUTO_TEST_}description",
            "editor_id": self_user_id,
            "author_id": self_user_id,
            "node": 0,
            "conn_type_id": ConnType.t_syslog,
            "workers_count": 2,
            "is_on": True,
            "debug_is_on": True,
            "monitoring_interval": 10,
            "monitoring_metric": "hour",
            "logo": f"data:image/jpeg;base64," + sample_image,
            "data": "",
            "params": None,
            "sys_info": {
                "ip": "127.0.0.1",
                "version": "1",
                "last_data_state": 0,
                "last_data_time": None,
                "log_last_executed": ""
            },
            "mapping_list": [
                {
                    "tag": "tag1",
                    "order_column": "TimeStamp",
                    "mapping": [
                        {
                            "storage_name": "TimeStamp",
                            "event_name": "name",
                            "type": "DateTime"
                        }
                    ],
                    "db_id": db_picker_tables,
                    "table_name": "ad_users_ngr",
                    "table_create_flag": 3
                }
            ],
            "id": _source_id
        }

        resp = req.absorber_source_put(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_absorber_source_post(self):
        req = Absorber(self.sess, self.host)

        str_rand_num = str(random.randint(100, 999))
        self_user_id = self.get_self_user_id()
        db_picker_tables = self.get_db_id_by_name(DB_picker_tables.name)

        file_path = os.path.dirname(__file__) + "/../../Files/img/d_01.jpg"
        with open(file_path, 'rb') as f:
            bytes_image = f.read()
        sample_image = base64.b64encode(bytes_image).decode("utf8")

        data = {
            "now": True,
            "name": API_AUTO_TEST_ + str_rand_num,
            "description": "",
            "editor_id": self_user_id,
            "author_id": self_user_id,
            "node": 0,
            "conn_type_id": ConnType.t_default,
            "workers_count": 2,
            "is_on": True,
            "debug_is_on": True,
            "monitoring_interval": 10,
            "monitoring_metric": "hour",
            "logo": f"data:image/jpeg;base64," + sample_image,
            "data": "",
            "params": [],
            "sys_info": {
                "ip": "127.0.0.1",
                "version": "1"
            },
            "mapping_list": [
                {
                    "mapping": [
                        {
                            "event_name": "name",
                            "storage_name": "TimeStamp",
                            "type": "DateTime"
                        }
                    ],
                    "order_column": "TimeStamp",
                    "db_id": db_picker_tables,
                    "table_name": "ad_users_ngr",
                    "table_create_flag": 1,
                    "tag": "tag1"
                }
            ]
        }

        resp = req.absorber_source_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_absorber_source_id_get(self):
        req = Absorber(self.sess, self.host)

        _source_id = self._get_source_id()
        resp = req.absorber_source_id_get(_source_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_absorber_source_id_delete(self):
        req = Absorber(self.sess, self.host)

        _source_id = self._get_source_id()
        resp = req.absorber_source_id_delete(_source_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # FIXME: код 400, {"error":{"code":400,"description":"code: 400,
    #  message: bad ssh commands","msg":"Ошибка выполнения ssh команд"}}
    def case_absorber_source_id_debug_get(self):
        # {"error":{"code":400,"msg":"Режим отладки выключен"}}
        req = Absorber(self.sess, self.host)

        # _source_id = self._get_source_id()
        _source_id = 105
        resp = req.absorber_source_id_debug_get(_source_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_absorber_source_id_log_get(self):
        # DAT-5372
        req = Absorber(self.sess, self.host)

        _source_id = self._get_source_id()
        resp = req.absorber_source_id_log_get(_source_id)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # 200: {"res":""}
        # 200: {"res":"--no errors, empty log--"}
        # 200: {"res":"Log: no data\nError: No errors"}

    # __del__
    def all_api_auto_test_entity_delete(self):
        delete_req = Absorber(self.sess, self.host)
        self._collect_source_id()
        while len(source_id) > 0:
            delete_req.absorber_source_id_delete(source_id.pop())

        self._collect_connector_id()
        while len(connector_id) > 0:
            delete_req.absorber_library_connector_id_delete(connector_id.pop())

        self._collect_logo_id()
        while len(logo_id) > 0:
            delete_req.absorber_library_logo_delete(logo_id.pop())
