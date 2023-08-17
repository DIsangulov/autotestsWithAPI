import json
import random

from req.Helpers.user_session import UserSession
from req.Api.req_rm_cook import RmCook
from resourses.credentials import DbName

_QA_SPAM_EMAIL = "s.yezhov@ngrsoftlab.ru"
SYSLOG_HOST = "107.130.0.16"
SYSLOG_PORT = 514


class RmCookCase(UserSession):

    def _get_random_rm_user_id(self, *, rm_role_id: int = None) -> int:
        if rm_role_id is not None:
            resp = RmCook(self.sess, self.host).rm_cook_role_model_result_source_source_id_users_by_role_role_id_get(0, rm_role_id)
            assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

            rm_users_rows = json.loads(resp.text)['res']
            return int(random.choice(rm_users_rows)['id'])
        else:
            # получить запрос со списком rm_пользователей
            resp = RmCook(self.sess, self.host).rm_cook_active_directory_users_get()
            assert resp.status_code == 200, f"Ошибка при получении списка AD users {resp.status_code}, {resp.text}"

            rm_users_info_rows = json.loads(resp.text)['res']['users']    # получить из запроса список пользователей
            rm_user_info = random.choice(rm_users_info_rows)              # получить случайную строку из списка
            return int(rm_user_info['id'])

    def _get_random_rm_group_id(self, *, rm_role_id: int = None) -> int:
        if rm_role_id is not None:
            resp = RmCook(self.sess, self.host).rm_cook_role_model_result_groups_by_role_id_get(rm_role_id)
            assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

            rm_groups_rows = json.loads(resp.text)['res']
            return int(random.choice(rm_groups_rows)['id'])
        else:
            # получить запрос со списком rm_групп
            resp = RmCook(self.sess, self.host).rm_cook_active_directory_groups_get()
            assert resp.status_code == 200, f"Ошибка при получении списка AD groups {resp.status_code}, {resp.text}"

            rm_groups_info_rows = json.loads(resp.text)['res']['groups']  # получить из запроса список групп
            rm_group_info = random.choice(rm_groups_info_rows)            # получить случайную строку из списка
            return int(rm_group_info['id'])

    def case_rm_cook_active_directory_groups_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_active_directory_groups_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_active_directory_groups_id_get(self):
        req = RmCook(self.sess, self.host)
        _rm_group_id = self._get_random_rm_group_id()
        resp = req.rm_cook_active_directory_groups_id_get(_rm_group_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_active_directory_state_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_active_directory_state_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_active_directory_top_groups_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_active_directory_top_groups_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_active_directory_top_users_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_active_directory_top_users_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_active_directory_users_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_active_directory_users_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_active_directory_users_id_get(self):
        req = RmCook(self.sess, self.host)
        _rm_user_id = self._get_random_rm_user_id()
        resp = req.rm_cook_active_directory_users_id_get(_rm_user_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_calculation_start_calc_id_post(self):
        req = RmCook(self.sess, self.host)
        calc_id = 1
        resp = req.rm_cook_calculation_start_calc_id_post(calc_id)
        # код 429, задание уже запустили / идет расчет
        assert resp.status_code == 200 or 429, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_rm_logs_last_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_rm_logs_last_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_rm_recommendations_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_rm_recommendations_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_rm_roles_id_alias_post(self):
        req = RmCook(self.sess, self.host)

        role_id = 0
        data = {"alias": "Роль 0_changed", "id": 0}
        resp = req.rm_cook_rm_roles_id_alias_post(role_id, data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_rm_roles_id_alias_ts_get(self):
        req = RmCook(self.sess, self.host)

        # role_id - id роли в таблица бизнес-ролей
        # role_id <- /role_model/result/roles_by_source/0

        # todo: 400: если не изменять alias вручную перед get
        # todo: different timestamp

        role_id = 0
        timestamp = 0

        resp = req.rm_cook_rm_roles_id_alias_ts_get(role_id, timestamp)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_rm_status_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_rm_status_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_role_model_result_export_role_model_to_excel_post(self):
        req = RmCook(self.sess, self.host)
        body = {
            "groups_db": DbName.picker_tables,
            "groups_table": "ad_groups_ngr_2",  # fixme
            "source": 0,
            "users_db": DbName.picker_tables,
            "users_table": "ad_users_ngr_2"  # fixme
        }
        resp = req.rm_cook_role_model_result_export_role_model_to_excel_post(body)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_role_model_result_groups_by_role_id_get(self):
        req = RmCook(self.sess, self.host)
        role_id = 0
        resp = req.rm_cook_role_model_result_groups_by_role_id_get(role_id)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_role_model_result_resources_by_role_id_get(self):
        # todo: where front:
        req = RmCook(self.sess, self.host)
        _role_id = 0
        resp = req.rm_cook_role_model_result_resources_by_role_id_get(_role_id)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_role_model_result_roles_by_source_source_id_get(self):
        req = RmCook(self.sess, self.host)
        _source_id = 0
        resp = req.rm_cook_role_model_result_roles_by_source_source_id_get(_source_id)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_role_model_result_source_0_users_by_role_0_get(self):
        req = RmCook(self.sess, self.host)
        _source_id = 0
        _role_id = 0
        resp = req.rm_cook_role_model_result_source_source_id_users_by_role_role_id_get(_source_id, _role_id)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_role_model_result_table_role_role_id_resources_by_user_user_id_get(self):
        req = RmCook(self.sess, self.host)
        rm_role_id = 0
        rm_user_id = self._get_random_rm_user_id()
        resp = req.rm_cook_role_model_result_table_role_role_id_resources_by_user_user_id_get(rm_role_id, rm_user_id)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_role_model_result_table_role_role_id_users_by_resource_resource_id_get(self):
        req = RmCook(self.sess, self.host)
        _role_id = 0
        _resource_id = 0            # FIXME: resource_id == 0
        resp = req.rm_cook_role_model_result_table_role_role_id_users_by_resource_resource_id_get(_role_id, _resource_id)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_role_model_result_form_role_role_id_groups_by_user_user_id_get(self):
        req = RmCook(self.sess, self.host)

        form_list = ("table", "graph")

        rm_role_id = 0
        # Получить пользователя, входящего в rm_role
        rm_user_id = self._get_random_rm_user_id(rm_role_id=rm_role_id)

        for form in form_list:
            resp = req.rm_cook_role_model_result_form_role_role_id_groups_by_user_user_id_get(form, rm_role_id, rm_user_id)
            # print(resp.text)
            assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_role_model_result_form_role_role_id_users_by_group_user_id_get1(self):
        req = RmCook(self.sess, self.host)

        form_list = ("table", "graph")

        rm_role_id = 0
        _group_id = self._get_random_rm_group_id(rm_role_id=rm_role_id)

        for form in form_list:
            resp = req.rm_cook_role_model_result_form_role_role_id_users_by_group_user_id_get(form, rm_role_id, _group_id)
            # print(resp.text)
            assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_settings_calc_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_settings_calc_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_settings_calc_put(self):
        req = RmCook(self.sess, self.host)
        _roles_num = 20
        body = {"roles_num": _roles_num}
        resp = req.rm_cook_settings_calc_put(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_settings_mailings_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_settings_mailings_get()
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_settings_mailings_post(self):
        req = RmCook(self.sess, self.host)
        body = {
            "destinations": [
                {
                    "email": "",
                    "syslog_host": SYSLOG_HOST,
                    "syslog_port": SYSLOG_PORT,
                    "syslog_protocol": "TCP",
                    "disable_syslog": False,
                    "disable_email": True,
                }, {
                    "email": _QA_SPAM_EMAIL,
                    # "syslog_host": "",
                    # "syslog_port": 0,
                    "syslog_protocol": "",
                    "disable_syslog": True,
                    "disable_email": False,
                }
            ]
        }
        resp = req.rm_cook_settings_mailings_post(body)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_settings_sources_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_settings_sources_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_settings_sources_post(self):
        req = RmCook(self.sess, self.host)
        db_picker_tables = self.get_db_id_by_name(DbName.picker_tables)
        body = [{"db_name": "picker_tables", "db_id": db_picker_tables, "source_type": 1, "table_name": "ad_groups_ngr"},
                {"db_name": "picker_tables", "db_id": db_picker_tables, "source_type": 2, "table_name": "ad_users_ngr"}]
        resp = req.rm_cook_settings_sources_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)
