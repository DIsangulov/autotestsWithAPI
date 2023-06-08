import json

from req.Helpers.base_req import BaseReq

group_id = None
user_id = None
syslog_host = "107.130.0.16"
pt_id = None


class Rm_Cook(BaseReq):

    def id_picker_table_get(self, token):  # забираем id таблицы picker_table
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/db",
                             headers=header, verify=False)
        json_data = json.loads(resp.text)
        global pt_id
        for item in json_data['res']:
            if item['name'] == 'picker_tables':
                pt_id = item['id']
        print(pt_id)
        return resp

    def rm_cook_active_directory_groups_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/groups", headers=header, verify=False)
        dct = json.loads(resp.text)
        global group_id
        group_id = dct['res']['groups'][1]['id']  # получили id группы
        return resp

    def rm_cook_active_directory_groups_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/groups/" + str(group_id), headers=header,
                             verify=False)
        return resp

    def rm_cook_active_directory_state_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/state", headers=header, verify=False)
        return resp

    def rm_cook_active_directory_top_groups_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/top_groups", headers=header, verify=False)
        return resp

    def rm_cook_active_directory_top_users_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/top_users", headers=header, verify=False)
        return resp

    def rm_cook_active_directory_users_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/users", headers=header, verify=False)
        dct = json.loads(resp.text)
        global user_id
        user_id = dct['res']['users'][1]['id']  # получили id пользователя
        return resp

    def rm_cook_active_directory_users_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/users/" + str(user_id), headers=header,
                             verify=False)
        return resp

    def rm_cook_calculation_start_calc_id_post(self, token):
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.rm_cook/calculation/start/1", headers=header, verify=False)
        return resp

    def rm_cook_rm_logs_last_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/rm/logs/last", headers=header, verify=False)
        return resp

    def rm_cook_rm_recommendations_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/rm/recommendations", headers=header, verify=False)
        return resp

    def rm_cook_rm_roles_id_alias_post(self, token):
        header = {'token': token, 'ui': str(2)}
        data = {"alias": "Роль 0_изменено", "id": 0}
        resp = self.sess.post(f"{self.host}/back/dp.rm_cook/rm/roles/0/alias", headers=header, json=data, verify=False)
        return resp

    def rm_cook_rm_roles_id_alias_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/rm/roles/0/alias", headers=header, verify=False)
        return resp

    def rm_cook_rm_status_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/rm/status", headers=header, verify=False)
        return resp

    def rm_cook_role_model_result_export_role_model_to_excel_post(self, token):
        body = {
            "groups_db": "picker_tables",
            "groups_table": "ad_groups_ngr_2",
            "source": 0,
            "users_db": "picker_tables",
            "users_table": "ad_users_ngr_2"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.rm_cook/role_model/result/export_role_model_to_excel",
                              headers=header, json=body, verify=False)
        return resp

    def rm_cook_role_model_result_groups_by_role_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/groups_by_role/0", headers=header,
                             verify=False)
        return resp

    def rm_cook_role_model_result_resources_by_role_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/resources_by_role/0", headers=header,
                             verify=False)
        return resp

    def rm_cook_role_model_result_roles_by_source_source_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/roles_by_source/0", headers=header,
                             verify=False)
        return resp

    def rm_cook_role_model_result_source_source_id_users_by_role_role_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/source/0/users_by_role/0", headers=header,
                             verify=False)
        return resp

    def rm_cook_role_model_result_table_role_role_id_resources_by_user_user_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(
            f"{self.host}/back/dp.rm_cook/role_model/result/table/role/0/resources_by_user/" + str(user_id),
            headers=header, verify=False)
        return resp

    def rm_cook_role_model_result_table_role_role_id_users_by_resource_resource_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/table/role/0/users_by_resource/0",
                             headers=header, verify=False)
        return resp

    def rm_cook_role_model_result_form_role_role_id_groups_by_user_user_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(
            f"{self.host}/back/dp.rm_cook/role_model/result/table/role/0/users_by_group/3909688664",
            headers=header, verify=False)
        return resp

    def rm_cook_role_model_result_form_role_role_id_users_by_group_user_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(
            f"{self.host}/back/dp.rm_cook/role_model/result/table/role/0/groups_by_user/1996248437",
            headers=header, verify=False)
        return resp

    def rm_cook_settings_calc_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/settings/calc", headers=header, verify=False)
        return resp

    def rm_cook_settings_calc_put(self, token):
        body = {"roles_num": 20}
        header = {'token': token}
        resp = self.sess.put(f"{self.host}/back/dp.rm_cook/settings/calc", headers=header, json=body, verify=False)
        return resp

    def rm_cook_settings_mailings_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/settings/mailings", headers=header, verify=False)
        return resp

    def rm_cook_settings_mailings_post(self, token):
        body = {"destinations": [
            {"email": "",
             "syslog_host": syslog_host,
             "syslog_port": 514,
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
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.rm_cook/settings/mailings", headers=header, json=body, verify=False)
        return resp

    def rm_cook_settings_sources_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.rm_cook/settings/sources", headers=header, verify=False)
        return resp

    def rm_cook_settings_sources_post(self, token):
        body = [{"db_name": "picker_tables", "db_id": pt_id, "source_type": 1, "table_name": "ad_groups_ngr"},
                {"db_name": "picker_tables", "db_id": pt_id, "source_type": 2, "table_name": "ad_users_ngr"}]
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.rm_cook/settings/sources", headers=header, json=body, verify=False)
        return resp
