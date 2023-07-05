import requests

from req.Helpers.base_req_raw import BaseReqRaw


class Permitter(BaseReqRaw):

    def permitter_check_ui_get(self) -> requests.Response:
        """process GET req for getting ui rules for token ([admin,data,analytics,xba,rm], 0-no access, 1-read, 2-write)"""
        return self.sess.get(f"{self.host}/back/dp.permitter/check_ui")

    def permitter_db_watcher_all_db_get(self) -> requests.Response:
        """process GET req for getting all (ch) databases list with role (by tok) rules"""
        return self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/all_db")

    def permitter_db_watcher_all_tables_get(self) -> requests.Response:
        """process GET req for getting all (ch) tables list with role (by tok) rules"""
        return self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/all_tables")

    def permitter_db_watcher_db_tables_id_get(self, _id) -> requests.Response:
        """process GET req for getting all (ch) tables list from db with id=db_id"""
        return self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/db_tables/{_id}")

    def permitter_db_watcher_empty_role_dbs_get(self) -> requests.Response:
        """process GET req for getting databases with empty role rules"""
        return self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/empty_role_dbs")

    def permitter_db_watcher_empty_role_tables_get(self) -> requests.Response:
        """process GET req for getting tables (all) with empty role rules"""
        return self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/empty_role_tables")

    def permitter_db_watcher_empty_role_tables_id_get(self, _id) -> requests.Response:
        """process GET req for getting tables (from db_id db) with empty role rules"""
        return self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/empty_role_tables/{_id}")

    def permitter_db_watcher_get_tab_name_id_get(self, tab_id) -> requests.Response:
        """process GET req for getting table name by table id"""
        return self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/get_tab_name/{tab_id}")

    def permitter_element_flags_element_type_element_id_get(self, element_type, element_id) -> requests.Response:
        """process GET req for getting element flags (published/opened)"""
        return self.sess.get(f"{self.host}/back/dp.permitter/element_flags/{element_type}/{element_id}")

    def permitter_element_flags_element_type_element_id_post(self, element_type, element_id, data) -> requests.Response:
        """process POST req for changing element flags (published/opened)"""
        return self.sess.post(f"{self.host}/back/dp.permitter/element_flags/{element_type}/{element_id}", json=data)

    def permitter_element_rules_all_element_type_element_id_get(self, element_type, element_id) -> requests.Response:
        """process GET req for getting all element rules for different roles&users"""
        return self.sess.get(f"{self.host}/back/dp.permitter/element_rules/all/{element_type}/{element_id}")

    def permitter_element_rules_delete_element_type_element_id_post(self, element_type, element_id, data) -> requests.Response:
        """process DELETE req for deleting element rules"""
        return self.sess.post(f"{self.host}/back/dp.permitter/element_rules/delete/{element_type}/{element_id}", json=data)

    def permitter_element_rules_element_type_element_id_get(self, element_type, element_id) -> requests.Response:
        """process GET req for getting element rules for users with tok"""
        return self.sess.get(f"{self.host}/back/dp.permitter/element_rules/{element_type}/{element_id}")

    def permitter_element_rules_element_type_element_id_post(self, element_type, element_id, data) -> requests.Response:
        """process POST req for changing element rules (published/opened)"""
        return self.sess.post(f"{self.host}/back/dp.permitter/element_rules/{element_type}/{element_id}", json=data)

    def permitter_roles_editor_roles_get(self) -> requests.Response:
        """process GET req for getting roles list"""
        return self.sess.get(f"{self.host}/back/dp.permitter/roles_editor/roles")

    def permitter_roles_editor_roles_post(self, data) -> requests.Response:
        """process POST req for creating new role"""
        return self.sess.post(f"{self.host}/back/dp.permitter/roles_editor/roles", json=data)

    def permitter_roles_editor_roles_edit_id_get(self, _role_id) -> requests.Response:
        """process GET req for getting role by id"""
        return self.sess.get(f"{self.host}/back/dp.permitter/roles_editor/roles/edit/{_role_id}")

    def permitter_roles_editor_roles_id_put(self, _role_id, data) -> requests.Response:
        """process PUT req for editing role by id"""
        return self.sess.put(f"{self.host}/back/dp.permitter/roles_editor/roles/{_role_id}", json=data)

    def permitter_roles_editor_roles_id_delete(self, _role_id) -> requests.Response:
        """process DELETE req for deleting role by id"""
        return self.sess.delete(f"{self.host}/back/dp.permitter/roles_editor/roles/{_role_id}")

    def permitter_user_rules_get(self) -> requests.Response:
        """process GET req for getting all user rights by token"""
        # исп: Данные > скрипты
        return self.sess.get(f"{self.host}/back/dp.permitter/user_rules")

    def permitter_users_elements_count_who_id_get(self, who_id) -> requests.Response:
        """process GET req for getting count of elements authored user with who_id"""
        return self.sess.get(f"{self.host}/back/dp.permitter/users/elements_count/{who_id}")

    def permitter_users_new_author_who_id_post(self, who_id, data) -> requests.Response:
        """process POST req for setting new author (or opening/publishing) all elements authored by who_id"""
        return self.sess.post(f"{self.host}/back/dp.permitter/users/new_author/{who_id}", json=data)

    def permitter_who_rules_who_id_get(self, who, who_id) -> requests.Response:
        """process GET req for getting all user or role rights by user id"""
        return self.sess.get(f"{self.host}/back/dp.permitter/{who}_rules/{who_id}")
