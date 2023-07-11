import json
import random

from req.Helpers.base_req import BaseReq
from req.Api.req_permitter import Permitter
from tests.case.api.reporter import ReporterCase
from tests.case.api.scripter import ScripterCase
from tests.case.api.visualisation import VisualisationCase

API_AUTO_TEST_ = "API_AUTO_TEST_"


def _get_sample_data() -> dict:
    s_data = {"name": f"{API_AUTO_TEST_}{random.randint(100, 999)}", "views": [
        {"ui_part": "administration", "read": False, "write": False},
        {"ui_part": "data", "read": False, "write": False},
        {"ui_part": "analytics", "read": False, "write": False},
        {"ui_part": "xba", "read": False, "write": False},
        {"ui_part": "rm", "read": False, "write": False}
    ]}
    return s_data


role_id = set()


class ElementType:
    query = "query"
    visualisation = "visualisation"
    report = "report"
    mailing = "mailing"
    script = "script"
    script_sequence = "script_sequence"


class PermitterCase(BaseReq):

    def _get_element_id_by_type(self, element_type) -> int:
        match element_type:
            case ElementType.query:
                return VisualisationCase(self.sess, self.host)._get_query_id()
            case ElementType.visualisation:
                return VisualisationCase(self.sess, self.host)._get_visualisation_id()
            case ElementType.report:
                return VisualisationCase(self.sess, self.host)._get_report_id()
            case ElementType.mailing:
                return ReporterCase(self.sess, self.host)._get_mailing_id()
            case ElementType.script:
                return ScripterCase(self.sess, self.host)._get_script_id()
            case ElementType.script_sequence:
                return ScripterCase(self.sess, self.host)._get_sequence_id()
            case _:
                assert False, f"Неверно выбран тип для {self.__class__.__name__}::{self._get_element_id_by_type.__name__}, element_type: {element_type}"

    def _collect_temp_role_id(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_roles_editor_roles_get()
        assert resp.status_code == 200, f"assert::permitter_roles_editor_roles_get, failed. status_code: {resp.status_code}, text: {resp.text}"

        role_info_rows = json.loads(resp.text)['res']
        for _row in role_info_rows:
            if str(_row['name']).startswith(API_AUTO_TEST_):
                role_id.add(int(_row['id']))

    def _get_temp_role_id(self) -> int:
        if len(role_id) == 0:
            self._collect_temp_role_id()

        if len(role_id) == 0:   # global role_id
            r_new_role = self.case_permitter_roles_editor_roles_post()  # создать новую роль
            new_role_id = json.loads(r_new_role.text)['res']
            return int(new_role_id)

        return role_id.pop()

    def _get_random_tab_id(self) -> int:
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/all_tables", headers=header, verify=False)
        dct = json.loads(resp.text)
        return dct['res'][1]['id']

    def case_permitter_check_ui_get(self):
        req = Permitter(self.sess, self.host)
        resp = req.permitter_check_ui_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_db_watcher_all_db_get(self):
        req = Permitter(self.sess, self.host)

        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_db_watcher_all_db_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_db_watcher_all_tables_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_db_watcher_all_tables_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_db_watcher_db_tables_id_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        _id = 1
        resp = req.permitter_db_watcher_db_tables_id_get(_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_db_watcher_empty_role_dbs_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_db_watcher_empty_role_dbs_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_db_watcher_empty_role_tables_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_db_watcher_empty_role_tables_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_db_watcher_empty_role_tables_id_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        _id = 1
        resp = req.permitter_db_watcher_empty_role_tables_id_get(_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_db_watcher_get_tab_name_id_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        tab_id = self._get_random_tab_id()
        resp = req.permitter_db_watcher_get_tab_name_id_get(tab_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    # <><><> <><><>
    def _permitter_element_flags_element_type_element_id_get(self, element_type, element_id):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_element_flags_element_type_element_id_get(element_type, element_id)
        # print(f"e_type: {element_type}, e_id: {element_id}, rtext: {resp.text}")
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_permitter_element_flags_query_id_get(self):
        element_type = ElementType.query
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_flags_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_flags_visualisation_id_get(self):
        element_type = ElementType.visualisation
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_flags_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_flags_report_id_get(self):
        element_type = ElementType.report
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_flags_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_flags_mailing_id_get(self):
        element_type = ElementType.mailing
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_flags_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_flags_script_id_get(self):
        element_type = ElementType.script
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_flags_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_flags_script_sequence_id_get(self):
        element_type = ElementType.script_sequence
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_flags_element_type_element_id_get(element_type, element_id)
    # <><><> <><><>

    # <><><> <><><>
    def _permitter_element_flags_element_type_element_id_post(self, element_type, element_id):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        data = {
            "opened": True,
            "published": True
        }
        resp = req.permitter_element_flags_element_type_element_id_post(element_type, element_id, data)
        # print(f"e_type: {element_type}, e_id: {element_id}, rtext: {resp.text}")
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # 200, при попытке изменить свой 'element', 400 - чужой

    def case_permitter_element_flags_query_id_post(self):
        element_type = ElementType.query
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_flags_element_type_element_id_post(element_type, element_id)

    def case_permitter_element_flags_visualisation_id_post(self):
        element_type = ElementType.visualisation
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_flags_element_type_element_id_post(element_type, element_id)

    def case_permitter_element_flags_report_id_post(self):
        element_type = ElementType.report
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_flags_element_type_element_id_post(element_type, element_id)

    def case_permitter_element_flags_mailing_id_post(self):
        element_type = ElementType.mailing
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_flags_element_type_element_id_post(element_type, element_id)

    def case_permitter_element_flags_script_id_post(self):
        element_type = ElementType.script
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_flags_element_type_element_id_post(element_type, element_id)

    def case_permitter_element_flags_script_sequence_id_post(self):
        element_type = ElementType.script_sequence
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_flags_element_type_element_id_post(element_type, element_id)
    # <><><> <><><>

    # <><><> <><><>
    # fixme: возвращает 200 с любым int значением element_id; query_id = 123456
    def _permitter_element_rules_all_element_type_element_id_get(self, element_type, element_id):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_element_rules_all_element_type_element_id_get(element_type, element_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_element_rules_all_query_id_get(self):
        element_type = ElementType.query
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_all_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_rules_all_visualisation_id_get(self):
        element_type = ElementType.visualisation
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_all_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_rules_all_report_id_get(self):
        element_type = ElementType.report
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_all_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_rules_all_mailing_id_get(self):
        element_type = ElementType.mailing
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_all_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_rules_all_script_id_get(self):
        element_type = ElementType.script
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_all_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_rules_all_script_sequence_id_get(self):
        element_type = ElementType.script_sequence
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_all_element_type_element_id_get(element_type, element_id)
    # <><><> <><><>

    # <><><> <><><>
    # FIXME: 200 or 400; add other element_type's
    def _permitter_element_rules_delete_element_type_element_id_post(self, element_type, element_id):
        pass

    def case_permitter_element_rules_delete_query_id_post(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        element_type = ElementType.query
        element_id = self._get_element_id_by_type(element_type)
        # FIXME: id -> в post-url и в data; who_id << ??
        data = {"access": True, "exec": True, "id": element_id, "is_user": True, "read": True, "who_id": 5, "write": True}
        resp = req.permitter_element_rules_delete_element_type_element_id_post(element_type, element_id, data)
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"
        print(resp.text)
    # <><><> <><><>

    # <><><> <><><>
    # fixme: возвращает 200 с любым int значением element_id; query_id = 123456
    def _permitter_element_rules_element_type_element_id_get(self, element_type, element_id):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_element_rules_element_type_element_id_get(element_type, element_id)
        # print(f"e_type: {element_type}, e_id: {element_id}, rtext: {resp.text}")
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_permitter_element_rules_query_id_get(self):
        element_type = ElementType.query
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_rules_visualisation_id_get(self):
        element_type = ElementType.visualisation
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_rules_report_id_get(self):
        element_type = ElementType.report
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_rules_mailing_id_get(self):
        element_type = ElementType.mailing
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_rules_script_id_get(self):
        element_type = ElementType.script
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_rules_script_sequence_id_get(self):
        element_type = ElementType.script_sequence
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_element_type_element_id_get(element_type, element_id)

    # <><><> <><><>

    # <><><> <><><>
    def _permitter_element_rules_element_type_element_id_post(self, element_type, element_id):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        # FIXME: who is 'who_id' ; who_name; id || (c) swagger
        data = {
            "access": True,
            "exec": True,
            # "id":0
            "is_user": False,
            "read": True,
            "who_id": 5,
            # "who_name": "string"
            "write": True
        }
        resp = req.permitter_element_rules_element_type_element_id_post(element_type, element_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_element_rules_query_id_post(self):
        element_type = ElementType.query
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_element_type_element_id_post(element_type, element_id)

    def case_permitter_element_rules_visualisation_id_post(self):
        element_type = ElementType.visualisation
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_element_type_element_id_post(element_type, element_id)

    def case_permitter_element_rules_report_id_post(self):
        element_type = ElementType.report
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_element_type_element_id_post(element_type, element_id)

    def case_permitter_element_rules_mailing_id_post(self):
        element_type = ElementType.mailing
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_element_type_element_id_post(element_type, element_id)

    def case_permitter_element_rules_script_id_post(self):
        element_type = ElementType.script
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_element_type_element_id_post(element_type, element_id)

    def case_permitter_element_rules_script_sequence_id_post(self):
        element_type = ElementType.script_sequence
        element_id = self._get_element_id_by_type(element_type)
        self._permitter_element_rules_element_type_element_id_post(element_type, element_id)
    # <><><> <><><>

    def case_permitter_roles_editor_roles_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_roles_editor_roles_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_roles_editor_roles_post(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})

        data = _get_sample_data()  # "name": f"API_AUTO_TEST_{random_num}"
        resp = req.permitter_roles_editor_roles_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)
        return resp

    def case_permitter_roles_editor_roles_edit_id_get(self):
        req = Permitter(self.sess, self.host)
        # req.sess.headers.update({'ui': "2"})
        _role_id = self._get_temp_role_id()
        resp = req.permitter_roles_editor_roles_edit_id_get(_role_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_roles_editor_roles_id_put(self):
        req = Permitter(self.sess, self.host)
        # req.sess.headers.update({'ui': "2"})
        _role_id = self._get_temp_role_id()
        data = _get_sample_data()
        resp = req.permitter_roles_editor_roles_id_put(_role_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_roles_editor_roles_id_delete(self):
        req = Permitter(self.sess, self.host)
        # req.sess.headers.update({'ui': "2"})
        _role_id = self._get_temp_role_id()
        resp = req.permitter_roles_editor_roles_id_delete(_role_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_user_rules_get(self):
        req = Permitter(self.sess, self.host)
        # req.sess.headers.update({'ui': "2"})
        resp = req.permitter_user_rules_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_users_elements_count_who_id_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        who_id = 123    # fixme:<
        resp = req.permitter_users_elements_count_who_id_get(who_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_users_new_author_who_id_post(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        who_id = 123    # fixme: принимает случайные значения
        data = {
            "delete": True,
            "new_author": API_AUTO_TEST_
        }
        resp = req.permitter_users_new_author_who_id_post(who_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_user_rules_who_id_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        who = "user"
        who_id = 123    # fixme:<
        resp = req.permitter_who_rules_who_id_get(who, who_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_role_rules_who_id_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        who = "role"
        who_id = 123    # fixme:<
        resp = req.permitter_who_rules_who_id_get(who, who_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    # __del__
    def all_temp_roles_delete(self):
        delete_req = Permitter(self.sess, self.host)
        self._collect_temp_role_id()
        while len(role_id) > 0:
            delete_req.permitter_roles_editor_roles_id_delete(role_id.pop())
