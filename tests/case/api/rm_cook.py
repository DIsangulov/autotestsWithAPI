import json
import random

from req.Helpers.user_session import UserSession
from req.Api.req_rm_cook import RmCook
from resourses.constants import QA_SPAM_EMAIL, DB_picker_tables


class RmCookCase(UserSession):

    def _get_random_rm_user_id(self, *, rm_role_id: int = None) -> int:
        if rm_role_id is not None:
            resp = RmCook(self.sess, self.host).rm_cook_role_model_result_source_id_users_by_role_id_get(0, rm_role_id)
            assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

            rm_users_rows = json.loads(resp.text)['res']
            assert rm_users_rows != 0, f"Ошибка при получении /users_by_role: количество пользователей == 0: resp {resp.text}"
            return int(random.choice(rm_users_rows)['id'])
        else:
            # получить запрос со списком rm_пользователей
            resp = RmCook(self.sess, self.host).rm_cook_active_directory_users_get()
            assert resp.status_code == 200, f"Ошибка при получении списка AD users {resp.status_code}, {resp.text}"

            rm_users_info_rows = json.loads(resp.text)['res']['users']    # получить из запроса список пользователей
            assert len(rm_users_info_rows) != 0, f"Ошибка при получении списка AD users: количество пользователей == 0: resp: {resp.text}"

            rm_user_info = random.choice(rm_users_info_rows)              # получить случайную строку из списка
            return int(rm_user_info['id'])

    def _get_random_rm_group_id(self, *, rm_role_id: int = None) -> int:
        if rm_role_id is not None:
            resp = RmCook(self.sess, self.host).rm_cook_role_model_result_groups_by_role_id_get(rm_role_id)
            assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

            rm_groups_rows = json.loads(resp.text)['res']
            assert rm_groups_rows != 0, f"Ошибка при получении /groups_by_role: количество групп == 0: resp {resp.text}"
            return int(random.choice(rm_groups_rows)['id'])
        else:
            # получить запрос со списком rm_групп
            resp = RmCook(self.sess, self.host).rm_cook_active_directory_groups_get()
            assert resp.status_code == 200, f"Ошибка при получении списка AD groups {resp.status_code}, {resp.text}"

            rm_groups_info_rows = json.loads(resp.text)['res']['groups']  # получить из запроса список групп
            assert len(rm_groups_info_rows) != 0, f"Ошибка при получении списка AD groups: количество групп == 0: resp: {resp.text}"

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

    def case_rm_cook_active_directory_state_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_active_directory_state_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_active_directory_top_groups_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_active_directory_top_groups_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_active_directory_top_users_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_active_directory_top_users_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_active_directory_users_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_active_directory_users_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_active_directory_users_id_get(self):
        req = RmCook(self.sess, self.host)
        _rm_user_id = self._get_random_rm_user_id()
        resp = req.rm_cook_active_directory_users_id_get(_rm_user_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_calculation_start_calc_id_post(self):
        req = RmCook(self.sess, self.host)
        calc_id = 1
        resp = req.rm_cook_calculation_start_calc_id_post(calc_id)
        # код 429, задание уже запустили / идет расчет
        assert resp.status_code == 200 or 429, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_rm_logs_last_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_rm_logs_last_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_rm_recommendations_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_rm_recommendations_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_rm_roles_id_alias_post(self):
        req = RmCook(self.sess, self.host)

        role_id = 0
        data = {"alias": f"role_{role_id}_changed", "id": 0}
        resp = req.rm_cook_rm_roles_id_alias_post(role_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_rm_roles_id_alias_ts_get(self, rm_role_id, timestamp):
        req = RmCook(self.sess, self.host)

        # role_id - id роли в таблица бизнес-ролей
        # role_id <- /role_model/result/roles_by_source/0
        # timestamp = 0   # ? role (creation) timestamp

        resp = req.rm_cook_rm_roles_id_alias_ts_get(rm_role_id, timestamp)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_rm_status_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_rm_status_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_role_model_result_export_role_model_to_excel_post(self):
        req = RmCook(self.sess, self.host)

        # Получение источников RM   # front: /role-mining/settings/source
        sources_resp = req.rm_cook_settings_sources_get()
        assert sources_resp.status_code == 200, \
            f"""1.Ошибка при получении настроек RM:
            status_code: {sources_resp.status_code}
            resp: {sources_resp.text}"""

        sources_resp_rows = json.loads(sources_resp.text)['res']
        source_type_1_row: dict = next((src_row for src_row in sources_resp_rows if src_row["source_type"] == 1), None)
        source_type_2_row: dict = next((src_row for src_row in sources_resp_rows if src_row["source_type"] == 2), None)

        assert source_type_1_row is not None, "Ошибка парсинга RM источника"
        assert source_type_2_row is not None, "Ошибка парсинга RM источника"

        groups_db = source_type_1_row.get("db_name")
        groups_table = source_type_1_row.get("table_name")

        users_db = source_type_2_row.get("db_name")
        users_table = source_type_2_row.get("table_name")

        post_data = {
            "source": 0,

            "groups_db": groups_db,
            "groups_table": groups_table,

            "users_db": users_db,
            "users_table": users_table
        }
        # print(post_data)

        resp = req.rm_cook_role_model_result_export_role_model_to_excel_post(post_data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_role_model_result_groups_by_role_id_get(self, rm_role_id):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_role_model_result_groups_by_role_id_get(rm_role_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_role_model_result_resources_by_role_id_get(self):
        req = RmCook(self.sess, self.host)
        _role_id = 0
        resp = req.rm_cook_role_model_result_resources_by_role_id_get(_role_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_role_model_result_roles_by_source_id_get(self, rm_source_id):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_role_model_result_roles_by_source_id_get(rm_source_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_role_model_result_source_id_users_by_role_id_get(self, rm_source_id, rm_role_id):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_role_model_result_source_id_users_by_role_id_get(rm_source_id, rm_role_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_role_model_result_table_role_id_resources_by_user_id_get(self):
        req = RmCook(self.sess, self.host)
        rm_role_id = 0
        rm_user_id = self._get_random_rm_user_id()
        resp = req.rm_cook_role_model_result_table_role_id_resources_by_user_id_get(rm_role_id, rm_user_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_role_model_result_table_role_id_users_by_resource_id_get(self):
        req = RmCook(self.sess, self.host)
        _role_id = 0
        _resource_id = 0
        resp = req.rm_cook_role_model_result_table_role_id_users_by_resource_id_get(_role_id, _resource_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_role_model_result_form_role_id_groups_by_user_id_get(self, form):
        req = RmCook(self.sess, self.host)

        rm_role_id = 0
        rm_user_id = self._get_random_rm_user_id(rm_role_id=rm_role_id)

        resp = req.rm_cook_role_model_result_form_role_id_groups_by_user_id_get(form, rm_role_id, rm_user_id)
        assert resp.status_code == 200, \
            f"""form: {form}
            role_id: {rm_role_id}
            group_id: {rm_user_id}
            status_code: {resp.status_code}
            resp: {resp.text}"""

    def case_rm_cook_role_model_result_form_role_id_users_by_group_id_get1(self, form):
        req = RmCook(self.sess, self.host)

        rm_role_id = 0
        rm_group_id = self._get_random_rm_group_id(rm_role_id=rm_role_id)

        resp = req.rm_cook_role_model_result_form_role_id_users_by_group_id_get(form, rm_role_id, rm_group_id)
        assert resp.status_code == 200, \
            f"""form: {form}
            role_id: {rm_role_id}
            group_id: {rm_group_id}
            status_code: {resp.status_code}
            resp: {resp.text}"""

    def case_rm_cook_settings_calc_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_settings_calc_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_settings_calc_put(self):
        # front: /role-mining/settings/calc # Чисто ролей, которое необходимо получить
        req = RmCook(self.sess, self.host)
        _roles_num = 20
        body = {"roles_num": _roles_num}
        resp = req.rm_cook_settings_calc_put(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_settings_mailings_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_settings_mailings_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_settings_mailings_post(self):
        req = RmCook(self.sess, self.host)
        body = {
            "destinations": [
                {
                    "email": "",
                    "syslog_host": "127.0.0.1",
                    "syslog_port": 4445,
                    "syslog_protocol": "TCP",
                    "disable_syslog": False,
                    "disable_email": True,
                }, {
                    "email": QA_SPAM_EMAIL,
                    # "syslog_host": "",
                    # "syslog_port": 0,
                    "syslog_protocol": "",
                    "disable_syslog": True,
                    "disable_email": False,
                }
            ]
        }
        resp = req.rm_cook_settings_mailings_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_settings_sources_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_settings_sources_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_rm_cook_settings_sources_post(self):
        # front: /role-mining/settings/source   # Настройки Role mining
        req = RmCook(self.sess, self.host)

        db_name = DB_picker_tables.name
        db_id = self.get_db_id_by_name(DB_picker_tables.name)
        db_groups_table = "ad_groups_nested_medium"
        db_users_table = "ad_nested_users_medium_view"

        self.asserts_check_db_and_table_is_exists(db_name, db_groups_table)
        self.asserts_check_db_and_table_is_exists(db_name, db_users_table)

        post_data = [
            {"db_name": db_name, "db_id": db_id, "source_type": 1, "table_name": db_groups_table},
            {"db_name": db_name, "db_id": db_id, "source_type": 2, "table_name": db_users_table}
        ]
        resp = req.rm_cook_settings_sources_post(post_data)
        assert resp.status_code == 200, f"Ошибка, post_data: {post_data}, status_code: {resp.status_code}, resp: {resp.text}"
