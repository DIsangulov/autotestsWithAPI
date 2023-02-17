import json
import time

import allure
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
from req.Api.req_permitter import Permitter
from req.Api.req_rm_cook import Rm_Cook
from req.Api.req_storage_worker import StorageWorker
from req.Api.req_xba_cook import XbaCook
from utilities.logger import Logger

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

    @pytest.mark.skip
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

    @pytest.mark.skip
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
        resp = req.alarmer_notification_read_type_admin(auth_token)
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

    # def test_core_nodes_test_datastore(self):
    #     req = Core(sess, host)
    #     resp = req.core_nodes_test_datastore_post(auth_token)
    #     assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
    #
    # def test_core_nodes_datastore_post(self):
    #     req = Core(sess, host)
    #     resp = req.core_nodes_datastore_post(auth_token)
    #     assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
    #
    # def test_core_nodes_datastore_delete(self):
    #     req = Core(sess, host)
    #     resp = req.core_nodes_datastore_delete(auth_token)
    #     assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

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

    def test_licenser_activate(self):
        req = Licenser(sess, host)
        resp = req.licenser_activate(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_licenser_license_info(self):
        req = Licenser(sess, host)
        resp = req.licenser_license_info(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


@pytest.mark.skip
class TestPeopler:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']
        print(auth_token)

    # @testit.displayName("peopler_many_users_put")
    # @testit.externalID("peopler_many_users_put")
    # @testit.workItemID(1959)
    def test_peopler_many_users_put(self):
        req = Peopler(sess, host)
        resp = req.peopler_many_users_put(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_peopler_many_users_post(self):
        req = Peopler(sess, host)
        resp = req.peopler_many_users_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # @testit.displayName("peopler_profile_get")
    # @testit.externalID("peopler_profile_get")
    # @testit.workItemID(1961)
    def test_peopler_profile(self):
        req = Peopler(sess, host)
        resp = req.peopler_profile(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # @testit.displayName("peopler_profiles_get")
    # @testit.externalID("peopler_profiles_get")
    # @testit.workItemID(1962)
    def test_peopler_profiles(self):
        req = Peopler(sess, host)
        resp = req.peopler_profiles(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # @testit.displayName("peopler_users_get")
    # @testit.externalID("peopler_users_get")
    # @testit.workItemID(1963)

    def test_peopler_users_get(self):
        req = Peopler(sess, host)
        resp = req.peopler_users_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # @testit.displayName("peopler_users_post")
    # @testit.externalID("peopler_users_post")
    # @testit.workItemID(1964)

    def test_peopler_users_post(self):
        req = Peopler(sess, host)
        resp = req.peopler_users_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # @testit.displayName("peopler_users_id_get")
    # @testit.externalID("peopler_users_id_get")
    # @testit.workItemID(1965)

    def test_peopler_users_id_get(self):
        req = Peopler(sess, host)
        resp = req.peopler_users_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # @testit.displayName("peopler_users_id_put")
    # @testit.externalID("peopler_users_id_put")
    # @testit.workItemID(1966)

    def test_peopler_users_id_put(self):
        req = Peopler(sess, host)
        resp = req.peopler_users_id_put(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # @testit.displayName("peopler_users_delete")
    # @testit.externalID("peopler_users_delete")
    # @testit.workItemID(1967)
    def test_peopler_users_delete(self):
        req = Peopler(sess, host)
        resp = req.peopler_users_delete(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


@pytest.mark.skip
class TestPermitter:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']

    def test_permitter_check_ui_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_check_ui_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_all_db(self):
        req = Permitter(sess, host)
        resp = req.permitter_db_watcher_all_db(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_all_tables(self):
        req = Permitter(sess, host)
        resp = req.permitter_db_watcher_all_tables(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_db_tables(self):
        req = Permitter(sess, host)
        resp = req.permitter_db_watcher_db_tables(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_empty_role_dbs(self):
        req = Permitter(sess, host)
        resp = req.permitter_db_watcher_empty_role_dbs(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_empty_role_tables(self):
        req = Permitter(sess, host)
        resp = req.permitter_db_watcher_empty_role_tables(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_empty_role_tables_id(self):
        req = Permitter(sess, host)
        resp = req.permitter_db_watcher_empty_role_tables_id(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_get_tab_name_id(self):
        req = Permitter(sess, host)
        resp = req.permitter_db_watcher_get_tab_name_id(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_flags_query_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_flags_query_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_flags_visualisation_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_flags_visualisation_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_flags_report_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_flags_report_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_flags_mailing_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_flags_report_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_flags_script_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_flags_script_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_flags_script_sequence_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_flags_sscript_sequence_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_flags_query_post(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_flags_query_post(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"  # 403 логичный ответ на изменение чужого профиля

    def test_permitter_element_flags_visualisation_post(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_flags_visualisation_post(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"  # 403 логичный ответ на изменение чужого профиля

    def test_permitter_element_flags_report_post(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_flags_report_post(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"  # 403 логичный ответ на изменение чужого профиля

    def test_permitter_element_flags_mailing_post(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_flags_report_post(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"  # 403 логичный ответ на изменение чужого профиля

    def test_permitter_element_flags_script_post(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_flags_script_post(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"  # 403 логичный ответ на изменение чужого профиля

    def test_permitter_element_flags_script_sequence_post(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_flags_sscript_sequence_post(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"  # 403 логичный ответ на изменение чужого профиля

    def test_permitter_element_rules_all_flags_query_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_all_flags_query_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_all_flags_visualisation_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_all_flags_visualisation_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_all_flags_report_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_all_flags_report_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_all_flags_mailing_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_all_flags_mailing_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_all_flags_script_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_all_flags_script_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_all_flags_script_sequence_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_all_flags_script_sequence_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_query_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_flags_query_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_visualisation_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_flags_visualisation_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_report_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_flags_report_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_mailing_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_flags_mailing_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_script_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_flags_script_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_script_sequence_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_flags_script_sequence_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_query_post(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_flags_query_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_visualisation_post(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_flags_visualisation_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_report_post(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_flags_report_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_mailing_post(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_flags_mailing_post(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_script_post(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_flags_script_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_script_sequence_post(self):
        req = Permitter(sess, host)
        resp = req.permitter_element_rules_flags_script_sequence_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_roles_editor_roles_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_roles_editor_roles_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_roles_editor_roles_post(self):
        req = Permitter(sess, host)
        resp = req.permitter_roles_editor_roles_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_roles_editor_roles_edit_id_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_roles_editor_roles_edit_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_roles_editor_roles_id_put(self):
        req = Permitter(sess, host)
        resp = req.permitter_roles_editor_roles_id_put(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_roles_editor_roles_id_delete(self):
        req = Permitter(sess, host)
        resp = req.permitter_roles_editor_roles_id_delete(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_user_rules(self):
        req = Permitter(sess, host)
        resp = req.permitter_user_rules(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_users_elements_count_who_id_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_users_elements_count_who_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_users_new_author_who_id(self):
        req = Permitter(sess, host)
        resp = req.permitter_users_new_author_who_id_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_who_rules_who_id(self):
        req = Permitter(sess, host)
        resp = req.permitter_who_rules_who_id(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


@pytest.mark.skip
class TestRmCook:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']

    def test_rm_cook_active_directory_groups(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_active_directory_groups(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_groups_id(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_active_directory_groups_id(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_state(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_active_directory_state(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_top_groups(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_active_directory_top_groups(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_top_users(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_active_directory_top_users(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_users(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_active_directory_users(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_users_id(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_active_directory_users(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_calculation_start_calc_id_post(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_calculation_start_calc_id_post(auth_token)
        assert resp.status_code == 200 or 429, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_rm_logs_last(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_rm_logs_last(auth_token)
        assert resp.status_code == 200 or 429, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_recommendations(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_rm_recommendations(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_rm_roles_id_alias_post(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_rm_roles_id_alias_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_rm_roles_id_alias_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_rm_roles_id_alias_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_status(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_rm_status(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_role_model_result_export_role_model_to_excel(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_export_role_model_to_excel(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_role_model_result_groups_by_role_id(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_groups_by_role_id(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_resources_by_role_id(self):  # Не реализовано
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_resources_by_role_id(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_role_model_result_roles_by_source_source_id(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_roles_by_source_source_id(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_role_model_result_source_source_id_users_by_role_role_id(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_source_source_id_users_by_role_role_id(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_table_role_role_id_resources_by_user_user_id(self):  # Не используется
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_table_role_role_id_resources_by_user_user_id(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_table_role_role_id_users_by_resource_resource_id(self):  # Не используется
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_table_role_role_id_users_by_resource_resource_id(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_form_role_role_id_groups_by_user_user_id(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_form_role_role_id_groups_by_user_user_id(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_form_role_role_id_users_by_group_user_id(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_form_role_role_id_users_by_group_user_id(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_settings_calc_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_settings_calc_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_settings_calc_put(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_settings_calc_put(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_settings_mailings_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_settings_mailings_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_settings_mailings_post(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_settings_mailings_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_settings_sources_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_settings_sources_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_settings_sources_post(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_settings_sources_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

@pytest.mark.skip
class TestStorageWorker:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']

    def test_storage_worker_ask_one_sql_post(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_ask_one_sql_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_ask_plain_sql_post(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_ask_plain_sql_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_import_rules_get(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_import_rules_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_psevdo_namer_regs_post(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_psevdo_namer_regs_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_psevdo_namer_regs_get(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_psevdo_namer_regs_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_psevdo_namer_regs_pid_get(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_psevdo_namer_regs_pid_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_psevdo_namer_regs_pid_delete(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_psevdo_namer_regs_pid_delete(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_show_base_db_name_get(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_show_base_db_name_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_db_event_stats_db_name_flag_post(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_statistics_db_event_stats_db_name_flag_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_db_one_tab_stats_db_name_tab_name_get(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_statistics_db_one_tab_stats_db_name_tab_name_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_db_search_post(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_statistics_db_search_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_db_status_dbname_get(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_statistics_db_status_dbname_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_db_tabs_event_stats_db_name_tab_name_flag_post(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_statistics_db_tabs_event_stats_db_name_tab_name_flag_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_storage_search_post(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_statistics_storage_search_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_test_selection_post(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_statistics_storage_search_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # def test_storage_worker_storage_db_get(self):
    #     req = StorageWorker(sess, host)
    #     resp = req.storage_worker_storage_db_get(auth_token)
    #     assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_db_post(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_storage_db_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_db_get(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_storage_db_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_roles_editor_roles_for_storage_worker_put(self):
        req = StorageWorker(sess, host)
        resp = req.permitter_roles_editor_roles_for_storage_worker_put(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_db_put(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_storage_db_put(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_db_delete(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_storage_db_delete(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_import_csv_db_name_table_name_post(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_storage_import_csv_db_name_table_name_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_import_json_db_name_table_name_post(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_storage_import_json_db_name_table_name_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_supported_engines_get(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_storage_supported_engines_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_supported_types_get(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_storage_supported_types_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_table_columns_db_name_tab_name_get(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_storage_table_columns_db_name_tab_name_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_table_columns_db_name_table_name_post(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_storage_table_columns_db_name_table_name_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_table_db_name_table_name_ttl_get(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_storage_table_db_name_table_name_ttl_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_table_db_name_table_name_count_get(self):
        req = StorageWorker(sess, host)
        resp = req.storage_worker_storage_table_db_name_table_name_count_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


@pytest.mark.skip
class TestXbaCook:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']
        print(auth_token)

    @pytest.mark.skip
    def test_xba_cook_anomalies_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_anomalies_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_anomalies_picker_max_min_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_anomalies_picker_max_min_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_check_entity_type_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_check_entity_type_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_dashboard_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_dashboard_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_entity_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_entity_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_entity_details_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_entity_details_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_entity_info_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_entity_info_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_entity_info_settings_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_entity_info_settings_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_entity_info_settings_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_entity_info_settings_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        assert resp.text == '{"res":"ok"}\n', f"Ошибка, текст ответа {resp.text}"

    def test_xba_cook_entity_info_settings_entity_type_delete(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_entity_info_settings_entity_type_delete(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_entity_picker_min_max_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_entity_picker_min_max_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_entity_risks_description_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_entity_risks_description_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_max_min_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_max_min_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_categories_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_categories_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_export_profiles_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_export_profiles_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_functions_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_functions_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_graph_drilldown_statement_id_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_graph_drilldown_statement_id_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_xba_cook_profiles_graph_drilldown_id_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_graph_drilldown_id_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_max_min_id_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_max_min_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_graph_personal_id_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_graph_personal_id_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_graph_id_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_graph_id_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_groups_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_groups_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_groups_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_groups_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_groups_put(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_groups_put(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_groups_info_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_groups_info_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_groups_id_delete(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_groups_id_delete(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_groups_group_id_profile_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_groups_group_id_profile_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_xba_cook_profiles_groups_id_max_min_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_groups_id_max_min_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_xba_cook_profiles_groups_profile_id_group_id_weight_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_groups_profile_id_group_id_weight_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_import_profiles_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_import_profiles_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_start_id_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_start_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_stop_id_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_stop_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_id_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_xba_cook_profiles_id_delete(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_id_delete(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_id_log_last_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_id_log_last_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_id_whitelist_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_id_whitelist_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_id_string_whitelist_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_id_string_whitelist_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_id_list_whitelist_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_profiles_id_list_whitelist_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_xba_get(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_xba_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_xba_post(self):
        req = XbaCook(sess, host)
        resp = req.xba_cook_xba_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
