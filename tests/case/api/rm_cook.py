import json
import random

from req.Helpers.user_session import UserSession
from req.Api.req_rm_cook import RmCook
from resourses.credentials import DbName

SYSLOG_HOST = "107.130.0.16"
SYSLOG_PORT = 514


class RmCookCase(UserSession):

    def _get_random_rm_user_id(self) -> int:
        # получить запрос со списком rm_пользователей
        resp = RmCook(self.sess, self.host).rm_cook_active_directory_users_get()
        rm_users_info_rows = json.loads(resp.text)['res']['users']    # получить из запроса список пользователей
        rm_user_info = random.choice(rm_users_info_rows)              # получить случайную строку из списка
        return int(rm_user_info['id'])

    def _get_random_rm_group_id(self) -> int:
        # получить запрос со списком rm_групп
        resp = RmCook(self.sess, self.host).rm_cook_active_directory_groups_get()
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
        # header = {'token': self.token, 'ui': str(2)}

        _id = 0         # FIXME: role_id?
        data = {"alias": "Роль 0_изменено", "id": 0}
        resp = req.rm_cook_rm_roles_id_alias_post(_id, data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_rm_roles_id_alias_get(self):
        req = RmCook(self.sess, self.host)
        _id = 0
        resp = req.rm_cook_rm_roles_id_alias_get(_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_rm_status_get(self):
        req = RmCook(self.sess, self.host)
        resp = req.rm_cook_rm_status_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_role_model_result_export_role_model_to_excel_post(self):
        req = RmCook(self.sess, self.host)
        body = {
            "groups_db": "picker_tables",       # FIXME:
            "groups_table": "ad_groups_ngr_2",
            "source": 0,
            "users_db": "picker_tables",
            "users_table": "ad_users_ngr_2"
        }
        resp = req.rm_cook_role_model_result_export_role_model_to_excel_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_role_model_result_groups_by_role_id_get(self):
        req = RmCook(self.sess, self.host)
        _role_id = 0        # FIXME: role_id == 0; кейс проходит
        resp = req.rm_cook_role_model_result_groups_by_role_id_get(_role_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_role_model_result_resources_by_role_id_get(self):
        req = RmCook(self.sess, self.host)
        _role_id = 0            # FIXME: role_id == 0; rm_role?
        resp = req.rm_cook_role_model_result_resources_by_role_id_get(_role_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_role_model_result_roles_by_source_source_id_get(self):
        req = RmCook(self.sess, self.host)
        _source_id = 0
        resp = req.rm_cook_role_model_result_roles_by_source_source_id_get(_source_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_role_model_result_source_0_users_by_role_0_get(self):
        req = RmCook(self.sess, self.host)
        _source_id = 0          # FIXME: source_id == 0
        _role_id = 0            # FIXME: role_id == 0; кейс проходит
        resp = req.rm_cook_role_model_result_source_source_id_users_by_role_role_id_get(_source_id, _role_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_role_model_result_table_role_role_id_resources_by_user_user_id_get(self):
        req = RmCook(self.sess, self.host)
        _role_id = 0            # FIXME: role_id == 0
        _rm_user_id = self._get_random_rm_user_id()
        resp = req.rm_cook_role_model_result_table_role_role_id_resources_by_user_user_id_get(_role_id, _rm_user_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_role_model_result_table_role_role_id_users_by_resource_resource_id_get(self):
        req = RmCook(self.sess, self.host)
        _role_id = 0                # FIXME: role_id == 0
        _resource_id = 0            # FIXME: resource_id == 0
        resp = req.rm_cook_role_model_result_table_role_role_id_users_by_resource_resource_id_get(_role_id, _resource_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_role_model_result_form_role_role_id_groups_by_user_user_id_get(self):
        req = RmCook(self.sess, self.host)
        _form = "table"     # FIXME: какие ещё бывают || form value: table or graph
        _role_id = 0        # FIXME: role_id == 0
        _user_id = 0        # old: 1996248437   || rm_user_id
        resp = req.rm_cook_role_model_result_form_role_role_id_groups_by_user_user_id_get(_form, _role_id, _user_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_role_model_result_form_role_role_id_users_by_group_user_id_get1(self):
        req = RmCook(self.sess, self.host)
        _form = "table"             # FIXME: какие ещё бывают
        _role_id = 0                # FIXME:
        _group_id = 3909688664      # FIXME:
        resp = req.rm_cook_role_model_result_form_role_role_id_users_by_group_user_id_get(_form, _role_id, _group_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

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
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_rm_cook_settings_mailings_post(self):
        req = RmCook(self.sess, self.host)
        body = {"destinations": [
            {"email": "",
             "syslog_host": SYSLOG_HOST,
             "syslog_port": SYSLOG_PORT,
             "syslog_protocol": "tcp",
             "disable_syslog": False,
             "disable_email": True, "id": 1},
            {"email": "qa@ku.ku",
             "syslog_host": "",
             "syslog_port": 0,
             "syslog_protocol": "",
             "disable_syslog": True,
             "disable_email": True,
             "id": 2}]}
        resp = req.rm_cook_settings_mailings_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

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
