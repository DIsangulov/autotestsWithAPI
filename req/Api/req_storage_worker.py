import json
import random

from req.Helpers.base_req import BaseReq
from resourses.credentials import DbName

reg_pid = []        # список, содержащий id новосозданных регулярных выражений


class StorageWorker(BaseReq):

    def _get_temp_reg_pid(self) -> int:
        if len(reg_pid) == 0:                               # global reg_pid # id регулярного выражения
            self.storage_worker_psevdo_namer_regs_post()    # если нет, создай новую
        return reg_pid[-1]

    # FIXME: обращение к api соседнего класса
    def permitter_roles_editor_roles_for_storage_worker_put(self):
        # Меняем пермишенны у роли, чтобы дальше смоги изменять и удалять таблицу

        db_id = self.get_db_id_by_name(DbName.API_TEST_DB1)

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
                "name": DbName.API_TEST_DB1,
                "db_id": 0,
                "select": True,
                "update": True
            }],
            "report_id": None
        }
        resp = self.sess.put(f"{self.host}/back/dp.permitter/roles_editor/roles/5", headers=header, json=data, verify=False)
        return resp

    def storage_worker_ask_one_sql_post(self):
        """process POST req with raw sql ask for executing it"""

        picker_tables_id = self.get_db_id_by_name(DbName.picker_tables)
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
        """process POST req with "plain-constructed" sql ask params for executing it"""

        picker_tables_id = self.get_db_id_by_name(DbName.picker_tables)
        header = {'token': self.token}

        data = {"base_id": picker_tables_id, "tab_name": "ad_users_ngr", "columns":
            [{"name": "*", "type": "LowCardinality(String)"}],
                "groupby": [], "filters": [], "agregators": [],
                "limit": 50, "base_name": "picker_tables", "regs": False}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/ask_plain_sql", headers=header, json=data, verify=False)
        return resp

    # TODO: [GET] /back/dp.storage_worker/backups

    # TODO: [POST] /back/dp.storage_worker/backups/table/{db_name}/{table_name}

    # TODO: [GET] /back/dp.storage_worker/backups/{id}

    # TODO: [DELETE] /back/dp.storage_worker/backups/{id}

    # TODO: [GET] /back/dp.storage_worker/backups/{id}/download

    # TODO: [POST] /back/dp.storage_worker/backups/{id}/restore

    # TODO: [POST] /back/dp.storage_worker/backups/{type}/upload

    def storage_worker_import_rules_get(self):
        """process GET to return db and tables import restrictions info"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/import_rules", headers=header, verify=False)
        return resp

    def storage_worker_psevdo_namer_regs_get(self):
        """process GET req for getting list of regexps"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/psevdo_namer/regs", headers=header, verify=False)
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
            "author": self.get_self_user_id()           # автором является инициатор
        }

        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/psevdo_namer/regs", headers=header, json=data, verify=False)

        dct = json.loads(resp.text)
        reg_pid.append(int(dct['res']))  # global reg_pid

        return resp

    def storage_worker_psevdo_namer_regs_pid_get(self):
        """process GET req for getting regexp with id=pid"""
        _reg_pid = self._get_temp_reg_pid()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/psevdo_namer/regs/{_reg_pid}", headers=header, verify=False)
        return resp

    # TODO: [PUT] /back/dp.storage_worker/psevdo_namer/regs/{pid}

    def storage_worker_psevdo_namer_regs_pid_delete(self):
        """process DELETE req for deleting pid regexp"""

        # FIXME: удалять элемент из списка reg_pid после удачного получения 'resp'
        _reg_pid = self._get_temp_reg_pid()

        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.storage_worker/psevdo_namer/regs/{_reg_pid}", headers=header, verify=False)
        return resp

    def storage_worker_show_base_db_name_get(self):
        """process GET req for getting the DB structure"""
        db_name = DbName.picker_tables      # FIXME:
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/show_base/{db_name}", headers=header, verify=False)
        return resp

    def storage_worker_statistics_db_event_stats_db_name_flag_post(self):
        """process POST req for getting one db inserts dynamic"""
        db_name = DbName.picker_tables  # FIXME:
        flag = 0                        # FIXME: magic
        header = {'token': self.token}
        data = {"timezone": "Europe/Moscow"}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/db_event_stats/{db_name}/{flag}", headers=header, json=data, verify=False)
        return resp

    def storage_worker_statistics_db_one_tab_stats_db_name_tab_name_get(self):
        """process GET req for getting one tables statistics info"""
        db_name = DbName.picker_tables  # FIXME:
        tab_name = "ad_groups_ngr"      # FIXME:    tab_name rel db_name
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/statistics/db_one_tab_stats/{db_name}/{tab_name}", headers=header, verify=False)
        return resp

    def storage_worker_statistics_db_search_post(self):
        """process POST req for getting columns matching search criteria"""
        header = {'token': self.token}
        data = {
            "database_name": "picker_tables",   # FIXME:
            "use_regexps": True
        }
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/db_search", headers=header, json=data, verify=False)
        return resp

    def storage_worker_statistics_db_stats_dbname_get(self):
        """process GET req for getting one db statistics info"""
        dbname = DbName.picker_tables
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/statistics/db_stats/{dbname}", headers=header, verify=False)
        return resp

    def storage_worker_statistics_db_tabs_event_stats_db_name_tab_name_flag_post(self):
        """process POST req for getting one table inserts dynamic"""
        db_name = DbName.picker_tables  # FIXME:
        tab_name = "ad_groups_ngr"      # FIXME: tab_name rel db_name
        flag = 0                        # FIXME: magic?
        header = {'token': self.token}
        data = {"timezone": "Europe/Moscow"}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/db_tabs_event_stats/{db_name}/{tab_name}/{flag}", headers=header, json=data, verify=False)
        return resp

    def storage_worker_statistics_db_tabs_stats_dbname_get(self):
        """process GET req for getting all tables statistics info"""
        dbname = DbName.picker_tables
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/statistics/db_tabs_stats/{dbname}", headers=header, verify=False)
        return resp

    def storage_worker_statistics_storage_search_post(self):
        """process POST req for getting content search result"""
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
        """process POST req for getting column test selection"""
        header = {'token': self.token}
        data = {"database_name": "picker_tables", "table_name": "ad_users_ngr", "name": "name"}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/test_selection", headers=header, json=data, verify=False)
        return resp

    def storage_worker_storage_db_get(self):
        """process GET to return all storage databases"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/db", headers=header, verify=False)
        return resp

    def storage_worker_storage_db_put(self):
        """process POST to edit storage db properties (description currently)"""
        header = {'token': self.token}
        data = {
            "base_name": DbName.API_TEST_DB1,
            "description": f"{DbName.API_TEST_DB1} +put"
        }
        resp = self.sess.put(f"{self.host}/back/dp.storage_worker/storage/db", headers=header, json=data, verify=False)
        return resp

    def storage_worker_storage_db_post(self):
        """process POST to create new storage DB"""
        header = {'token': self.token}
        data = {
            "base_name": DbName.API_TEST_DB1,
            "description": f"{DbName.API_TEST_DB1} auto created"
        }
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/storage/db", headers=header, json=data, verify=False)
        return resp

    def storage_worker_storage_db_delete(self):
        """process DELETE to delete storage DB (if already exists)"""
        db_name = DbName.API_TEST_DB1
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.storage_worker/storage/db/{db_name}", headers=header, verify=False)
        return resp

    def storage_worker_storage_import_csv_db_name_table_name_post(self):
        """process POST to insert fetched from csv data into DB table"""
        db_name = DbName.picker_tables  # FIXME:
        table_name = "ad_groups_ngr"    # FIXME: table_name rel db_name
        header = {'token': self.token}
        data = {"data": None}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/storage/import_csv/{db_name}/{table_name}", headers=header, json=data, verify=False)
        return resp

    def storage_worker_storage_import_json_db_name_table_name_post(self):
        """process POST to insert fetched from json data into DB table"""
        db_name = DbName.picker_tables  # FIXME:
        table_name = "ad_groups_ngr"    # FIXME: table_name rel db_name
        header = {'token': self.token}
        data = {"data": None}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/storage/import_json/{db_name}/{table_name}", headers=header, json=data, verify=False)
        return resp

    def storage_worker_storage_supported_engines_get(self):
        """process GET req to get available storage table engine list"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/supported_engines", headers=header, verify=False)
        return resp

    def storage_worker_storage_supported_types_get(self):
        """process GET req to get storage data types list"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/supported_types", headers=header, verify=False)
        return resp

    def storage_worker_storage_table_columns_db_name_tab_name_get(self):
        """process GET req for getting table columns"""
        db_name = DbName.picker_tables  # FIXME:
        tab_name = "ad_groups_ngr"      # FIXME: tab_name rel db_name
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/table/columns/{db_name}/{tab_name}", headers=header, verify=False)
        return resp

    # FIXME: падает GL
    # Неверный синтаксис запроса или ошибка соединения (c)
    # .."msg": "Ошибка создания view"}}
    def storage_worker_storage_table_columns_db_name_table_name_post(self):
        """process POST to set aliases for columns"""
        db_name = DbName.picker_tables  # FIXME:
        table_name = "ad_groups_ngr"    # FIXME: table_name rel db_name
        header = {'token': self.token}

        data = [
            {"name": "Nopt", "dtype": "DateTime", "alias": "псевдоним", "mask_it": False},
            {"name": "Npqroduct", "alias": "", "table_name": "ad_groups_ngr", "database_name": "picker_tables", "dtype": "String", "mask_it": False},
            {"name": "Ntype", "alias": "", "table_name": "ad_groups_ngr", "database_name": "picker_tables", "dtype": "String", "mask_it": False},
            {"name": "opt", "alias": "", "table_name": "ad_groups_ngr", "database_name": "picker_tables", "dtype": "DateTime", "mask_it": False},
            {"name": "pqroduct", "alias": "", "table_name": "ad_groups_ngr", "database_name": "picker_tables", "dtype": "String", "mask_it": False},
            {"name": "type", "alias": "", "table_name": "ad_groups_ngr", "database_name": "picker_tables", "dtype": "UInt32", "mask_it": False}
        ]

        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/storage/table/columns/{db_name}/{table_name}", headers=header, json=data, verify=False)
        return resp

    # TODO: [POST] /back/dp.storage_worker/storage/table/{db_name}
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
    # TODO: [POST] /back/dp.storage_worker/storage/table/{db_name}/{table_name}
    # def storage_worker_storage_table_table_db_name_table_name(self):
    #     header = {'token': self.token}
    #     data = {"name": "five", "type": "Int8"}
    #     resp = self.sess.post(f"{self.host}/back/dp.storage_worker/storage/table/API_TEST_DB1/API_TEST_TABLE",
    #                           headers=header, json=data, verify=False)
    #     return resp

    # TODO: [DELETE] /back/dp.storage_worker/storage/table/{db_name}/{table_name}

    def storage_worker_storage_table_db_name_table_name_ttl_get(self):
        """returns TTL settings for a table"""
        db_name = DbName.picker_tables  # FIXME:
        table_name = "ad_groups_ngr"    # FIXME: table_name rel db_name
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/table/{db_name}/{table_name}/ttl", headers=header, verify=False)
        return resp

    # TODO: [PUT] /back/dp.storage_worker/storage/table/{db_name}/{table_name}/ttl

    # TODO: [DELETE] /back/dp.storage_worker/storage/table/{db_name}/{table_name}/{column_name}

    def storage_worker_storage_table_db_name_table_name_count_get(self):
        """process GET to return to client a part of data from table"""
        db_name = DbName.picker_tables  # FIXME:
        table_name = "ad_groups_ngr"    # FIXME: table_name rel db_name
        count = 2                       # number of rows limit
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/table/{db_name}/{table_name}/{count}", headers=header, verify=False)
        return resp

    # TODO: [POST] /back/dp.storage_worker/storage/view/{db_name}
