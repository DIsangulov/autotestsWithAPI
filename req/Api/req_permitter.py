import json
import random
import requests

from req.Helpers.base_req import BaseReq
from req.Helpers.base_req_raw import BaseReqRaw


def _get_sample_data() -> dict:
    s_data = {"name": f"auto_role_{random.randint(0, 999)}", "views": [
        {"id": 1, "name": "Администрирование", "ui_part": "administration", "read": False, "write": False, "disabled": []},
        {"id": 2, "name": "Данные", "ui_part": "data", "read": False, "write": False, "disabled": []},
        {"id": 3, "name": "Аналитика", "ui_part": "analytics", "read": False, "write": False, "disabled": []},
        {"id": 4, "name": "xBA", "ui_part": "xba", "read": False, "write": False, "disabled": []},
        {"id": 5, "name": "Role Mining", "ui_part": "rm", "read": False, "write": False, "disabled": []}
    ]}
    return s_data


role_id = []


class PermitterNew(BaseReqRaw):

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

class Permitter(BaseReq):

    def _get_temp_role_id(self) -> int:
        if len(role_id) == 0:   # global role_id
            self.permitter_roles_editor_roles_post()

        return role_id[-1]

    # ______________/back/dp.permitter/element_rules/{element_type}/{element_id}_____________

    # TODO: [POST] /back/dp.permitter/element_rules/delete/{element_type}/{element_id}

    def permitter_element_rules_delete_element_type_query_element_id_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {"access": True, "exec": True, "id": 56, "is_user": True, "read": True, "who_id": 5, "write": True}
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_rules/delete/query/56", headers=header, json=data, verify=False)
        return resp

    # TODO: [GET] /back/dp.permitter/element_rules/{element_type}/{element_id}

    def permitter_element_rules_query_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/query/123", headers=header, verify=False)
        return resp

    def permitter_element_rules_visualisation_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/visualisation/260", headers=header, verify=False)
        return resp

    def permitter_element_rules_report_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/report/4", headers=header, verify=False)
        return resp

    def permitter_element_rules_mailing_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/mailing/1", headers=header, verify=False)
        return resp

    def permitter_element_rules_script_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/script/206", headers=header, verify=False)
        return resp

    def permitter_element_rules_script_sequence_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/script_sequence/56", headers=header, verify=False)
        return resp

    # TODO: [POST] /back/dp.permitter/element_rules/{element_type}/{element_id}

    def permitter_element_rules_query_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {"who_id": 5, "is_user": False, "read": True, "write": True, "exec": True, "access": True}
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_rules/query/123", headers=header, json=data, verify=False)
        return resp

    def permitter_element_rules_visualisation_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {"who_id": 5, "is_user": False, "read": True, "write": True, "exec": True, "access": True}
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_rules/visualisation/260", headers=header, json=data, verify=False)
        return resp

    def permitter_element_rules_report_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {"who_id": 5, "is_user": False, "read": True, "write": True, "exec": True, "access": True}
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_rules/report/4", headers=header, json=data, verify=False)
        return resp

    def permitter_element_rules_mailing_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {"who_id": 5, "is_user": False, "read": True, "write": True, "exec": True, "access": True}
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_rules/mailing/1", headers=header, json=data, verify=False)
        return resp

    def permitter_element_rules_script_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {"who_id": 5, "is_user": False, "read": True, "write": True, "exec": True, "access": True}
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_rules/script/206", headers=header, json=data, verify=False)
        return resp

    # FIXME: {"error":{"code":403,"msg":"Запрещено"}}
    def permitter_element_rules_script_sequence_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {"who_id": 5, "is_user": False, "read": True, "write": True, "exec": True, "access": True}
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_rules/script_sequence/56", headers=header, json=data, verify=False)
        return resp

    # ______________/back/dp.permitter/element_rules/{element_type}/{element_id}_____________

    def permitter_roles_editor_roles_get(self):
        """process GET req for getting roles list"""
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/roles_editor/roles", headers=header, verify=False)
        return resp

    def permitter_roles_editor_roles_post(self):
        """process POST req for creating new role"""
        header = {'token': self.token, 'ui': str(2)}
        data = _get_sample_data()  # "name": f"auto_role_{random_num}}"
        resp = self.sess.post(f"{self.host}/back/dp.permitter/roles_editor/roles", headers=header, json=data, verify=False)

        # FIXME: перенести логику в _get_temp_role_id
        dct = json.loads(resp.text)
        role_id.append(int(dct['res']))     # global role_id    # получили id роли

        return resp

    def permitter_roles_editor_roles_edit_id_get(self):
        """process GET req for getting role by id"""
        _role_id = self._get_temp_role_id()
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/roles_editor/roles/edit/{_role_id}", headers=header, verify=False)
        return resp

    def permitter_roles_editor_roles_id_put(self):
        """process PUT req for editing role by id"""
        _role_id = self._get_temp_role_id()
        header = {'token': self.token, 'ui': str(2)}
        data = _get_sample_data()
        resp = self.sess.put(f"{self.host}/back/dp.permitter/roles_editor/roles/{_role_id}", headers=header, json=data, verify=False)
        return resp

    def permitter_roles_editor_roles_id_delete(self):
        """process DELETE req for deleting role by id"""
        _role_id = self._get_temp_role_id()
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.delete(f"{self.host}/back/dp.permitter/roles_editor/roles/{_role_id}", headers=header, verify=False)
        return resp

    def permitter_user_rules_get(self):
        """process GET req for getting all user rights by token"""
        # исп: Данные > скрипты
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/user_rules", headers=header, verify=False)
        return resp

    def permitter_users_elements_count_who_id_get(self):
        """process GET req for getting count of elements authored user with who_id"""
        who_id = 123
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/users/elements_count/{who_id}", headers=header, verify=False)
        return resp

    def permitter_users_new_author_who_id_post(self):
        """process POST req for setting new author (or opening/publishing) all elements authored by who_id"""
        who_id = 123
        header = {'token': self.token, 'ui': str(2)}
        data = {
            "delete": True,
            "new_author": "TestAPI"
        }
        resp = self.sess.post(f"{self.host}/back/dp.permitter/users/new_author/{who_id}", headers=header, json=data, verify=False)
        return resp

    def permitter_who_rules_who_id_get(self):
        """process GET req for getting all user or role rights by user id"""
        who_id = 123
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/role_rules/{who_id}", headers=header, verify=False)
        return resp

    # def __del__(self):
    #     pass  # delete all temp_role_id ' s

# исп: редактирование скрипта
# get: /back/dp.permitter/element_rules/script/305

# исп: редактирование последовательности
# get: /dp.permitter/element_rules/script_sequence/11

# исп: Аналитика > отчеты
# get: /dp.permitter/element_rules/report/408

# исп: Данные > рассылки > редактирование рассылки из отчета
# get: /back/dp.permitter/element_rules/mailing/409

# исп: Аналитика > визуализации > редактирование визуализации
# get: /back/dp.permitter/element_rules/visualisation/282

# исп: Аналитика > запросы > редактирование запроса
# get: /back/dp.permitter/element_rules/query/134
