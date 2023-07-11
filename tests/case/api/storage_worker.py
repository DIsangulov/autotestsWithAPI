import json
import random

from req.Helpers.base_req import BaseReq
from req.Api.req_storage_worker import StorageWorker
from req.Api.req_permitter import Permitter
from resourses.credentials import DbName

API_AUTO_TEST_ = "API_AUTO_TEST_"

reg_pid = []        # список, содержащий id новосозданных регулярных выражений


class StorageWorkerCase(BaseReq):

    # fixme: add _collect
    def _get_temp_reg_pid(self) -> int:
        if len(reg_pid) == 0:                               # global reg_pid # id регулярного выражения
            self.case_storage_worker_psevdo_namer_regs_post()    # если нет, создай новую
        return reg_pid[-1]

    def _permitter_sysop_add_permission_to_change_db_by_name(self, db_name):
        # Меняем пермишенны у роли, чтобы дальше смоги изменять и удалять таблицу
        # >> фактически, добавить доступ к хранилищу db_name для роли "sysop"

        db_id = self.get_db_id_by_name(db_name)

        _role_id = 5
        _rolename = "sysop"

        data = {
            # "id": _role_id,
            "name": _rolename,
            "rolename": _rolename,
            "views": [{
                # "id": 1,
                # "name": "Администрирование",
                "ui_part": "administration",
                "read": True,
                "write": True,
                # "disabled": ["read"]
            }, {
                # "id": 2,
                # "name": "Данные",
                "ui_part": "data",
                "read": True,
                "write": True,
                # "disabled": ["read"]
            }, {
                # "id": 3,
                # "name": "Аналитика",
                "ui_part": "analytics",
                "read": True,
                "write": True,
                # "disabled": ["read"]
            }, {
                # "id": 4,
                # "name": "xBA",
                "ui_part": "xba",
                "read": True,
                "write": True,
                # "disabled": ["read"]
            }, {
                # "id": 5,
                # "name": "Role Mining",
                "ui_part": "rm",
                "read": True,
                "write": True,
                # "disabled": ["read"]
            }],
            "dbs": [{
                "id": db_id,
                "name": DbName.API_TEST_DB1,
                "db_id": 0,
                "select": True,
                "update": True
            }],
            # "report_id": None
        }

        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': '2'})
        resp = req.permitter_roles_editor_roles_id_put(_role_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # resp = self.sess.put(f"{self.host}/back/dp.permitter/roles_editor/roles/{_role_id}", headers=header, json=data, verify=False)

    def case_storage_worker_ask_one_sql_post(self):
        req = StorageWorker(self.sess, self.host)
        picker_tables_id = self.get_db_id_by_name(DbName.picker_tables)
        # FIXME: прям инъекцию подцепить можно суда?
        data = {"base_id": picker_tables_id, "base_name": "picker_tables",
                "statements": "SELECT * FROM ad_users_ngr LIMIT 50;",
                "regs": False,
                ""
                "params": []}
        resp = req.storage_worker_ask_one_sql_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_ask_plain_sql_post(self):
        req = StorageWorker(self.sess, self.host)
        picker_tables_id = self.get_db_id_by_name(DbName.picker_tables)
        data = {"base_id": picker_tables_id, "tab_name": "ad_users_ngr", "columns":
            [{"name": "*", "type": "LowCardinality(String)"}],
                "groupby": [], "filters": [], "agregators": [],
                "limit": 50, "base_name": "picker_tables", "regs": False}
        resp = req.storage_worker_ask_plain_sql_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_import_rules_get(self):
        req = StorageWorker(self.sess, self.host)
        resp = req.storage_worker_import_rules_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_psevdo_namer_regs_get(self):
        req = StorageWorker(self.sess, self.host)
        resp = req.storage_worker_psevdo_namer_regs_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_psevdo_namer_regs_post(self):
        req = StorageWorker(self.sess, self.host)
        str_rand_num = str(random.randint(100, 999))
        data = {
            "rus": API_AUTO_TEST_ + str_rand_num,   # название на русском?
            "reg": "1",                             # сам рег шаблон
            "stages": "1",
            "postfix": "1",
            "state": False,
            "is_on": False,
            "author": self.get_self_user_id()           # автором является инициатор
        }

        resp = req.storage_worker_psevdo_namer_regs_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

        dct = json.loads(resp.text)
        reg_pid.append(int(dct['res']))  # global reg_pid

    def case_storage_worker_psevdo_namer_regs_pid_get(self):
        req = StorageWorker(self.sess, self.host)
        _reg_pid = self._get_temp_reg_pid()
        resp = req.storage_worker_psevdo_namer_regs_pid_get(_reg_pid)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_psevdo_namer_regs_pid_delete(self):
        req = StorageWorker(self.sess, self.host)

        # FIXME: удалять элемент из списка reg_pid после удачного получения 'resp'
        _reg_pid = self._get_temp_reg_pid()

        resp = req.storage_worker_psevdo_namer_regs_pid_delete(_reg_pid)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_show_base_db_name_get(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.picker_tables      # FIXME:
        resp = req.storage_worker_show_base_db_name_get(db_name)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_statistics_db_event_stats_db_name_flag_post(self):
        req = StorageWorker(self.sess, self.host)

        db_name = DbName.picker_tables  # FIXME:
        flag = 0                        # FIXME: magic
        data = {"timezone": "Europe/Moscow"}
        resp = req.storage_worker_statistics_db_event_stats_db_name_flag_post(db_name, flag, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_statistics_db_one_tab_stats_db_name_tab_name_get(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.picker_tables  # FIXME:
        tab_name = "ad_groups_ngr"      # FIXME:    tab_name rel db_name
        resp = req.storage_worker_statistics_db_one_tab_stats_db_name_tab_name_get(db_name, tab_name)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_statistics_db_search_post(self):
        req = StorageWorker(self.sess, self.host)
        data = {
            "database_name": "picker_tables",   # FIXME:
            # "pattern": "pattern"              # fixme
            "use_regexps": True
        }
        resp = req.storage_worker_statistics_db_search_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_statistics_db_stats_dbname_get(self):
        req = StorageWorker(self.sess, self.host)
        dbname = DbName.picker_tables
        resp = req.storage_worker_statistics_db_stats_dbname_get(dbname)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_statistics_db_tabs_event_stats_db_name_tab_name_flag_post(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.picker_tables  # FIXME:
        tab_name = "ad_groups_ngr"      # FIXME: tab_name rel db_name
        flag = 0                        # FIXME: magic?
        data = {"timezone": "Europe/Moscow"}
        resp = req.storage_worker_statistics_db_tabs_event_stats_db_name_tab_name_flag_post(db_name, tab_name, flag, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_statistics_db_tabs_stats_dbname_get(self):
        req = StorageWorker(self.sess, self.host)
        dbname = DbName.picker_tables
        resp = req.storage_worker_statistics_db_tabs_stats_dbname_get(dbname)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_statistics_storage_search_post(self):
        req = StorageWorker(self.sess, self.host)
        data = {
            "database_name": "picker_tables",
            "table": "ad_users_ngr",
            "filter_columns": ["mail"],
            "select_columns": ["mail"],
            "pattern": "",
            "use_regexps": False
        }
        resp = req.storage_worker_statistics_storage_search_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_statistics_test_selection_post(self):
        req = StorageWorker(self.sess, self.host)
        data = {"database_name": "picker_tables", "table_name": "ad_users_ngr", "name": "name"}
        resp = req.storage_worker_statistics_test_selection_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_storage_db_get(self):
        req = StorageWorker(self.sess, self.host)
        resp = req.storage_worker_storage_db_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_storage_db_put(self):
        req = StorageWorker(self.sess, self.host)
        data = {
            "base_name": DbName.API_TEST_DB1,
            "description": f"{DbName.API_TEST_DB1} +put"
        }
        resp = req.storage_worker_storage_db_put(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_storage_db_post(self):
        req = StorageWorker(self.sess, self.host)
        data = {
            "base_name": DbName.API_TEST_DB1,
            "description": f"..for api test things"
        }
        resp = req.storage_worker_storage_db_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # доступ на изменение хранилища API_TEST_DB1
        self._permitter_sysop_add_permission_to_change_db_by_name(DbName.API_TEST_DB1)

    def case_storage_worker_storage_db_delete(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.API_TEST_DB1
        resp = req.storage_worker_storage_db_delete(db_name)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_storage_import_csv_db_name_table_name_post(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.picker_tables  # FIXME:
        table_name = "ad_groups_ngr"    # FIXME: table_name rel db_name
        data = {"data": None}
        resp = req.storage_worker_storage_import_csv_db_name_table_name_post(db_name, table_name, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_storage_import_json_db_name_table_name_post(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.picker_tables  # FIXME:
        table_name = "ad_groups_ngr"    # FIXME: table_name rel db_name
        data = {"data": None}
        resp = req.storage_worker_storage_import_json_db_name_table_name_post(db_name, table_name, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_storage_supported_engines_get(self):
        req = StorageWorker(self.sess, self.host)
        resp = req.storage_worker_storage_supported_engines_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_storage_supported_types_get(self):
        req = StorageWorker(self.sess, self.host)
        resp = req.storage_worker_storage_supported_types_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_storage_table_columns_db_name_tab_name_get(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.picker_tables  # FIXME:
        tab_name = "ad_groups_ngr"      # FIXME: tab_name rel db_name
        resp = req.storage_worker_storage_table_columns_db_name_tab_name_get(db_name, tab_name)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    # FIXME: падает GL
    # Неверный синтаксис запроса или ошибка соединения (c)
    # .."msg": "Ошибка создания view"}}
    def case_storage_worker_storage_table_columns_db_name_table_name_post(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.picker_tables  # FIXME:
        table_name = "ad_groups_ngr"    # FIXME: table_name rel db_name
        data = [
            {"name": "Nopt", "dtype": "DateTime", "alias": "псевдоним", "mask_it": False},
            {"name": "Npqroduct", "alias": "", "table_name": "ad_groups_ngr", "database_name": "picker_tables", "dtype": "String", "mask_it": False},
            {"name": "Ntype", "alias": "", "table_name": "ad_groups_ngr", "database_name": "picker_tables", "dtype": "String", "mask_it": False},
            {"name": "opt", "alias": "", "table_name": "ad_groups_ngr", "database_name": "picker_tables", "dtype": "DateTime", "mask_it": False},
            {"name": "pqroduct", "alias": "", "table_name": "ad_groups_ngr", "database_name": "picker_tables", "dtype": "String", "mask_it": False},
            {"name": "type", "alias": "", "table_name": "ad_groups_ngr", "database_name": "picker_tables", "dtype": "UInt32", "mask_it": False}
        ]
        resp = req.storage_worker_storage_table_columns_db_name_table_name_post(db_name, table_name, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

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

    # def storage_worker_storage_table_table_db_name_table_name(self):
    #     header = {'token': self.token}
    #     data = {"name": "five", "type": "Int8"}
    #     resp = self.sess.post(f"{self.host}/back/dp.storage_worker/storage/table/API_TEST_DB1/API_TEST_TABLE",
    #                           headers=header, json=data, verify=False)
    #     return resp

    def case_storage_worker_storage_table_db_name_table_name_ttl_get(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.picker_tables  # FIXME:
        table_name = "ad_groups_ngr"    # FIXME: table_name rel db_name
        resp = req.storage_worker_storage_table_db_name_table_name_ttl_get(db_name, table_name)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_storage_table_db_name_table_name_count_get(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.picker_tables  # FIXME:
        table_name = "ad_groups_ngr"    # FIXME: table_name rel db_name
        count = 2                       # number of rows limit
        resp = req.storage_worker_storage_table_db_name_table_name_count_get(db_name, table_name, count)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)
