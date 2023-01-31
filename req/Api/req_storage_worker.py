import json
import random

from req.Helpers.base_req import BaseReq

reg_pid = None
rand = None


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
