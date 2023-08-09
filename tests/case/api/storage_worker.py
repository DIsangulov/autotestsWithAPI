import datetime
import json
import random

from req.Helpers.user_session import UserSession
from req.Api.req_storage_worker import StorageWorker
from resourses.credentials import DbName
from tests.case.api.permitter import PermitterCase

API_AUTO_TEST_ = "API_AUTO_TEST_"

reg_pid = set()        # список, содержащий id новосозданных регулярных выражений


def get_datetime_now_z() -> str:
    # 2023-07-20T17:04:16Z
    return datetime.datetime.today().replace(microsecond=0).isoformat() + "Z"


class StorageWorkerCase(UserSession):

    def _collect_reg_pid(self):
        resp = StorageWorker(self.sess, self.host).storage_worker_psevdo_namer_regs_get()
        assert resp.status_code == 200, f"assert::storage_worker_psevdo_namer_regs_get, failed. status_code: {resp.status_code}, text: {resp.text}"

        reg_info_rows = json.loads(resp.text)['res']
        for _row in reg_info_rows:
            if str(_row['rus']).startswith(API_AUTO_TEST_):
                reg_pid.add(int(_row['id']))

    def _get_reg_pid(self) -> int:
        if len(reg_pid) == 0:
            self._collect_reg_pid()

        if len(reg_pid) == 0:                               # global reg_pid # id регулярного выражения
            r_new_reg_pid = self.case_storage_worker_psevdo_namer_regs_post()    # если нет, создай новую
            new_reg_pid = json.loads(r_new_reg_pid.text)['res']
            return int(new_reg_pid)

        return reg_pid.pop()

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
        return resp

    def case_storage_worker_psevdo_namer_regs_pid_get(self):
        req = StorageWorker(self.sess, self.host)
        _reg_pid = self._get_reg_pid()
        resp = req.storage_worker_psevdo_namer_regs_pid_get(_reg_pid)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_psevdo_namer_regs_pid_delete(self):
        req = StorageWorker(self.sess, self.host)

        _reg_pid = self._get_reg_pid()

        resp = req.storage_worker_psevdo_namer_regs_pid_delete(_reg_pid)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_storage_worker_show_base_db_name_get(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.picker_tables
        resp = req.storage_worker_show_base_db_name_get(db_name)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_storage_worker_statistics_db_event_stats_db_name_flag_post(self):
        # flag == | 0 - сегодня | 1 - вчера | 2 - неделя | 3 - месяц | 4 - год
        flag_keys = (0, 1, 2, 3, 4)

        req = StorageWorker(self.sess, self.host)

        db_name = DbName.picker_tables

        data = {
            # "start": "2023-08-13T00:00:00Z",
            # "end": get_datetime_now_z(),
            "offset": 0,
            "timeFlag": 0   # todo:? flag и в data, и в post-пути
        }
        for flag in flag_keys:
            resp = req.storage_worker_statistics_db_event_stats_db_name_flag_post(db_name, flag, data)
            # print(resp.text)
            assert resp.status_code == 200, f"Ошибка, code: {resp.status_code}, flag: {flag}, resp: {resp.text}"

    def case_storage_worker_statistics_db_one_tab_stats_db_name_tab_name_get(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.picker_tables
        tab_name = "ad_groups_ngr"
        resp = req.storage_worker_statistics_db_one_tab_stats_db_name_tab_name_get(db_name, tab_name)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_statistics_db_search_post(self):
        req = StorageWorker(self.sess, self.host)
        data = {
            "database_name": DbName.picker_tables,
            # "pattern": "pattern"      # fixme
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
        # flag == | 0 - сегодня | 1 - вчера | 2 - неделя | 3 - месяц | 4 - год
        flag_keys = (0, 1, 2, 3, 4)

        req = StorageWorker(self.sess, self.host)

        db_name = DbName.picker_tables
        tab_name = "ad_groups_ngr"
        data = {
            # "start": "2023-08-13T00:00:00Z",
            # "end": get_datetime_now_z(),
            "offset": 0,
            "timeFlag": 0   # todo: ?flag и в data, и в post-пути
        }

        for flag in flag_keys:
            resp = req.storage_worker_statistics_db_tabs_event_stats_db_name_tab_name_flag_post(db_name, tab_name, flag, data)
            # print(resp.text)
            assert resp.status_code == 200, f"Ошибка, code: {resp.status_code}, flag: {flag}, resp: {resp.text}"

    def case_storage_worker_statistics_db_tabs_stats_dbname_get(self):
        req = StorageWorker(self.sess, self.host)

        self.sess.headers.update({
            "ui": "1",
        })
        dbname = DbName.picker_tables

        resp = req.storage_worker_statistics_db_tabs_stats_dbname_get(dbname)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_statistics_storage_search_post(self):
        req = StorageWorker(self.sess, self.host)
        data = {
            "database_name": DbName.picker_tables,
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
        data = {
            "database_name": DbName.picker_tables,
            "table_name": "ad_users_ngr",
            "name": "name"
        }
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
        PermitterCase().permitter_sysop_add_permission_to_change_db_by_name(DbName.API_TEST_DB1)

    def case_storage_worker_storage_db_delete(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.API_TEST_DB1
        resp = req.storage_worker_storage_db_delete(db_name)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_storage_import_csv_db_name_table_name_post(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.picker_tables
        table_name = "ad_groups_ngr"
        data = {"data": None}
        resp = req.storage_worker_storage_import_csv_db_name_table_name_post(db_name, table_name, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_storage_import_json_db_name_table_name_post(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.picker_tables
        table_name = "ad_groups_ngr"
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
        db_name = DbName.picker_tables
        tab_name = "ad_groups_ngr"
        resp = req.storage_worker_storage_table_columns_db_name_tab_name_get(db_name, tab_name)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    # FIXME: падает GL
    # Неверный синтаксис запроса или ошибка соединения (c)
    # .."msg": "Ошибка создания view"}}
    def case_storage_worker_storage_table_columns_db_name_table_name_post(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.picker_tables  # FIXME: picker_tables >> test_db
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

    # TODO: [POST] /back/dp.storage_worker/storage/table/{db_name}
    def case_storage_worker_storage_table_db_name_post(self):
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
        req = StorageWorker(self.sess, self.host)
        db_name = None
        data = {}
        resp = req.storage_worker_storage_table_db_name_post(db_name, data)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # def storage_worker_storage_table_table_db_name_table_name(self):
    #     header = {'token': self.token}
    #     data = {"name": "five", "type": "Int8"}
    #     resp = self.sess.post(f"{self.host}/back/dp.storage_worker/storage/table/API_TEST_DB1/API_TEST_TABLE",
    #                           headers=header, json=data, verify=False)
    #     return resp

    def case_storage_worker_storage_table_db_name_table_name_ttl_get(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.picker_tables
        table_name = "ad_groups_ngr"
        resp = req.storage_worker_storage_table_db_name_table_name_ttl_get(db_name, table_name)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_storage_worker_storage_table_db_name_table_name_count_get(self):
        req = StorageWorker(self.sess, self.host)
        db_name = DbName.picker_tables
        table_name = "ad_groups_ngr"
        count = 2                       # number of rows limit
        resp = req.storage_worker_storage_table_db_name_table_name_count_get(db_name, table_name, count)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def all_api_auto_test_regs_delete(self):
        delete_req = StorageWorker(self.sess, self.host)
        self._collect_reg_pid()
        while len(reg_pid) > 0:
            delete_req.storage_worker_psevdo_namer_regs_pid_delete(reg_pid.pop())
