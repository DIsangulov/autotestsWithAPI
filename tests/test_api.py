import json
import pytest
import requests
import testit
import urllib3

from self import self

from req.Api.req_auth import AuthApi
from req.Helpers.base_req import BaseReq
from req.Api.req_absorber import Absorber
from req.Api.req_alarmer import Alarmer
from req.Api.req_core import Core
from req.Api.req_licenser import Licenser
from req.Api.req_peopler import Peopler

urllib3.disable_warnings()
# ________Constants________
sess = requests.Session()
host = "https://10.130.0.22"
# ________Constants________

# _________Globals_________
auth_token = None
uid = None
user_id = None


# _________Globals_________

@pytest.mark.skip
class TestAuth:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']

    def test_ad_struct(self):
        req = AuthApi(sess, host)
        resp = req.ad_struct(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_ou_users(self):
        req = AuthApi(sess, host)
        resp = req.ou_users(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions(self):
        req = AuthApi(sess, host)
        resp = req.sessions(auth_token)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions_uid(self):
        req = AuthApi(sess, host)
        resp = req.sessions_uid(auth_token)

        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions_one_sid_del(self):  # sid вкорячен в req_auth в метод sessions_one_sid_del
        req = AuthApi(sess, host)
        resp = req.sessions_one_sid_del(auth_token)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions_all_uid_del(self):
        self.test_get_token()
        req = AuthApi(sess, host)
        resp = req.sessions_all_uid_del(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # __________________________________LOGOUT_______________________________________

    def test_logout(self):
        self.test_get_token()
        req = AuthApi(sess, host)
        resp = req.sessions(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # __________________________________ABSORBER_______________________________________


@pytest.mark.skip
class TestAbsorber:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']
        print(auth_token)

    def test_library_columns(self):
        req = Absorber(sess, host)
        resp = req.library_columns(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_conn_type(self):
        req = Absorber(sess, host)
        resp = req.library_conn_type(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_conn_type_id(self):
        req = Absorber(sess, host)
        resp = req.library_conn_type_id(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_connector(self):  # получаем список всех коннекторов
        req = Absorber(sess, host)
        resp = req.library_connector(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_connector_post(self):
        req = Absorber(sess, host)
        resp = req.library_connector_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_connector_put(self):
        req = Absorber(sess, host)
        resp = req.library_connector_put(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_connector_get(self):
        req = Absorber(sess, host)
        resp = req.library_connector_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_connector_delete(self):
        req = Absorber(sess, host)
        resp = req.library_connector_delete(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_logo_get(self):
        req = Absorber(sess, host)
        resp = req.library_logo_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_logo_post(self):
        req = Absorber(sess, host)
        resp = req.library_logo_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_logo_put(self):
        req = Absorber(sess, host)
        resp = req.library_logo_put(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_logo_delete(self):
        req = Absorber(sess, host)
        resp = req.library_logo_delete(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_source_get(self):
        req = Absorber(sess, host)
        resp = req.source_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_source_post(self):  # тут какая-то задница
        req = Absorber(sess, host)
        resp = req.source_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


@pytest.mark.skip
class TestAlarmer:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']
        print(auth_token)

    def test_alarmer_notification_admin_all(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_admin_all(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_read_admin(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_admin_all(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_read_type_admin(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_read_type_user(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_admin(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_settings_admin(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_common_get(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_settings_common_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_common_post(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_settings_common_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_user_get(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_settings_user_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_userone_post(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_settings_userone_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_type_post(self):  # проблемный
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_settings_type_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_user_all(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_settings_user_all(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_user(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_user(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_send_invitation(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_send_invitation(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_send_invitations(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_send_invitations(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_send_msg(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_send_msg(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


@pytest.mark.skip
class TestCore:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']
        print(auth_token)

    def test_core_active_directory_get(self):
        req = Core(sess, host)
        resp = req.core_active_directory_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_active_directory_post(self):
        req = Core(sess, host)
        resp = req.core_active_directory_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_active_directory_structure_post(self):
        req = Core(sess, host)
        resp = req.core_active_directory_structure_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_active_directory_test_settings_post(self):
        req = Core(sess, host)
        resp = req.core_active_directory_test_settings_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_backups(self):
        req = Core(sess, host)
        resp = req.core_check(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_common_get(self):
        req = Core(sess, host)
        resp = req.core_common_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_common_post(self):
        req = Core(sess, host)
        resp = req.core_common_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_common_test_post(self):
        req = Core(sess, host)
        resp = req.core_common_test_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_component_ml_restart(self):
        req = Core(sess, host)
        resp = req.core_component_ml_restart(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_component_picker_restart(self):
        req = Core(sess, host)
        resp = req.core_component_picker_restart(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_component_servicedb_restart(self):  # считаем 400 ответ правильным, система не даст перезапустить
        req = Core(sess, host)
        resp = req.core_component_servicedb_restart(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_component_datastore_restart(self):  # считаем 400 ответ правильным, система не даст перезапустить
        req = Core(sess, host)
        resp = req.core_component_datastore_restart(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_download_settings(self):
        req = Core(sess, host)
        resp = req.core_download_settings(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_send_test(self):
        req = Core(sess, host)
        resp = req.core_send_test(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_email_in_get(self):
        req = Core(sess, host)
        resp = req.core_email_in_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_email_out_get(self):
        req = Core(sess, host)
        resp = req.core_email_out_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_email_in_post(self):
        req = Core(sess, host)
        resp = req.core_email_out_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_email_out_post(self):
        req = Core(sess, host)
        resp = req.core_email_in_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_flag(self):
        req = Core(sess, host)
        resp = req.core_flag(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_ip(self):
        req = Core(sess, host)
        resp = req.core_flag(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_list_ml_get(self):
        req = Core(sess, host)
        resp = req.core_nodes_list_ml_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_list_picker_get(self):
        req = Core(sess, host)
        resp = req.core_nodes_list_picker_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_list_servicedb_get(self):
        req = Core(sess, host)
        resp = req.core_nodes_list_servicedb_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_list_datastore_get(self):
        req = Core(sess, host)
        resp = req.core_nodes_list_datastore_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_ml_get(self):
        req = Core(sess, host)
        resp = req.core_nodes_ml_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_picker_get(self):
        req = Core(sess, host)
        resp = req.core_nodes_picker_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_servicedb_get(self):
        req = Core(sess, host)
        resp = req.core_nodes_servicedb_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_datastore_get(self):
        req = Core(sess, host)
        resp = req.core_nodes_datastore_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_test_datastore(self):
        req = Core(sess, host)
        resp = req.core_nodes_test_datastore_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_datastore_post(self):
        req = Core(sess, host)
        resp = req.core_nodes_datastore_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_datastore_delete(self):
        req = Core(sess, host)
        resp = req.core_nodes_datastore_delete(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_alarmer(self):
        req = Core(sess, host)
        resp = req.core_service_dp_alarmer(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_auth(self):
        req = Core(sess, host)
        resp = req.core_service_dp_auth(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_core(self):
        req = Core(sess, host)
        resp = req.core_service_dp_core(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_licenser(self):
        req = Core(sess, host)
        resp = req.core_service_dp_licenser(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_log_eater(self):
        req = Core(sess, host)
        resp = req.core_service_dp_log_eater(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_monitor(self):
        req = Core(sess, host)
        resp = req.core_service_dp_monitor(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_peopler(self):
        req = Core(sess, host)
        resp = req.core_service_dp_peopler(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_permitter(self):
        req = Core(sess, host)
        resp = req.core_service_dp_permitter(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_postgres_single(self):
        req = Core(sess, host)
        resp = req.core_service_dp_postgres_single(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_taskplan(self):
        req = Core(sess, host)
        resp = req.core_service_dp_taskplan(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_updater(self):
        req = Core(sess, host)
        resp = req.core_service_dp_updater(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_absorber(self):
        req = Core(sess, host)
        resp = req.core_service_dp_absorber(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_picker(self):
        req = Core(sess, host)
        resp = req.core_service_dp_picker(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_storage_single(self):
        req = Core(sess, host)
        resp = req.core_service_dp_storage_single(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_storage_worker(self):
        req = Core(sess, host)
        resp = req.core_service_dp_storage_worker(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_ml(self):
        req = Core(sess, host)
        resp = req.core_service_dp_ml(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_scripter(self):
        req = Core(sess, host)
        resp = req.core_service_dp_scripter(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_datapie_baker(self):
        req = Core(sess, host)
        resp = req.core_service_dp_datapie_baker(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_elements_eater(self):
        req = Core(sess, host)
        resp = req.core_service_dp_elements_eater(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_frontend(self):
        req = Core(sess, host)
        resp = req.core_service_dp_frontend(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_reporter(self):
        req = Core(sess, host)
        resp = req.core_service_dp_reporter(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_rm_cook(self):
        req = Core(sess, host)
        resp = req.core_service_dp_rm_cook(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_rm_ml(self):
        req = Core(sess, host)
        resp = req.core_service_dp_rm_ml(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_screener(self):
        req = Core(sess, host)
        resp = req.core_service_dp_screener(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_visualisation(self):
        req = Core(sess, host)
        resp = req.core_service_dp_visualisation(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_xba_cook(self):
        req = Core(sess, host)
        resp = req.core_service_dp_xba_cook(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_xba_py(self):
        req = Core(sess, host)
        resp = req.core_service_dp_xba_py(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_core_service_all_restart(self):  # стенд не тянет этот метод!
        req = Core(sess, host)
        resp = req.core_service_all_restart(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_sid(self):
        req = Core(sess, host)
        resp = req.core_sid(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_syslog_get(self):
        req = Core(sess, host)
        resp = req.core_syslog_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_syslog_post(self):
        req = Core(sess, host)
        resp = req.core_syslog_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


@pytest.mark.skip
class TestLicenser:
    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']
        print(auth_token)

    def test_licenser_activate(self):
        req = Licenser(sess, host)
        resp = req.licenser_activate(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_licenser_license_info(self):
        req = Licenser(sess, host)
        resp = req.licenser_license_info(auth_token)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestPeopler:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']
        print(auth_token)

    @testit.displayName("peopler_many_users_put")
    @testit.externalID("peopler_many_users_put")
    @testit.workItemID(1959)
    def test_peopler_many_users_put(self):
        req = Peopler(sess, host)
        resp = req.peopler_many_users_put(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_peopler_many_users_post(self):
        req = Peopler(sess, host)
        resp = req.peopler_many_users_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @testit.displayName("peopler_profile_get")
    @testit.externalID("peopler_profile_get")
    @testit.workItemID(1961)
    def test_peopler_profile(self):
        req = Peopler(sess, host)
        resp = req.peopler_profile(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @testit.displayName("peopler_profiles_get")
    @testit.externalID("peopler_profiles_get")
    @testit.workItemID(1962)
    def test_peopler_profiles(self):
        req = Peopler(sess, host)
        resp = req.peopler_profiles(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @testit.displayName("peopler_users_get")
    @testit.externalID("peopler_users_get")
    @testit.workItemID(1963)
    def test_peopler_users_get(self):
        req = Peopler(sess, host)
        resp = req.peopler_users_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @testit.displayName("peopler_users_post")
    @testit.externalID("peopler_users_post")
    @testit.workItemID(1964)
    def test_peopler_users_post(self):
        req = Peopler(sess, host)
        resp = req.peopler_users_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @testit.displayName("peopler_users_id_get")
    @testit.externalID("peopler_users_id_get")
    @testit.workItemID(1965)
    def test_peopler_users_id_get(self):
        req = Peopler(sess, host)
        resp = req.peopler_users_id_get(auth_token)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @testit.displayName("peopler_users_id_put")
    @testit.externalID("peopler_users_id_put")
    @testit.workItemID(1966)
    def test_peopler_users_id_put(self):
        req = Peopler(sess, host)
        resp = req.peopler_users_id_put(auth_token)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @testit.displayName("peopler_users_delete")
    @testit.externalID("peopler_users_delete")
    @testit.workItemID(1967)
    def test_peopler_users_delete(self):
        req = Peopler(sess, host)
        resp = req.peopler_users_delete(auth_token)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
