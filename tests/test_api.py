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
from req.Api.req_elements_eater import ElementsEater
from req.Api.req_log_eater import LogEater
from req.Api.req_monitor import Monitor

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

    def test_ad_struct_get(self):
        req = AuthApi(sess, host)
        resp = req.ad_struct_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_ou_users_post(self):
        req = AuthApi(sess, host)
        resp = req.ou_users_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions_get(self):
        req = AuthApi(sess, host)
        resp = req.sessions_get(auth_token)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions_uid_get(self):
        req = AuthApi(sess, host)
        resp = req.sessions_uid_get(auth_token)

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

    def test_logout_get(self):
        self.test_get_token()
        req = AuthApi(sess, host)
        resp = req.sessions_get(auth_token)
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

    def test_library_columns_get(self):
        req = Absorber(sess, host)
        resp = req.library_columns_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_conn_type_get(self):
        req = Absorber(sess, host)
        resp = req.library_conn_type_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_conn_type_id_get(self):
        req = Absorber(sess, host)
        resp = req.library_conn_type_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_connector_get(self):  # получаем список всех коннекторов
        req = Absorber(sess, host)
        resp = req.library_connector_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_connector_post(self):
        req = Absorber(sess, host)
        resp = req.library_connector_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_connector_put(self):
        req = Absorber(sess, host)
        resp = req.library_connector_put(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_connector_id_get(self):
        req = Absorber(sess, host)
        resp = req.library_connector_id_get(auth_token)
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

    def test_alarmer_notification_admin_all_get(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_admin_all_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_read_admin_get(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_read_admin_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_read_type_admin_post(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_read_type_admin_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_admin_get(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_settings_admin_get(auth_token)
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

    def test_alarmer_notification_user_all_get(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_settings_user_all_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_user_get(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_user_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_send_invitation_post(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_send_invitation_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_send_invitations_post(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_send_invitations_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_send_msg_post(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_send_msg_post(auth_token)
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

    def test_core_backups_get(self):
        req = Core(sess, host)
        resp = req.core_check_backups_get(auth_token)
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

    def test_core_component_ml_restart_get(self):
        req = Core(sess, host)
        resp = req.core_component_ml_restart_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_component_picker_restart_get(self):
        req = Core(sess, host)
        resp = req.core_component_picker_restart_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_component_servicedb_restart_get(self):  # считаем 400 ответ правильным, система не даст перезапустить
        req = Core(sess, host)
        resp = req.core_component_servicedb_restart_get(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_component_datastore_restart_get(self):  # считаем 400 ответ правильным, система не даст перезапустить
        req = Core(sess, host)
        resp = req.core_component_datastore_restart_get(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_download_settings_get(self):
        req = Core(sess, host)
        resp = req.core_download_settings_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_send_test_post(self):
        req = Core(sess, host)
        resp = req.core_send_test_post(auth_token)
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

    def test_core_flag_get(self):
        req = Core(sess, host)
        resp = req.core_flag_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_ip_get(self):
        req = Core(sess, host)
        resp = req.core_flag_get(auth_token)
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

    def test_core_service_dp_alarmer_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_alarmer_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_auth_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_auth_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_core_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_core_get(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_licenser_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_licenser_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_log_eater_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_log_eater_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_monitor_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_monitor_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_peopler_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_peopler_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_permitter_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_permitter_get(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_postgres_single_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_postgres_single_get(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_taskplan_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_taskplan_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_updater_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_updater_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_absorber_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_absorber_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_picker_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_picker_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_storage_single_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_storage_single_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_storage_worker_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_storage_worker_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_ml_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_ml_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_scripter_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_scripter_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_datapie_baker_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_datapie_baker_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_elements_eater_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_elements_eater_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_frontend_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_frontend_get(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_reporter_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_reporter_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_rm_cook_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_rm_cook_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_rm_ml_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_rm_ml_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_screener_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_screener_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_visualisation_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_visualisation_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_xba_cook_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_xba_cook_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_xba_py_get(self):
        req = Core(sess, host)
        resp = req.core_service_dp_xba_py_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_core_service_all_restart_get(self):  # стенд не тянет этот метод!
        req = Core(sess, host)
        resp = req.core_service_all_restart_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_sid_get(self):
        req = Core(sess, host)
        resp = req.core_sid_get(auth_token)
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

    def test_licenser_activate_post(self):
        req = Licenser(sess, host)
        resp = req.licenser_activate_post(auth_token)
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_licenser_license_info_get(self):
        req = Licenser(sess, host)
        resp = req.licenser_license_info_get(auth_token)
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
    def test_peopler_profile_get(self):
        req = Peopler(sess, host)
        resp = req.peopler_profile_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # @testit.displayName("peopler_profiles_get")
    # @testit.externalID("peopler_profiles_get")
    # @testit.workItemID(1962)
    def test_peopler_profiles_get(self):
        req = Peopler(sess, host)
        resp = req.peopler_profiles_get(auth_token)
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

    def test_permitter_db_watcher_all_db_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_db_watcher_all_db_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_all_tables_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_db_watcher_all_tables_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_db_tables_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_db_watcher_db_tables_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_empty_role_dbs_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_db_watcher_empty_role_dbs_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_empty_role_tables_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_db_watcher_empty_role_tables_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_empty_role_tables_id_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_db_watcher_empty_role_tables_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_get_tab_name_id_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_db_watcher_get_tab_name_id_get(auth_token)
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

    def test_permitter_user_rules_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_user_rules_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_users_elements_count_who_id_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_users_elements_count_who_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_users_new_author_who_id(self):
        req = Permitter(sess, host)
        resp = req.permitter_users_new_author_who_id_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_who_rules_who_id_get(self):
        req = Permitter(sess, host)
        resp = req.permitter_who_rules_who_id_get(auth_token)
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

    def test_rm_cook_active_directory_groups_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_active_directory_groups_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_groups_id_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_active_directory_groups_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_state_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_active_directory_state_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_top_groups_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_active_directory_top_groups_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_top_users_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_active_directory_top_users_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_users_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_active_directory_users_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_users_id_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_active_directory_users_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_calculation_start_calc_id_post(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_calculation_start_calc_id_post(auth_token)
        assert resp.status_code == 200 or 429, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_rm_logs_last_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_rm_logs_last_get(auth_token)
        assert resp.status_code == 200 or 429, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_recommendations_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_rm_recommendations_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_rm_roles_id_alias_post(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_rm_roles_id_alias_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_rm_roles_id_alias_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_rm_roles_id_alias_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_status_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_rm_status_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_role_model_result_export_role_model_to_excel_post(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_export_role_model_to_excel_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_role_model_result_groups_by_role_id_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_groups_by_role_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_resources_by_role_id_get(self):  # Не реализовано
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_resources_by_role_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_role_model_result_roles_by_source_source_id_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_roles_by_source_source_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_role_model_result_source_source_id_users_by_role_role_id_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_source_source_id_users_by_role_role_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_table_role_role_id_resources_by_user_user_id_get(self):  # Не используется
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_table_role_role_id_resources_by_user_user_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_table_role_role_id_users_by_resource_resource_id_get(self):  # Не используется
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_table_role_role_id_users_by_resource_resource_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_form_role_role_id_groups_by_user_user_id_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_form_role_role_id_groups_by_user_user_id_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_form_role_role_id_users_by_group_user_id_get(self):
        req = Rm_Cook(sess, host)
        resp = req.rm_cook_role_model_result_form_role_role_id_users_by_group_user_id_get(auth_token)
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


@pytest.mark.skip
class TestElementsEater:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']

    def test_elements_eater_reports_export_post(self):
        req = ElementsEater(sess, host)
        resp = req.elements_eater_reports_export_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_elements_eater_reports_import_post(self):
        req = ElementsEater(sess, host)
        resp = req.elements_eater_reports_import_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


@pytest.mark.skip
class TestLogEater:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']

    def test_log_eater_audit_users_days_get(self):
        req = LogEater(sess, host)
        resp = req.log_eater_audit_users_days_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestMonitor:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']

    def test_monitor_anomals_flag_0_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_anomals_flag_0_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_anomals_flag_1_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_anomals_flag_1_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_anomals_flag_2_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_anomals_flag_2_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_anomals_flag_3_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_anomals_flag_3_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_anomals_flag_4_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_anomals_flag_4_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_monitor_dump_server_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_dump_server_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_monitor_dump_nodes_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_dump_nodes_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # -----------------------------------------------------------

    def test_monitor_nodes_graphs_ml_ram_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_ml_ram_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_ml_cpu_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_ml_cpu_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_ml_iops_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_ml_iops_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_ml_network_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_ml_network_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_ml_picked_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_ml_picked_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_picker_ram_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_picker_ram_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_picker_cpu_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_picker_cpu_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_picker_iops_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_picker_iops_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_picker_network_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_picker_network_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_picker_picked_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_picker_picked_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_servicedb_ram_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_servicedb_ram_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_servicedb_cpu_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_servicedb_cpu_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_servicedb_iops_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_servicedb_iops_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_servicedb_network_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_servicedb_network_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_servicedb_picked_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_servicedb_picked_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_datastore_ram_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_datastore_ram_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_datastore_cpu_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_datastore_cpu_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_datastore_iops_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_datastore_iops_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_datastore_network_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_datastore_network_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_datastore_picked_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_graphs_datastore_picked_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # -----------------------------------------------------------

    def test_monitor_nodes_stats_ml_get(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_stats_ml_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_stats_picker_get(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_stats_picker_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_stats_servicedb_get(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_stats_servicedb_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_stats_datastore_get(self):
        req = Monitor(sess, host)
        resp = req.monitor_nodes_stats_datastore_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_graphs_ram_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_webserver_graphs_ram_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_graphs_cpu_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_webserver_graphs_cpu_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_graphs_iops_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_webserver_graphs_iops_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_graphs_network_post(self):
        req = Monitor(sess, host)
        resp = req.monitor_webserver_graphs_network_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_groups_get(self):
        req = Monitor(sess, host)
        resp = req.monitor_webserver_groups_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_stats_sys_get(self):
        req = Monitor(sess, host)
        resp = req.monitor_webserver_stats_sys_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_stats_visual_get(self):
        req = Monitor(sess, host)
        resp = req.monitor_webserver_stats_visual_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_stats_analytics_get(self):
        req = Monitor(sess, host)
        resp = req.monitor_webserver_stats_analytics_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_stats_datastore_get(self):
        req = Monitor(sess, host)
        resp = req.monitor_webserver_stats_datastore_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_stats_dataproc_get(self):
        req = Monitor(sess, host)
        resp = req.monitor_webserver_stats_dataproc_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
