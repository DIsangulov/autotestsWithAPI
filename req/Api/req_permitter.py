import json
import random

from req.Helpers.base_req import BaseReq


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


class Permitter(BaseReq):

    # def __del__(self):
    #     pass  # delete all temp_role_id ' s

    def _get_temp_role_id(self) -> int:
        if len(role_id) == 0:   # global role_id
            self.permitter_roles_editor_roles_post()

        return role_id[-1]

    def _get_random_tab_id(self) -> int:
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/all_tables", headers=header, verify=False)
        dct = json.loads(resp.text)
        return dct['res'][1]['id']

    def permitter_check_ui_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/check_ui", headers=header, verify=False)
        return resp

    def permitter_db_watcher_all_db_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/all_db", headers=header, verify=False)
        return resp

    def permitter_db_watcher_all_tables_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/all_tables", headers=header, verify=False)
        # dct = json.loads(resp.text)
        # global tab_id
        # tab_id = dct['res'][1]['id']  # получили id таблицы # ad_groups_masked
        # print(tab_id)
        return resp

    def permitter_db_watcher_db_tables_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/db_tables/1", headers=header, verify=False)
        return resp

    def permitter_db_watcher_empty_role_dbs_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/empty_role_dbs", headers=header, verify=False)
        return resp

    def permitter_db_watcher_empty_role_tables_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/empty_role_tables", headers=header, verify=False)
        return resp

    def permitter_db_watcher_empty_role_tables_id_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/empty_role_tables/1", headers=header, verify=False)
        return resp

    def permitter_db_watcher_get_tab_name_id_get(self):
        tab_id = self._get_random_tab_id()
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/get_tab_name/" + str(tab_id), headers=header, verify=False)
        return resp

    # ______________/back/dp.permitter/element_flags/{element_type}/{element_id}_____________

    def permitter_element_flags_query_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_flags/query/123", headers=header, verify=False)
        return resp

    def permitter_element_flags_visualisation_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_flags/visualisation/260", headers=header, verify=False)
        return resp

    def permitter_element_flags_report_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_flags/report/4", headers=header, verify=False)
        return resp

    # FIXME: {"error":{"code":400,"description":"sql: no rows in result set","msg":"Ошибка выборки из бд"}}
    def permitter_element_flags_mailing_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_flags/mailing/1", headers=header, verify=False)
        return resp

    # FIXME: {"error":{"code":400,"description":"sql: no rows in result set","msg":"Ошибка выборки из бд"}}
    def permitter_element_flags_script_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_flags/script/206", headers=header, verify=False)
        return resp

    # FIXME: {"error":{"code":400,"description":"sql: no rows in result set","msg":"Ошибка выборки из бд"}}
    def permitter_element_flags_script_sequence_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_flags/script_sequence/56", headers=header, verify=False)
        return resp

    def permitter_element_flags_query_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {
            "opened": True,
            "published": True
        }
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_flags/query/123", headers=header, json=data, verify=False)
        return resp

    def permitter_element_flags_visualisation_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {
            "opened": True,
            "published": True
        }
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_flags/visualisation/260", headers=header, json=data, verify=False)
        return resp

    def permitter_element_flags_report_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {
            "opened": True,
            "published": True
        }
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_flags/report/4", headers=header, json=data, verify=False)
        return resp

    def permitter_element_flags_mailing_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {
            "opened": True,
            "published": True
        }
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_flags/mailing/1", headers=header, json=data, verify=False)
        return resp

    def permitter_element_flags_script_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {
            "opened": True,
            "published": True
        }
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_flags/script/206", headers=header, json=data, verify=False)
        return resp

    def permitter_element_flags_sscript_sequence_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {
            "opened": True,
            "published": True
        }
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_flags/script_sequence/56", headers=header, json=data, verify=False)
        return resp

    # ______________/back/dp.permitter/element_flags/{element_type}/{element_id}_____________

    # ______________/back/dp.permitter/element_rules/all/{element_type}/{element_id}_____________

    def permitter_element_rules_all_flags_query_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/all/query/123", headers=header, verify=False)
        return resp

    def permitter_element_rules_all_flags_visualisation_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/all/visualisation/260", headers=header, verify=False)
        return resp

    def permitter_element_rules_all_flags_report_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/all/report/4", headers=header, verify=False)
        return resp

    def permitter_element_rules_all_flags_mailing_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/all/mailing/1", headers=header, verify=False)
        return resp

    def permitter_element_rules_all_flags_script_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/all/script/206", headers=header, verify=False)
        return resp

    def permitter_element_rules_all_flags_script_sequence_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/all/script_sequence/56", headers=header, verify=False)
        return resp

    # ______________/back/dp.permitter/element_rules/all/{element_type}/{element_id}_____________

    # ______________/back/dp.permitter/element_rules/{element_type}/{element_id}_____________

    def permitter_element_rules_flags_query_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/query/123", headers=header, verify=False)
        return resp

    def permitter_element_rules_flags_visualisation_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/visualisation/260", headers=header, verify=False)
        return resp

    def permitter_element_rules_flags_report_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/report/4", headers=header, verify=False)
        return resp

    def permitter_element_rules_flags_mailing_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/mailing/1", headers=header, verify=False)
        return resp

    def permitter_element_rules_flags_script_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/script/206", headers=header, verify=False)
        return resp

    def permitter_element_rules_flags_script_sequence_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/element_rules/script_sequence/56", headers=header, verify=False)
        return resp

    def permitter_element_rules_flags_query_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {"who_id": 5, "is_user": False, "read": True, "write": True, "exec": True, "access": True}
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_rules/query/123", headers=header, json=data, verify=False)
        return resp

    def permitter_element_rules_flags_visualisation_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {"who_id": 5, "is_user": False, "read": True, "write": True, "exec": True, "access": True}
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_rules/visualisation/260", headers=header, json=data, verify=False)
        return resp

    def permitter_element_rules_flags_report_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {"who_id": 5, "is_user": False, "read": True, "write": True, "exec": True, "access": True}
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_rules/report/4", headers=header, json=data, verify=False)
        return resp

    def permitter_element_rules_flags_mailing_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {"who_id": 5, "is_user": False, "read": True, "write": True, "exec": True, "access": True}
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_rules/mailing/1", headers=header, json=data, verify=False)
        return resp

    def permitter_element_rules_flags_script_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {"who_id": 5, "is_user": False, "read": True, "write": True, "exec": True, "access": True}
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_rules/script/206", headers=header, json=data, verify=False)
        return resp

    # FIXME: {"error":{"code":403,"msg":"Запрещено"}}
    def permitter_element_rules_flags_script_sequence_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {"who_id": 5, "is_user": False, "read": True, "write": True, "exec": True, "access": True}
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_rules/script_sequence/56", headers=header, json=data, verify=False)
        return resp

    def permitter_element_rules_delete_element_type_query_element_id_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {"access": True, "exec": True, "id": 56, "is_user": True, "read": True, "who_id": 5, "write": True}
        resp = self.sess.post(f"{self.host}/back/dp.permitter/element_rules/delete/query/56", headers=header, json=data, verify=False)
        return resp

    # ______________/back/dp.permitter/element_rules/{element_type}/{element_id}_____________

    def permitter_roles_editor_roles_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/roles_editor/roles", headers=header, verify=False)
        return resp

    def permitter_roles_editor_roles_post(self):
        """process POST req for creating new role"""
        header = {'token': self.token, 'ui': str(2)}
        data = _get_sample_data()  # "name": f"auto_role_{random_num}}"
        resp = self.sess.post(f"{self.host}/back/dp.permitter/roles_editor/roles", headers=header, json=data, verify=False)

        dct = json.loads(resp.text)
        role_id.append(int(dct['res']))     # global role_id    # получили id роли

        return resp

    def permitter_roles_editor_roles_edit_id_get(self):
        _role_id = self._get_temp_role_id()
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/roles_editor/roles/edit/" + str(_role_id), headers=header, verify=False)
        return resp

    def permitter_roles_editor_roles_id_put(self):
        _role_id = self._get_temp_role_id()
        header = {'token': self.token, 'ui': str(2)}
        data = _get_sample_data()
        resp = self.sess.put(f"{self.host}/back/dp.permitter/roles_editor/roles/" + str(_role_id), headers=header, json=data, verify=False)
        return resp

    def permitter_roles_editor_roles_id_delete(self):
        # FIXME: удалять из глобального списка (role_id) роль .pop()
        _role_id = self._get_temp_role_id()
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.delete(f"{self.host}/back/dp.permitter/roles_editor/roles/" + str(_role_id), headers=header, verify=False)
        return resp

    def permitter_user_rules_get(self):
        # исп: Данные > скрипты
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/user_rules", headers=header, verify=False)
        return resp

    def permitter_users_elements_count_who_id_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/users/elements_count/123", headers=header, verify=False)
        return resp

    def permitter_users_new_author_who_id_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {
            "delete": True,
            "new_author": "TestAPI"
        }
        resp = self.sess.post(f"{self.host}/back/dp.permitter/users/new_author/123", headers=header, json=data, verify=False)
        return resp

    def permitter_who_rules_who_id_get(self):
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/role_rules/123", headers=header, verify=False)
        return resp

# add - this

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
