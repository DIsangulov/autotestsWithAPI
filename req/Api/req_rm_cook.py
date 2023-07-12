from req.Helpers.base_req import BaseReq


class RmCook(BaseReq):

    def rm_cook_active_directory_groups_get(self):
        """process GET req to get AD groups list."""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/groups")

    def rm_cook_active_directory_groups_id_get(self, _rm_group_id):
        """process GET req to get AD group by id"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/groups/{_rm_group_id}")

    def rm_cook_active_directory_state_get(self):
        """process GET req to get AD state stats/metrics"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/state")

    def rm_cook_active_directory_top_groups_get(self):
        """process GET req to get AD top groups list"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/top_groups")

    def rm_cook_active_directory_top_users_get(self):
        """process GET req to get AD top users list"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/top_users")

    def rm_cook_active_directory_users_get(self):
        """process GET req to get AD users list"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/users")

    def rm_cook_active_directory_users_id_get(self, _rm_user_id):
        """process GET req to get AD user by ID"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/active_directory/users/{_rm_user_id}")

    def rm_cook_calculation_start_calc_id_post(self, calc_id):
        """process POST req to start rm calculation"""
        return self.sess.post(f"{self.host}/back/dp.rm_cook/calculation/start/{calc_id}")

    def rm_cook_rm_logs_last_get(self):
        """process GET req to get the last RM calculation log"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/rm/logs/last")

    def rm_cook_rm_recommendations_get(self):
        """process GET req to get RoleMining recommendations"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/rm/recommendations")

    def rm_cook_rm_roles_id_alias_post(self, _id, data):
        """
        process POST req to set role alias. calc_time parameter is optional.
        If it's omitted, the last role model timestamp is used.
        """
        return self.sess.post(f"{self.host}/back/dp.rm_cook/rm/roles/{_id}/alias", json=data)

    # FIXME: /back/dp.rm_cook/rm/roles/{id}/alias/{ts}      << без {ts} писания нет
    def rm_cook_rm_roles_id_alias_get(self, _id):
        return self.sess.get(f"{self.host}/back/dp.rm_cook/rm/roles/{_id}/alias")

    def rm_cook_rm_status_get(self):
        """process GET req to get RM calculation status"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/rm/status")

    def rm_cook_role_model_result_export_role_model_to_excel_post(self, body):
        """process POST req to export role model to Excel file from rm_ml"""
        return self.sess.post(f"{self.host}/back/dp.rm_cook/role_model/result/export_role_model_to_excel", json=body)

    def rm_cook_role_model_result_groups_by_role_id_get(self, role_id):
        """process GET req to get full list of rm group by role id"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/groups_by_role/{role_id}")

    def rm_cook_role_model_result_resources_by_role_id_get(self, role_id):
        """process GET req to get full list of rm resource by role id"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/resources_by_role/{role_id}")

    def rm_cook_role_model_result_roles_by_source_source_id_get(self, _source_id):
        """process GET req to get full list of rm roles by source id"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/roles_by_source/{_source_id}")

    def rm_cook_role_model_result_source_source_id_users_by_role_role_id_get(self, source_id, role_id):
        """process GET req to get full list of rm user by role id"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/source/{source_id}/users_by_role/{role_id}")

    def rm_cook_role_model_result_table_role_role_id_resources_by_user_user_id_get(self, role_id, rm_user_id):
        """process GET req to get full list of rm resource by username id and role id"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/table/role/{role_id}/resources_by_user/{rm_user_id}")

    def rm_cook_role_model_result_table_role_role_id_users_by_resource_resource_id_get(self, role_id, resource_id):
        """process GET req to get full list of rm user by resource name and role id"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/table/role/{role_id}/users_by_resource/{resource_id}")

    def rm_cook_role_model_result_form_role_role_id_groups_by_user_user_id_get(self, form, role_id, user_id):
        """process GET req to get full list of rm group by username and role id"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/{form}/role/{role_id}/groups_by_user/{user_id}")

    def rm_cook_role_model_result_form_role_role_id_users_by_group_user_id_get(self, form, role_id, group_id):
        """process GET req to get full list of rm user by group name and role id"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/role_model/result/{form}/role/{role_id}/users_by_group/{group_id}")

    def rm_cook_settings_calc_get(self):
        """process GET req to get current RM calculations settings."""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/settings/calc")

    def rm_cook_settings_calc_put(self, body):
        """
        process PUT req to set new RM calculations settings.
        only roles_num is being set at the time
        """
        return self.sess.put(f"{self.host}/back/dp.rm_cook/settings/calc", json=body)

    def rm_cook_settings_mailings_get(self):
        """process GET req to get current syslog-mailing-alert RM settings"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/settings/mailings")

    def rm_cook_settings_mailings_post(self, body):
        """process POST req to set new syslog-mailing-alert RM settings"""
        return self.sess.post(f"{self.host}/back/dp.rm_cook/settings/mailings", json=body)

    def rm_cook_settings_sources_get(self):
        """process GET req to get current RM sources settings"""
        return self.sess.get(f"{self.host}/back/dp.rm_cook/settings/sources")

    def rm_cook_settings_sources_post(self, body):
        """process POST req to set RM sources settings"""
        return self.sess.post(f"{self.host}/back/dp.rm_cook/settings/sources", json=body)
