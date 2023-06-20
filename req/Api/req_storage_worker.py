import json
import random

from req.Helpers.base_req import BaseReq

reg_pid = []        # список, содержащий id новосозданных регулярных выражений
db_id = None


class StorageWorker(BaseReq):

    def _get_user_id(self) -> int:
        """Возвращает 'user_id' текущего пользователя"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/profile", headers=header, verify=False)
        dct = json.loads(resp.text)
        return dct['res']['user_id']

    def _get_temp_reg_pid(self) -> int:
        if len(reg_pid) == 0:                               # global reg_pid
            self.storage_worker_psevdo_namer_regs_post()    # если нет, создай новую
        return reg_pid[-1]

    # def peopler_users_at_uid_get(self):
    #     header = {'token': self.token}
    #     resp = self.sess.get(f"{self.host}/back/dp.peopler/users", headers=header, verify=False)
    #     name = 'dataplan_qaa@ngrsoftlab.ru'
    #     users = json.loads(resp.text)['res']
    #     uid = next((user for user in users if user['name'] == name), None)
    #     global at_uid
    #     at_uid = uid['id']
    #     print(at_uid)
    #     return resp

    def _id_picker_tables_get(self) -> int:  # забираем id таблицы picker_table
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/db", headers=header, verify=False)
        json_data = json.loads(resp.text)
        pt_id = None
        for item in json_data['res']:
            if item['name'] == 'picker_tables':
                pt_id = item['id']
        # print(f"pt_id = {pt_id}")
        return pt_id

    def storage_worker_ask_one_sql_post(self):

        picker_tables_id = self._id_picker_tables_get()
        header = {'token': self.token}

        # FIXME: прям инъекцию подцепить можно суда?
        data = {"base_id": picker_tables_id, "base_name": "picker_tables",
                "statements": "SELECT * FROM ad_users_ngr LIMIT 50;",
                "regs": False,
                ""
                "params": []}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/ask_one_sql", headers=header, json=data, verify=False)
        return resp

    def storage_worker_ask_plain_sql_post(self):

        picker_tables_id = self._id_picker_tables_get()
        header = {'token': self.token}

        data = {"base_id": picker_tables_id, "tab_name": "ad_users_ngr", "columns":
            [{"name": "*", "type": "LowCardinality(String)"}],
                "groupby": [], "filters": [], "agregators": [],
                "limit": 50, "base_name": "picker_tables", "regs": False}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/ask_plain_sql", headers=header, json=data, verify=False)
        return resp

    def storage_worker_import_rules_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/import_rules", headers=header, verify=False)
        return resp

    def storage_worker_psevdo_namer_regs_post(self):
        """process POST req for creating new regexp"""
        rand = random.randint(0, 999)
        header = {'token': self.token}
        data = {
            "rus": "auto_testApi_" + str(rand),     # название на русском
            "reg": "1",                             # сам рег шаблон
            "stages": "1",
            "postfix": "1",
            "state": False,
            "is_on": False,
            "author": self._get_user_id()           # автором является инициатор
        }

        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/psevdo_namer/regs", headers=header, json=data, verify=False)

        dct = json.loads(resp.text)
        reg_pid.append(int(dct['res']))  # global reg_pid

        return resp

    def storage_worker_psevdo_namer_regs_get(self):
        """process GET req for getting list of regexps"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/psevdo_namer/regs", headers=header, verify=False)
        return resp

    def storage_worker_psevdo_namer_regs_pid_get(self):

        _reg_pid = self._get_temp_reg_pid()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/psevdo_namer/regs/" + str(_reg_pid), headers=header, verify=False)
        return resp


    def storage_worker_psevdo_namer_regs_pid_delete(self):

        # FIXME: удалять элемент из списка reg_pid
        _reg_pid = self._get_temp_reg_pid()

        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.storage_worker/psevdo_namer/regs/" + str(_reg_pid), headers=header, verify=False)
        return resp

    def storage_worker_show_base_db_name_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/show_base/picker_tables", headers=header, verify=False)
        return resp

    def storage_worker_statistics_db_event_stats_db_name_flag_post(self):
        header = {'token': self.token}
        data = {"timezone": "Europe/Moscow"}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/db_event_stats/picker_tables/0", headers=header, json=data, verify=False)
        return resp

    def storage_worker_statistics_db_one_tab_stats_db_name_tab_name_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/statistics/db_one_tab_stats/picker_tables"
                             f"/ad_groups_ngr", headers=header, verify=False)
        return resp

    def storage_worker_statistics_db_search_post(self):
        header = {'token': self.token}
        data = {
            "database_name": "picker_tables",
            "use_regexps": True
        }
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/db_search", headers=header, json=data, verify=False)
        return resp

    def storage_worker_statistics_db_status_dbname_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/statistics/db_stats/picker_tables", headers=header, verify=False)
        return resp

    def storage_worker_statistics_db_tabs_event_stats_db_name_tab_name_flag_post(self):
        header = {'token': self.token}
        data = {"timezone": "Europe/Moscow"}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/db_tabs_event_stats/picker_tables/ad_groups_ngr/0", headers=header, json=data, verify=False)
        return resp

    def storage_worker_statistics_db_tabs_stats_dbname_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/statistics/db_tabs_stats/picker_tables", headers=header, verify=False)
        return resp

    def storage_worker_statistics_storage_search_post(self):
        header = {'token': self.token}
        data = {
            "database_name": "picker_tables",
            "table": "ad_users_ngr",
            "filter_columns": ["mail"],
            "select_columns": ["mail"],
            "pattern": "",
            "use_regexps": False
        }
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/storage_search", headers=header, json=data, verify=False)
        return resp

    def storage_worker_statistics_test_selection_post(self):
        header = {'token': self.token}
        data = {"database_name": "picker_tables", "table_name": "ad_users_ngr", "name": "name"}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/test_selection", headers=header, json=data, verify=False)
        return resp

    def storage_worker_storage_db_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/db", headers=header, verify=False)
        dct = json.loads(resp.text)
        global db_id
        db_id = dct['res'][0]['id']  # получили id базы данных
        # print(f"db_id = {db_id}")
        return resp

    def storage_worker_storage_db_post(self):
        header = {'token': self.token}
        data = {"base_name": "API_TEST_DB1", "description": "API_TEST_DB1"}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/storage/db", headers=header, json=data, verify=False)
        return resp

    def permitter_roles_editor_roles_for_storage_worker_put(self):
        # Меняем пермишенны у роли, чтобы дальше смоги изменять и удалять таблицу
        header = {'token': self.token, 'ui': str(2)}
        data = {
            "id": 5,
            "name": "sysop",
            "rolename": "sysop",
            "views": [{
                "id": 1,
                "name": "Администрирование",
                "ui_part": "administration",
                "read": True,
                "write": True,
                "disabled": ["read"]
            }, {
                "id": 2,
                "name": "Данные",
                "ui_part": "data",
                "read": True,
                "write": True,
                "disabled": ["read"]
            }, {
                "id": 3,
                "name": "Аналитика",
                "ui_part": "analytics",
                "read": True,
                "write": True,
                "disabled": ["read"]
            }, {
                "id": 4,
                "name": "xBA",
                "ui_part": "xba",
                "read": True,
                "write": True,
                "disabled": ["read"]
            }, {
                "id": 5,
                "name": "Role Mining",
                "ui_part": "rm",
                "read": True,
                "write": True,
                "disabled": ["read"]
            }],
            "dbs": [{
                "id": db_id,
                "name": "API_TEST_DB1",
                "db_id": 0,
                "select": True,
                "update": True
            }],
            "report_id": None
        }
        resp = self.sess.put(f"{self.host}/back/dp.permitter/roles_editor/roles/5", headers=header, json=data,
                             verify=False)
        return resp

    def storage_worker_storage_db_put(self):
        header = {'token': self.token}
        data = {"base_name": "API_TEST_DB1", "description": "API_TEST_DB11"}
        resp = self.sess.put(f"{self.host}/back/dp.storage_worker/storage/db", headers=header, json=data, verify=False)
        return resp

    def storage_worker_storage_db_delete(self):
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.storage_worker/storage/db/API_TEST_DB1", headers=header, verify=False)
        return resp

    def storage_worker_storage_import_csv_db_name_table_name_post(self):
        header = {'token': self.token}
        data = {"data": None}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/storage/import_csv/picker_tables/ad_groups_ngr", headers=header, json=data, verify=False)
        return resp

    def storage_worker_storage_import_json_db_name_table_name_post(self):
        header = {'token': self.token}
        data = {"data": None}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/storage/import_json/picker_tables/ad_groups_ngr", headers=header, json=data, verify=False)
        return resp

    def storage_worker_storage_supported_engines_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/supported_engines", headers=header, verify=False)
        return resp

    def storage_worker_storage_supported_types_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/supported_types", headers=header, verify=False)
        return resp

    def storage_worker_storage_table_columns_db_name_tab_name_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/table/columns/picker_tables/ad_groups_ngr", headers=header, verify=False)
        return resp

    # FIXME: падает GL
    # Неверный синтаксис запроса или ошибка соединения (c)
    # .."msg": "Ошибка создания view"}}
    def storage_worker_storage_table_columns_db_name_table_name_post(self):
        header = {'token': self.token}

        data = [
            {"name": "Nopt", "dtype": "DateTime", "alias": "псевдоним", "mask_it": False},
            {"name": "Npqroduct", "alias": "", "table_name": "ad_groups_ngr", "database_name": "picker_tables", "dtype": "String", "mask_it": False},
            {"name": "Ntype", "alias": "", "table_name": "ad_groups_ngr", "database_name": "picker_tables", "dtype": "String", "mask_it": False},
            {"name": "opt", "alias": "", "table_name": "ad_groups_ngr", "database_name": "picker_tables", "dtype": "DateTime", "mask_it": False},
            {"name": "pqroduct", "alias": "", "table_name": "ad_groups_ngr", "database_name": "picker_tables", "dtype": "String", "mask_it": False},
            {"name": "type", "alias": "", "table_name": "ad_groups_ngr", "database_name": "picker_tables", "dtype": "UInt32", "mask_it": False}
        ]

        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/storage/table/columns/picker_tables/ad_groups_ngr", headers=header, json=data, verify=False)
        return resp

    # def storage_worker_storage_table_db_name_post(self):
    #     header = {'token': self.token}
    #     data = {"auto_read": True, "columns":
    #         [{"name": "one", "type": "DateTime"},
    #          {"name": "two", "type": "UInt64"},
    #          {"name": "three", "type": "String"}],
    #             "engine": "MergeTree", "order_by":
    #                 "one", "partition_by": "tuple()",
    #             "tab_name": "API_TEST_DB1", "ttl": 0, "ttl_base": ""}
    #     resp = self.sess.post(f"{self.host}/back/dp.storage_worker/storage/table/API_TEST_DB1",
    #                           headers=header, json=data, verify=False)
    #     return resp
    #
    # def storage_worker_storage_table_table_db_name_table_name(self):
    #     header = {'token': self.token}
    #     data = {"name": "five", "type": "Int8"}
    #     resp = self.sess.post(f"{self.host}/back/dp.storage_worker/storage/table/API_TEST_DB1/API_TEST_TABLE",
    #                           headers=header, json=data, verify=False)
    #     return resp

    def storage_worker_storage_table_db_name_table_name_ttl_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/table/picker_tables/ad_groups_ngr/ttl", headers=header, verify=False)
        return resp

    def storage_worker_storage_table_db_name_table_name_count_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/table/picker_tables/ad_groups_ngr/2", headers=header, verify=False)
        return resp
