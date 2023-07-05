import json
import random

from req.Helpers.base_req import BaseReq
from req.Api.req_permitter import PermitterNew


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


class PermitterCase(BaseReq):

    def _get_temp_role_id(self) -> int:
        if len(role_id) == 0:   # global role_id
            self.permitter_roles_editor_roles_post()
        return role_id[-1]

    def _get_random_tab_id(self) -> int:
        header = {'token': self.token, 'ui': str(2)}
        resp = self.sess.get(f"{self.host}/back/dp.permitter/db_watcher/all_tables", headers=header, verify=False)
        dct = json.loads(resp.text)
        return dct['res'][1]['id']

    def case_permitter_check_ui_get(self):
        req = PermitterNew(self.sess, self.host)
        resp = req.permitter_check_ui_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_db_watcher_all_db_get(self):
        req = PermitterNew(self.sess, self.host)

        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_db_watcher_all_db_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_db_watcher_all_tables_get(self):
        req = PermitterNew(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_db_watcher_all_tables_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_db_watcher_db_tables_id_get(self):
        req = PermitterNew(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        _id = 1
        resp = req.permitter_db_watcher_db_tables_id_get(_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_db_watcher_empty_role_dbs_get(self):
        req = PermitterNew(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_db_watcher_empty_role_dbs_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_db_watcher_empty_role_tables_get(self):
        req = PermitterNew(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_db_watcher_empty_role_tables_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_db_watcher_empty_role_tables_id_get(self):
        req = PermitterNew(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        _id = 1
        resp = req.permitter_db_watcher_empty_role_tables_id_get(_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_db_watcher_get_tab_name_id_get(self):
        req = PermitterNew(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        tab_id = self._get_random_tab_id()
        resp = req.permitter_db_watcher_get_tab_name_id_get(tab_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    # <><><> <><><>
    def _permitter_element_flags_element_type_element_id_get(self, element_type, element_id):
        req = PermitterNew(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_element_flags_element_type_element_id_get(element_type, element_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_element_flags_query_id_get(self):
        element_type = "query"
        element_id = 123    # FIXME:
        self._permitter_element_flags_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_flags_visualisation_id_get(self):
        element_type = "visualisation"
        element_id = 260    # FIXME:
        self._permitter_element_flags_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_flags_report_id_get(self):
        element_type = "report"
        element_id = 4      # FIXME:
        self._permitter_element_flags_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_flags_mailing_id_get(self):
        element_type = "mailing"
        element_id = 428      # FIXME:
        self._permitter_element_flags_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_flags_script_id_get(self):
        element_type = "script"
        element_id = 25        # FIXME:
        self._permitter_element_flags_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_flags_script_sequence_id_get(self):
        element_type = "script_sequence"
        element_id = 25         # FIXME:    # ?! прошел на несуществующем element_id
        self._permitter_element_flags_element_type_element_id_get(element_type, element_id)
    # <><><> <><><>

    # <><><> <><><>
    def _permitter_element_flags_element_type_element_id_post(self, element_type, element_id):
        req = PermitterNew(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        data = {
            "opened": True,
            "published": True
        }
        resp = req.permitter_element_flags_element_type_element_id_post(element_type, element_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)    # 200, при попытке изменить свой 'element', 400 - чужой

    def case_permitter_element_flags_query_id_post(self):
        element_type = "query"
        element_id = 139        # FIXME:
        self._permitter_element_flags_element_type_element_id_post(element_type, element_id)

    def case_permitter_element_flags_visualisation_id_post(self):
        element_type = "visualisation"
        element_id = 281        # FIXME:
        self._permitter_element_flags_element_type_element_id_post(element_type, element_id)

    def case_permitter_element_flags_report_id_post(self):
        element_type = "report"
        element_id = 397        # FIXME:
        self._permitter_element_flags_element_type_element_id_post(element_type, element_id)

    def case_permitter_element_flags_mailing_id_post(self):
        element_type = "mailing"
        element_id = 480        # FIXME:
        self._permitter_element_flags_element_type_element_id_post(element_type, element_id)

    def case_permitter_element_flags_script_id_post(self):
        element_type = "script"
        element_id = 344        # FIXME:
        self._permitter_element_flags_element_type_element_id_post(element_type, element_id)

    def case_permitter_element_flags_script_sequence_id_post(self):
        element_type = "script_sequence"
        element_id = 81         # FIXME:
        self._permitter_element_flags_element_type_element_id_post(element_type, element_id)
    # <><><> <><><>

    # <><><> <><><>
    def _permitter_element_rules_all_element_type_element_id_get(self, element_type, element_id):
        req = PermitterNew(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        resp = req.permitter_element_rules_all_element_type_element_id_get(element_type, element_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_permitter_element_rules_all_query_id_get(self):
        element_type = "query"
        element_id = 139        # FIXME
        self._permitter_element_rules_all_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_rules_all_visualisation_id_get(self):
        element_type = "visualisation"
        element_id = 281        # FIXME
        self._permitter_element_rules_all_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_rules_all_report_id_get(self):
        element_type = "report"
        element_id = 397        # FIXME
        self._permitter_element_rules_all_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_rules_all_mailing_id_get(self):
        element_type = "mailing"
        element_id = 480        # FIXME
        self._permitter_element_rules_all_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_rules_all_script_id_get(self):
        element_type = "script"
        element_id = 344        # FIXME
        self._permitter_element_rules_all_element_type_element_id_get(element_type, element_id)

    def case_permitter_element_rules_all_script_sequence_id_get(self):
        element_type = "script_sequence"
        element_id = 81         # FIXME
        self._permitter_element_rules_all_element_type_element_id_get(element_type, element_id)
    # <><><> <><><>
