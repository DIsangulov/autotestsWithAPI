from req.Helpers.base_req import BaseReq


class XbaCook(BaseReq):

    def xba_cook_anomalies_get(self):
        """process GET req to get all app anomalies"""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/anomalies")

    def xba_cook_anomalies_picker_max_min_get(self):
        """process GET to get max and min date values"""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/anomalies/picker/max_min")

    def xba_cook_check_entity_type_post(self, data):
        """process POST for checking if entity type column contains not more distinct values than 20 & no nulls"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/check_entity_type", json=data)

    def xba_cook_dashboard_entities_post(self, data):
        """process POST for get data for entities statistics"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/dashboard/entities", json=data)

    def xba_cook_dashboard_entities_more_post(self, data):
        """process POST for get more anomalous entities"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/dashboard/entities/more", json=data)

    def xba_cook_dashboard_groups_post(self, data):
        """
        process POST for get data for meta profile statistics
        other, department, user, host, process:
        truе - included in the dashboard
        false - not included in the dashboard
        """
        return self.sess.post(f"{self.host}/back/dp.xba_cook/dashboard/groups", json=data)

    def xba_cook_dashboard_groups_more_post(self, data):
        """
        process POST for get more data for meta profile statistics
        other, department, user, host, process:
        truе - included in the dashboard
        false - not included in the dashboard
        """
        return self.sess.post(f"{self.host}/back/dp.xba_cook/dashboard/groups/more", json=data)

    def xba_cook_dashboard_profiles_post(self, data):
        """process POST req to get xba dashboard data"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/dashboard/profiles", json=data)

    def xba_cook_dashboard_profiles_more_post(self, data):
        """process POST req to get top 2k profiles by risk table"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/dashboard/profiles/more", json=data)

    def xba_cook_entity_post(self, data):
        """returns Entity card summary info and risk levels graph"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/entity", json=data)

    def xba_cook_entity_details_post(self, data):
        """returns Entity card detailed info: risk levels pie chart, risk by profile table"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/entity/details", json=data)

    def xba_cook_entity_info_post(self, data):
        """returns Entity card enrichment info (additional entity attributes from AD or DB-based dictionary)"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/entity/info", json=data)

    def xba_cook_entity_info_settings_get(self):
        """returns Entity card enrichment settings"""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/entity/info/settings")

    def xba_cook_entity_info_settings_post(self, data):
        """process POST req to set Entity card enrichment settings."""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/entity/info/settings", json=data)

    def xba_cook_entity_info_settings_entity_type_delete(self, entity_type):
        """process DELETE req to remove Entity card enrichment settings"""
        return self.sess.delete(f"{self.host}/back/dp.xba_cook/entity/info/settings/{entity_type}")

    def xba_cook_entity_picker_max_min_post(self, data):
        """process GET to get max and min date values"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/entity/picker/max_min", json=data)

    def xba_cook_entity_risks_description_post(self, data):
        """returns Entity card summary info and risk levels graph"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/entity/risks-description", json=data)

    def xba_cook_max_min_post(self, data):
        """process POST to get max and min column values"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/max_min", json=data)

    def xba_cook_profiles_get(self):
        """process GET req to get profile list"""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/profiles")

    def xba_cook_profiles_post(self, data):
        """process POST req to create new profile"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/profiles", json=data)

    def xba_cook_profiles_categories_get(self):
        """process GET req to get profile categories"""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/categories")

    def xba_cook_profiles_export_profiles_post(self, data):
        """process POST req to get profile list by ids"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/export_profiles", json=data)

    def xba_cook_profiles_functions_get(self):
        """process GET req to get profile functions"""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/functions")

    def xba_cook_profiles_graph_drilldown_statement_id_post(self, prof_id, data):
        """process POST to get statement for xba drilldown custom execution"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/graph/drilldown/statement/{prof_id}", json=data)

    def xba_cook_profiles_graph_drilldown_id_post(self, prof_id, data):
        """process POST to get profile raw data (deep-personal level)"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/graph/drilldown/{prof_id}", json=data)

    def xba_cook_profiles_max_min_id_get(self, prof_id):
        """process GET to get profile data max and min date"""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/graph/max_min/{prof_id}")

    def xba_cook_profiles_graph_personal_id_post(self, prof_id, data):
        """process POST to get profile personal data (personal level)"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/graph/personal/{prof_id}", json=data)

    def xba_cook_profiles_groups_get(self):
        """process GET req to get groups list"""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/groups")

    def xba_cook_profiles_groups_put(self, data):
        """process PUT req for updating group name"""
        return self.sess.put(f"{self.host}/back/dp.xba_cook/profiles/groups", json=data)

    def xba_cook_profiles_groups_post(self, data):
        """process POST to create new group"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/groups", json=data)

    def xba_cook_profiles_groups_info_get(self):
        """process GET req to get info"""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/groups/info")

    def xba_cook_profiles_groups_id_delete(self, group_id):
        """process DELETE to delete group"""
        return self.sess.delete(f"{self.host}/back/dp.xba_cook/profiles/groups/{group_id}")

    def xba_cook_profiles_groups_group_id_profiles_get(self, group_id):
        """process GET req to get list of profiles of the group"""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/groups/{group_id}/profiles")

    def xba_cook_profiles_groups_id_post(self, group_id, data):
        """process GET to get profile group data for visualisation on front"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/groups/{group_id}", json=data)

    def xba_cook_profiles_groups_id_max_min_get(self, group_id):
        """process GET to get profile group data max and min date"""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/groups/{group_id}/max_min")

    def xba_cook_profiles_groups_profile_id_group_id_delete(self, xba_profile_id, xba_group_id):
        """process GET req to delete profile from group"""
        return self.sess.delete(f"{self.host}/back/dp.xba_cook/profiles/groups/{xba_profile_id}/{xba_group_id}")

    def xba_cook_profiles_groups_profile_id_group_id_weight_get(self, prof_id, group_id, weight):
        """process GET req to update profile weight in group"""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/groups/{prof_id}/{group_id}/{weight}")

    def xba_cook_profiles_import_profiles_post(self, data):
        """process POST to create new profiles"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/import_profiles", json=data)

    def xba_cook_profiles_start_id_get(self, prof_id):
        """process GET req to start profile by id"""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/start/{prof_id}")

    def xba_cook_profiles_stop_id_get(self, prof_id):
        """process GET req to stop profile by id"""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/stop/{prof_id}")

    def xba_cook_profiles_id_get(self, prof_id):
        """process GET req to get profile info by id"""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/{prof_id}")

    def xba_cook_profiles_id_post(self, xba_profile_id, data):
        """process POST to edit xBA Profile"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/{xba_profile_id}", json=data)

    def xba_cook_profiles_id_delete(self, prof_id):
        """process DELETE to delete xBA Profile"""
        return self.sess.delete(f"{self.host}/back/dp.xba_cook/profiles/{prof_id}")

    def xba_cook_profiles_id_graph_post(self, xba_profile_id, data):
        """process POST to get profile data for visualisation on front"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/{xba_profile_id}/graph", json=data)

    def xba_cook_profiles_id_log_last_get(self, prof_id):
        """process GET req to get profile last log by profile id"""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/{prof_id}/log/last")

    def xba_cook_profiles_id_summary_post(self, xba_profile_id, data):
        """process POST to get profile summary data and top-10 of risky entities"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/{xba_profile_id}/summary", json=data)

    def xba_cook_profiles_id_whitelist_post(self, prof_id, data):
        """process POST req to update profile whitelist content"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/{prof_id}/whitelist", json=data)

    def xba_cook_profiles_id_whitelist_element_post(self, prof_id, data):
        """process POST req to add element into profile whitelist"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/{prof_id}/whitelist/element", json=data)

    def xba_cook_profiles_id_zones_post(self, xba_profile_id, data):
        """
        process GET to get profile's entites-by-zone table and counts (doughnut)
        zone: red|green|yellow, if something else, then everything will be displayed at once
        """
        return self.sess.post(f"{self.host}/back/dp.xba_cook/profiles/{xba_profile_id}/zones", json=data)

    def xba_cook_profiles_id_form_whitelist_get(self, prof_id, form):
        """process GET req to get profile whitelist content"""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/profiles/{prof_id}/{form}/whitelist")

    def xba_cook_profiles_profile_id_whitelist_element_id_delete(self, xba_profile_id, element_id):
        """process DELETE req to delete element from profile whitelist"""
        return self.sess.delete(f"{self.host}/back/dp.xba_cook/profiles/{xba_profile_id}/whitelist/element/{element_id}")

    def xba_cook_set_log_level_xba_py_mode_post(self, mode, data):
        """process POST to change level log in xba_py"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/set_log_level_xba_py/{mode}", json=data)

    def xba_cook_xba_get(self):
        """process GET req to get current syslog-mailing-alert xba settings."""
        return self.sess.get(f"{self.host}/back/dp.xba_cook/xba")

    def xba_cook_xba_post(self, data):
        """process POST req to set new syslog-mailing-alert xba settings"""
        return self.sess.post(f"{self.host}/back/dp.xba_cook/xba", json=data)
