import json
import random

from req.Helpers.user_session import UserSession
from req.Api.req_permitter import Permitter
from resourses.constants import API_AUTO_TEST_
from tests.case.api.peopler import PeoplerCase
from tests.case.api.reporter import ReporterCase
from tests.case.api.scripter import ScripterCase
from tests.case.api.visualisation import VisualisationCase


test_role_id = set()


class ElementType:
    query = "query"
    visualisation = "visualisation"
    report = "report"
    mailing = "mailing"
    script = "script"
    script_sequence = "script_sequence"


class PermitterCase(UserSession):

    def _get_element_id_by_type(self, element_type) -> int:
        match element_type:
            case ElementType.query:
                return VisualisationCase().get_query_id()
            case ElementType.visualisation:
                return VisualisationCase().get_visualisation_id()
            case ElementType.report:
                return VisualisationCase().get_report_id()
            case ElementType.mailing:
                return ReporterCase().get_mailing_id()
            case ElementType.script:
                return ScripterCase().get_script_id()
            case ElementType.script_sequence:
                return ScripterCase().get_sequence_id()
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
                test_role_id.add(int(_row['id']))

    def _get_test_role_id(self) -> int:
        if len(test_role_id) == 0:
            self._collect_temp_role_id()

        if len(test_role_id) == 0:   # global role_id
            r_new_role = self.case_permitter_roles_editor_roles_post()  # создать новую роль
            new_role_id = json.loads(r_new_role.text)['res']
            return int(new_role_id)

        return test_role_id.pop()

    def _get_random_tab_id(self) -> int:
        # header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/all_tables")
        dct = json.loads(resp.text)
        return dct['res'][1]['id']

    def add_role_permission_to_change_db(self, role_id: int, db_name: str):
        """Дать доступ роли 'role_id' на просмотр и изменение хранилища 'db_name'"""

        db_id = self.get_db_id_by_name(db_name)

        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': '2'})

        current_data_resp = req.permitter_roles_editor_roles_edit_id_get(role_id)
        assert current_data_resp.status_code == 200, f"Ошибка, код {current_data_resp.status_code}, {current_data_resp.text}"

        current_data: dict = json.loads(current_data_resp.text)["res"]
        current_data.update({
            "dbs": [{
                "id": db_id,
                # "name": "string",
                "db_id": 0,
                "select": True,
                "update": True
            }]
        })

        resp = req.permitter_roles_editor_roles_id_put(role_id, current_data)
        assert resp.status_code == 200, \
            f"""
            status_code: {resp.status_code}
            role_id: {role_id}
            db_name: {db_name}
            post_data: {current_data}
            resp = {resp.text}
            """

    def case_permitter_check_ui_get(self):
        req = Permitter(self.sess, self.host)
        resp = req.permitter_check_ui_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_permitter_db_watcher_all_db_get(self):
        req = Permitter(self.sess, self.host)

        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_db_watcher_all_db_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_permitter_db_watcher_all_tables_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_db_watcher_all_tables_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_permitter_db_watcher_db_tables_id_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        _id = 1
        resp = req.permitter_db_watcher_db_tables_id_get(_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_permitter_db_watcher_empty_role_dbs_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_db_watcher_empty_role_dbs_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_permitter_db_watcher_empty_role_tables_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_db_watcher_empty_role_tables_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_permitter_db_watcher_empty_role_tables_id_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        _id = 1
        resp = req.permitter_db_watcher_empty_role_tables_id_get(_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_permitter_db_watcher_get_tab_name_id_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        tab_id = self._get_random_tab_id()
        resp = req.permitter_db_watcher_get_tab_name_id_get(tab_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_permitter_element_flags_element_type_element_id_get(self, element_type):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})

        element_id = self._get_element_id_by_type(element_type)

        resp = req.permitter_element_flags_element_type_element_id_get(element_type, element_id)
        # print(f"e_type: {element_type}, e_id: {element_id}, rtext: {resp.text}")
        assert resp.status_code == 200, \
            f"""
            status_code: {resp.status_code}
            element_type: {element_type}
            element_id: {element_id}
            resp = {resp.text}
            """

    def case_permitter_element_flags_element_type_element_id_post(self, element_type):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})

        element_id = self._get_element_id_by_type(element_type)
        post_data = {
            "opened": False,
            "published": False
        }

        resp = req.permitter_element_flags_element_type_element_id_post(element_type, element_id, post_data)
        # print(f"e_type: {element_type}, e_id: {element_id}, rtext: {resp.text}")
        # 200, при попытке изменить свой 'element', 400 - чужой
        assert resp.status_code == 200, \
            f"""
            status_code: {resp.status_code}
            element_type: {element_type}
            element_id: {element_id}
            post_data = {post_data}
            resp = {resp.text}
            """

    def case_permitter_element_rules_all_element_type_element_id_get(self, element_type):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})

        element_id = self._get_element_id_by_type(element_type)
        # element_id = 12345  # look: возвращает 200 с любым int значением element_id

        resp = req.permitter_element_rules_all_element_type_element_id_get(element_type, element_id)
        assert resp.status_code == 200, \
            f"""
            status_code: {resp.status_code}
            element_type: {element_type}
            element_id: {element_id}
            resp = {resp.text}
            """

    def case_permitter_element_rules_delete_element_type_element_id_post(self, element_type):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})

        element_id = self._get_element_id_by_type(element_type)
        post_data = {
            "access": True,
            "exec": True,
            # "id": element_id,
            "is_user": False,
            "who_id": 5,
            "read": True,
            "write": True
        }

        resp = req.permitter_element_rules_delete_element_type_element_id_post(element_type, element_id, post_data)
        assert resp.status_code == 200, \
            f"""
            status_code: {resp.status_code}
            element_type: {element_type}
            element_id: {element_id}
            post_data = {post_data}
            resp = {resp.text}
            """

    def case_permitter_element_rules_element_type_element_id_get(self, element_type):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})

        element_id = self._get_element_id_by_type(element_type)
        # element_id = 12345   # look: возвращает 200 с любым int значением element_id; query_id = 123456

        resp = req.permitter_element_rules_element_type_element_id_get(element_type, element_id)
        # print(f"e_type: {element_type}, e_id: {element_id}, rtext: {resp.text}")
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_permitter_element_rules_element_type_element_id_post(self, element_type):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})

        element_id = self._get_element_id_by_type(element_type)

        post_data = {
            "access":   True,
            "exec":     True,
            # "id":0,
            "is_user":  False,
            "who_id":   5,  # who_id: user or role id
            # "who_name": "string"  # who_name: user or role name
            "read":     True,
            "write":    True
        }
        resp = req.permitter_element_rules_element_type_element_id_post(element_type, element_id, post_data)
        assert resp.status_code == 200, \
            f"""
            status_code: {resp.status_code}
            element_type: {element_type}
            element_id: {element_id}
            post_data = {post_data}
            resp = {resp.text}
            """

    def case_permitter_roles_editor_roles_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_roles_editor_roles_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # DAT-4766  # Проверка наличия поля "user_count" в ответе
        resp_res_list = json.loads(resp.text)['res']
        for _row in resp_res_list:
            _row: dict
            _search_field = "user_count"
            assert _search_field in _row, f"Нет поля '{_search_field}' в 'res': [{_row}, ...]"

    def case_permitter_roles_editor_roles_post(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})

        post_data = {
            "name": f"{API_AUTO_TEST_}{random.randint(100, 999)}",
            "views": [
                {"ui_part": "administration",   "read": False, "write": False},
                {"ui_part": "data",             "read": False, "write": False},
                {"ui_part": "analytics",        "read": False, "write": False},
                {"ui_part": "xba",              "read": False, "write": False},
                {"ui_part": "rm",               "read": False, "write": False}
            ]}

        resp = req.permitter_roles_editor_roles_post(post_data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        return resp

    def case_permitter_roles_editor_roles_edit_id_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        role_id = self._get_test_role_id()
        resp = req.permitter_roles_editor_roles_edit_id_get(role_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_permitter_roles_editor_roles_id_put(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        role_id = self._get_test_role_id()

        post_data = {
            "name": f"{API_AUTO_TEST_}CHANGED_{random.randint(100, 999)}",
            "views": [
                {"ui_part": "administration",   "read": False, "write": False},
                {"ui_part": "data",             "read": False, "write": False},
                {"ui_part": "analytics",        "read": False, "write": False},
                {"ui_part": "xba",              "read": False, "write": False},
                {"ui_part": "rm",               "read": False, "write": False}
            ]}

        resp = req.permitter_roles_editor_roles_id_put(role_id, post_data)
        assert resp.status_code == 200, f"""
        status_code: {resp.status_code}
        role_id: {role_id}
        post_data = {post_data}
        resp = {resp.text}
        """

    def case_permitter_roles_editor_roles_id_delete(self):
        req = Permitter(self.sess, self.host)
        # req.sess.headers.update({'ui': "2"})
        role_id = self._get_test_role_id()
        resp = req.permitter_roles_editor_roles_id_delete(role_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_permitter_user_rules_get(self):
        req = Permitter(self.sess, self.host)
        # req.sess.headers.update({'ui': "2"})
        resp = req.permitter_user_rules_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_permitter_users_elements_count_who_id_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        who_id = self.get_self_user_id()
        resp = req.permitter_users_elements_count_who_id_get(who_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_permitter_users_new_author_who_id_post(self, who_id, post_data):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})

        # :delete: True - удалить личные элементы
        # :delete: False - Не удалять личные элементы
        # :new_author - id of new author    # как вариант self.get_self_user_id()
        # :new_author: None - Не назначать нового автора (личные элементы присваиваются системе и открыты + опубликованы)

        # look: who_id - id 'старого' пользователя; нет проверки на существование этого пользователя
        # who_id = PeoplerCase().get_auto_test_user_id()

        resp = req.permitter_users_new_author_who_id_post(who_id, post_data)
        assert resp.status_code == 200, \
            f"""Ошибка, 
            who_id: {who_id}
            post_data: {post_data}
            status_code: {resp.status_code}
            resp: {resp.text}"""

    def case_permitter_user_rules_who_id_get(self):
        req = Permitter(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        who = "user"
        who_id = PeoplerCase().get_test_user_id()   # 'user' id
        resp = req.permitter_who_rules_who_id_get(who, who_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_permitter_role_rules_who_id_get(self):
        req = Permitter(self.sess, self.host)
        # req.sess.headers.update({'ui': "2"})
        who = "role"
        who_id = self._get_test_role_id()   # 'role' id
        resp = req.permitter_who_rules_who_id_get(who, who_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # __del__
    def all_temp_roles_delete(self):
        delete_req = Permitter(self.sess, self.host)
        self._collect_temp_role_id()
        while len(test_role_id) > 0:
            delete_req.permitter_roles_editor_roles_id_delete(test_role_id.pop())
