import json
import random

from req.Helpers.base_req import BaseReq
from resourses.credentials import DbName

SYSLOG_HOST = "107.130.0.16"
SYSLOG_PORT = 514


class RmCook(BaseReq):

    def _get_random_rm_user_id(self) -> int:
        _resp = self.rm_cook_active_directory_users_get()               # получить запрос со списком пользователей
        _rm_users_info_rows = json.loads(_resp.text)['res']['users']    # получить из запроса список пользователей
        _rm_user_info = random.choice(_rm_users_info_rows)              # получить случайную строку из списка
        return int(_rm_user_info['id'])

    def _get_random_rm_group_id(self) -> int:
        _resp = self.rm_cook_active_directory_groups_get()              # получить запрос со списком групп
        _rm_groups_info_rows = json.loads(_resp.text)['res']['groups']  # получить из запроса список групп
        _rm_group_info = random.choice(_rm_groups_info_rows)            # получить случайную строку из списка
        return int(_rm_group_info['id'])

    def rm_cook_active_directory_groups_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/groups", headers=header, verify=False)
        return resp

    def rm_cook_active_directory_groups_id_get(self):
        _rm_group_id = self._get_random_rm_group_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/groups/" + str(_rm_group_id), headers=header, verify=False)
        return resp

    def rm_cook_active_directory_state_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/state", headers=header, verify=False)
        return resp

    def rm_cook_active_directory_top_groups_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/top_groups", headers=header, verify=False)
        return resp

    def rm_cook_active_directory_top_users_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/top_users", headers=header, verify=False)
        return resp

    def rm_cook_active_directory_users_get(self):
        """process GET req to get AD users list"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/users", headers=header, verify=False)
        return resp

    def rm_cook_active_directory_users_id_get(self):
        """process GET req to get AD user by ID"""
        _rm_user_id = self._get_random_rm_user_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/users/" + str(_rm_user_id), headers=header, verify=False)
        return resp

    def rm_cook_calculation_start_calc_id_post(self):
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.rm_cook/calculation/start/1", headers=header, verify=False)
        return resp

    def rm_cook_rm_logs_last_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/rm/logs/last", headers=header, verify=False)
        return resp

    def rm_cook_rm_recommendations_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/rm/recommendations", headers=header, verify=False)
        return resp

    def rm_cook_rm_roles_id_alias_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {"alias": "Роль 0_изменено", "id": 0}
        resp = self.sess.post(f"{self.host}/back/dp.rm_cook/rm/roles/0/alias", headers=header, json=data, verify=False)
        return resp

    def rm_cook_rm_roles_id_alias_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/rm/roles/0/alias", headers=header, verify=False)
        return resp

    def rm_cook_rm_status_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/rm/status", headers=header, verify=False)
        return resp

    def rm_cook_role_model_result_export_role_model_to_excel_post(self):
        body = {
            "groups_db": "picker_tables",
            "groups_table": "ad_groups_ngr_2",
            "source": 0,
            "users_db": "picker_tables",
            "users_table": "ad_users_ngr_2"
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.rm_cook/role_model/result/export_role_model_to_excel", headers=header, json=body, verify=False)
        return resp

    # FIXME: role_id == 0; кейс проходит
    def rm_cook_role_model_result_groups_by_role_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/groups_by_role/0", headers=header, verify=False)
        return resp

    # FIXME: role_id == 0;
    def rm_cook_role_model_result_resources_by_role_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/resources_by_role/0", headers=header, verify=False)
        return resp

    def rm_cook_role_model_result_roles_by_source_source_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/roles_by_source/0", headers=header, verify=False)
        return resp

    # FIXME: role_id == 0; кейс проходит
    def rm_cook_role_model_result_source_source_id_users_by_role_role_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/source/0/users_by_role/0", headers=header, verify=False)
        return resp

    # FIXME: role_id == 0
    def rm_cook_role_model_result_table_role_role_id_resources_by_user_user_id_get(self):
        _rm_user_id = self._get_random_rm_user_id()
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/table/role/0/resources_by_user/" + str(_rm_user_id), headers=header, verify=False)
        return resp

    # FIXME: role_id == 0
    def rm_cook_role_model_result_table_role_role_id_users_by_resource_resource_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/table/role/0/users_by_resource/0", headers=header, verify=False)
        return resp

    # FIXME: role_id == 0
    def rm_cook_role_model_result_form_role_role_id_groups_by_user_user_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/table/role/0/users_by_group/3909688664", headers=header, verify=False)
        return resp

    # FIXME: role_id == 0
    def rm_cook_role_model_result_form_role_role_id_users_by_group_user_id_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/table/role/0/groups_by_user/1996248437", headers=header, verify=False)
        return resp

    def rm_cook_settings_calc_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/settings/calc", headers=header, verify=False)
        return resp

    def rm_cook_settings_calc_put(self):
        body = {"roles_num": 20}
        header = {'token': self.token}
        resp = self.sess.put(f"{self.host}/back/dp.rm_cook/settings/calc", headers=header, json=body, verify=False)
        return resp

    def rm_cook_settings_mailings_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/settings/mailings", headers=header, verify=False)
        return resp

    def rm_cook_settings_mailings_post(self):
        body = {"destinations": [
            {"email": "",
             "syslog_host": SYSLOG_HOST,
             "syslog_port": SYSLOG_PORT,
             "syslog_protocol": "tcp",
             "disable_syslog": False,
             "disable_email": True, "id": 1},
            {"email": "qa@ku.ku",
             "syslog_host": "",
             "syslog_port": 0,
             "syslog_protocol": "",
             "disable_syslog": True,
             "disable_email": True,
             "id": 2}]}
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.rm_cook/settings/mailings", headers=header, json=body, verify=False)
        return resp

    def rm_cook_settings_sources_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/settings/sources", headers=header, verify=False)
        return resp

    def rm_cook_settings_sources_post(self):
        # db_picker_tables = self._id_picker_tables_get()
        db_picker_tables = self.get_db_id_by_name(DbName.picker_tables)
        body = [{"db_name": "picker_tables", "db_id": db_picker_tables, "source_type": 1, "table_name": "ad_groups_ngr"},
                {"db_name": "picker_tables", "db_id": db_picker_tables, "source_type": 2, "table_name": "ad_users_ngr"}]
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.rm_cook/settings/sources", headers=header, json=body, verify=False)
        return resp
