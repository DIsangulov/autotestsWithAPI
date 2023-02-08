import json
import random

from req.Helpers.base_req import BaseReq

reg_pid = None
rand = None
db_id = None


class StorageWorker(BaseReq):

    def storage_worker_ask_one_sql_post(self, token):
        header = {'token': token}
        data = {"base_id": 108, "base_name": "picker_tables",
                "statements": "SELECT access_point_name FROM polina2     LIMIT 50;",
                "regs": False,
                ""
                "params": []}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/ask_one_sql", headers=header, json=data,
                              verify=False)
        return resp

    def storage_worker_ask_plain_sql_post(self, token):
        header = {'token': token}
        data = {"base_id": 108, "tab_name": "polina2", "columns":
            [{"name": "access_point_name", "type": "LowCardinality(String)"}],
                "groupby": [], "filters": [], "agregators": [],
                "limit": 50, "base_name": "picker_tables", "regs": False}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/ask_plain_sql", headers=header, json=data,
                              verify=False)
        return resp

    def storage_worker_import_rules_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/import_rules", headers=header, verify=False)
        return resp

    def storage_worker_psevdo_namer_regs_post(self, token):
        global rand
        rand = random.randint(1200, 12500)
        header = {'token': token}
        data = {"rus": "TestApi_1" + str(rand), "reg": "1", "stages": "1", "postfix": "1", "state": False,
                "is_on": False, "author": 1238}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/psevdo_namer/regs", headers=header, json=data,
                              verify=False)

        return resp

    def storage_worker_psevdo_namer_regs_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/psevdo_namer/regs", headers=header, verify=False)
        dct = json.loads(resp.text)
        global reg_pid
        reg_pid = dct['res'][-1]['id']  # получили id регулярного выражения
        print(resp.text)
        print(reg_pid)
        return resp

    def storage_worker_psevdo_namer_regs_pid_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/psevdo_namer/regs/" + str(reg_pid), headers=header,
                             verify=False)
        return resp

    def storage_worker_psevdo_namer_regs_pid_delete(self, token):
        header = {'token': token}
        resp = self.sess.delete(f"{self.host}/back/dp.storage_worker/psevdo_namer/regs/" + str(reg_pid), headers=header,
                                verify=False)
        return resp

    def storage_worker_show_base_db_name_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/show_base/picker_tables", headers=header,
                             verify=False)
        return resp

    def storage_worker_statistics_db_event_stats_db_name_flag_post(self, token):
        global rand
        rand = random.randint(1200, 12500)
        header = {'token': token}
        data = {"timezone": "Europe/Moscow"}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/db_event_stats/picker_tables/0",
                              headers=header, json=data,
                              verify=False)
        return resp

    def storage_worker_statistics_db_one_tab_stats_db_name_tab_name_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/statistics/db_one_tab_stats/picker_tables"
                             f"/ad_groups_ngr", headers=header, verify=False)
        return resp

    def storage_worker_statistics_db_search_post(self, token):
        header = {'token': token}
        data = {
            "database_name": "picker_tables",
            "use_regexps": True
        }
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/db_search", headers=header, json=data,
                              verify=False)
        return resp

    def storage_worker_statistics_db_status_dbname_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/statistics/db_stats/picker_tables", headers=header,
                             verify=False)
        return resp

    def storage_worker_statistics_db_tabs_event_stats_db_name_tab_name_flag_post(self, token):
        global rand
        rand = random.randint(1200, 12500)
        header = {'token': token}
        data = {"timezone": "Europe/Moscow"}
        resp = self.sess.post(
            f"{self.host}/back/dp.storage_worker/statistics/db_tabs_event_stats/picker_tables/ad_groups_ngr/0",
            headers=header, json=data,
            verify=False)
        return resp

    def storage_worker_statistics_db_tabs_stats_dbname_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/statistics/db_tabs_stats/picker_tables",
                             headers=header, verify=False)
        return resp

    def storage_worker_statistics_storage_search_post(self, token):
        global rand
        rand = random.randint(1200, 12500)
        header = {'token': token}
        data = {"database_name": "picker_tables",
                "table": "ad_groups_ngr_fresh",
                "filter_columns": ["mail"],
                "select_columns": ["mail"],
                "pattern": "",
                "use_regexps": False}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/storage_search", headers=header,
                              json=data,
                              verify=False)
        return resp

    def storage_worker_statistics_test_selection_post(self, token):
        global rand
        rand = random.randint(1200, 12500)
        header = {'token': token}
        data = {"database_name": "picker_tables", "table_name": "ad_groups_ngr_fresh", "name": "name"}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/statistics/test_selection", headers=header,
                              json=data,
                              verify=False)
        return resp

    def storage_worker_storage_db_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/db",
                             headers=header, verify=False)
        dct = json.loads(resp.text)
        global db_id
        db_id = dct['res'][0]['id']  # получили id базы данных
        return resp

    def storage_worker_storage_db_post(self, token):
        header = {'token': token}
        data = {"base_name": "API_TEST_DB1", "description": "API_TEST_DB1"}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/storage/db", headers=header, json=data, verify=False)
        return resp

    def permitter_roles_editor_roles_for_storage_worker_put(self,
                                                            token):  # Меняем пермишенны у роли, чтобы дальше смоги изменять и удалять таблицу
        header = {'token': token, 'ui': str(2)}
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

    def storage_worker_storage_db_put(self, token):
        header = {'token': token}
        data = {"base_name": "API_TEST_DB1", "description": "API_TEST_DB11"}
        resp = self.sess.put(f"{self.host}/back/dp.storage_worker/storage/db", headers=header, json=data, verify=False)
        return resp

    def storage_worker_storage_db_delete(self, token):
        header = {'token': token}
        resp = self.sess.delete(f"{self.host}/back/dp.storage_worker/storage/db/API_TEST_DB1", headers=header,
                                verify=False)
        return resp

    def storage_worker_storage_import_csv_db_name_table_name_post(self, token):
        header = {'token': token}
        data = {"data": None}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/storage/import_csv/picker_tables/ad_groups_ngr",
                              headers=header, json=data, verify=False)
        return resp

    def storage_worker_storage_import_json_db_name_table_name_post(self, token):
        header = {'token': token}
        data = {"data": None}
        resp = self.sess.post(f"{self.host}/back/dp.storage_worker/storage/import_json/picker_tables/ad_groups_ngr",
                              headers=header, json=data, verify=False)
        return resp

    def storage_worker_storage_supported_engines_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/supported_engines", headers=header,
                             verify=False)
        return resp

    def storage_worker_storage_supported_types_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/supported_types", headers=header,
                             verify=False)
        return resp

    def storage_worker_storage_table_columns_db_name_tab_name_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/table/columns/picker_tables/ad_groups_ngr",
                             headers=header, verify=False)
        return resp

    def storage_worker_storage_table_columns_db_name_table_name_post(self, token):
        header = {'token': token}
        data = [{"name": "Nopt", "dtype": "DateTime", "alias": "псевдоним", "mask_it": False},
                {"name": "Npqroduct", "alias": "", "table_name": "TYPE_SYSNOST_2005", "database_name": "picker_tables",
                 "dtype": "String", "mask_it": False},
                {"name": "Ntype", "alias": "", "table_name": "TYPE_SYSNOST_2005", "database_name": "picker_tables",
                 "dtype": "String", "mask_it": False},
                {"name": "opt", "alias": "", "table_name": "TYPE_SYSNOST_2005", "database_name": "picker_tables",
                 "dtype": "DateTime", "mask_it": False},
                {"name": "pqroduct", "alias": "", "table_name": "TYPE_SYSNOST_2005", "database_name": "picker_tables",
                 "dtype": "String", "mask_it": False},
                {"name": "type", "alias": "", "table_name": "TYPE_SYSNOST_2005", "database_name": "picker_tables",
                 "dtype": "UInt32", "mask_it": False}]
        resp = self.sess.post(
            f"{self.host}/back/dp.storage_worker/storage/table/columns/picker_tables/TYPE_SYSNOST_2005",
            headers=header, json=data, verify=False)
        return resp

    # def storage_worker_storage_table_db_name_post(self, token):
    #     header = {'token': token}
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
    # def storage_worker_storage_table_table_db_name_table_name(self, token):
    #     header = {'token': token}
    #     data = {"name": "five", "type": "Int8"}
    #     resp = self.sess.post(f"{self.host}/back/dp.storage_worker/storage/table/API_TEST_DB1/API_TEST_TABLE",
    #                           headers=header, json=data, verify=False)
    #     return resp

    def storage_worker_storage_table_db_name_table_name_ttl_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/table/picker_tables/ad_groups_ngr/ttl",
                             headers=header, verify=False)
        return resp

    def storage_worker_storage_table_db_name_table_name_count_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/table/picker_tables/ad_groups_ngr/2",
                             headers=header, verify=False)
        return resp
