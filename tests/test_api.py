import os
import json

import pytest
import requests
import urllib3

from req.Api.req_auth import AuthApi
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
from req.Api.req_reporter import Reporter
from req.Api.req_scripter import Scripter
from req.Api.req_taskplan import Taskplan
from req.Api.req_updater import Updater
from req.Api.req_visualisation import Visualisation

urllib3.disable_warnings()

# ________Constants________
SESS = requests.Session()
HOST = os.environ.get('TARGET_URL', "https://10.130.0.22")


class TestAuth:

    @pytest.mark.skip # не реализовано
    def test_auth_local_register_post(self):
        req = AuthApi(SESS, HOST, withauth=False)
        resp = req.auth_local_register_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_ad_struct_get(self):
        req = AuthApi(SESS, HOST)
        resp = req.ad_struct_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_ou_users_post(self):
        req = AuthApi(SESS, HOST)
        resp = req.ou_users_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions_get(self):
        req = AuthApi(SESS, HOST)
        resp = req.sessions_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions_uid_get(self):
        req = AuthApi(SESS, HOST)
        resp = req.sessions_uid_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions_one_sid_del(self):
        req = AuthApi(SESS, HOST)
        resp = req.sessions_one_sid_del()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions_all_uid_del(self):
        req = AuthApi(SESS, HOST)
        resp = req.sessions_all_uid_del()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_logout_get(self):
        req = AuthApi(SESS, HOST)
        resp = req.logout_get()

        assert resp.status_code == 401, f"Ошибка, код {resp.status_code}, {resp.text}"
        assert resp.text == '{"res":"ok"}\n', f"Ошибка, текст ответа: {resp.text}"


class TestAbsorber:

    def test_absorber_library_columns_get(self):
        req = Absorber(SESS, HOST)
        resp = req.absorber_library_columns_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_peopler_users_at_uid_get(self):
        req = Absorber(SESS, HOST)
        resp = req.peopler_users_at_uid_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_id_picker_table_get(self):
        req = Absorber(SESS, HOST)
        resp = req.id_picker_table_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_absorber_library_conn_type_get(self):
        req = Absorber(SESS, HOST)
        resp = req.absorber_library_conn_type_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_absorber_library_conn_type_id_get(self):
        req = Absorber(SESS, HOST)
        resp = req.absorber_library_conn_type_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_absorber_library_connector_get(self):  # получаем список всех коннекторов
        req = Absorber(SESS, HOST)
        resp = req.absorber_library_connector_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_absorber_library_connector_post(self):
        req = Absorber(SESS, HOST)
        resp = req.absorber_library_connector_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_absorber_library_connector_put(self):
        req = Absorber(SESS, HOST)
        resp = req.absorber_library_connector_put()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_absorber_library_connector_id_get(self):
        req = Absorber(SESS, HOST)
        resp = req.absorber_library_connector_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_absorber_library_connector_delete(self):
        req = Absorber(SESS, HOST)
        resp = req.absorber_library_connector_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_absorber_library_logo_get(self):
        req = Absorber(SESS, HOST)
        resp = req.absorber_library_logo_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_absorber_library_logo_post(self):
        req = Absorber(SESS, HOST)
        resp = req.absorber_library_logo_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_library_logo_put(self):
        req = Absorber(SESS, HOST)
        resp = req.absorber_library_logo_put()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_absorber_library_logo_delete(self):
        req = Absorber(SESS, HOST)
        resp = req.absorber_library_logo_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_absorber_source_get(self):
        req = Absorber(SESS, HOST)
        resp = req.absorber_source_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_absorber_source_post(self):  # тут какая-то задница
        req = Absorber(SESS, HOST)
        resp = req.absorber_source_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_absorber_source_put(self):  # тут какая-то задница
        req = Absorber(SESS, HOST)
        resp = req.absorber_source_put()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_absorber_source_id_get(self):
        req = Absorber(SESS, HOST)
        resp = req.absorber_source_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_absorber_source_id_debug_get(self):
        req = Absorber(SESS, HOST)
        resp = req.absorber_source_id_debug_get()
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_absorber_source_id_delete(self):
        req = Absorber(SESS, HOST)
        resp = req.absorber_source_id_delete()
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestAlarmer:

    def test_alarmer_notification_admin_all_get(self):
        req = Alarmer(SESS, HOST)
        resp = req.alarmer_notification_admin_all_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_read_admin_get(self):
        req = Alarmer(SESS, HOST)
        resp = req.alarmer_notification_read_admin_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_read_type_admin_post(self):
        req = Alarmer(SESS, HOST)
        resp = req.alarmer_notification_read_type_admin_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_admin_get(self):
        req = Alarmer(SESS, HOST)
        resp = req.alarmer_notification_settings_admin_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_common_get(self):
        req = Alarmer(SESS, HOST)
        resp = req.alarmer_notification_settings_common_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_common_post(self):
        req = Alarmer(SESS, HOST)
        resp = req.alarmer_notification_settings_common_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_user_get(self):
        req = Alarmer(SESS, HOST)
        resp = req.alarmer_notification_settings_user_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_userone_post(self):
        req = Alarmer(SESS, HOST)
        resp = req.alarmer_notification_settings_userone_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_type_post(self):  # проблемный
        req = Alarmer(SESS, HOST)
        resp = req.alarmer_notification_settings_type_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_user_all_get(self):
        req = Alarmer(SESS, HOST)
        resp = req.alarmer_notification_settings_user_all_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_user_get(self):
        req = Alarmer(SESS, HOST)
        resp = req.alarmer_notification_user_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_send_invitation_post(self):
        req = Alarmer(SESS, HOST)
        resp = req.alarmer_send_invitation_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_send_invitations_post(self):
        req = Alarmer(SESS, HOST)
        resp = req.alarmer_send_invitations_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_send_msg_post(self):
        req = Alarmer(SESS, HOST)
        resp = req.alarmer_send_msg_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestCore:

    def test_core_active_directory_get(self):
        req = Core(SESS, HOST)
        resp = req.core_active_directory_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_active_directory_post(self):
        req = Core(SESS, HOST)
        resp = req.core_active_directory_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_active_directory_structure_post(self):
        req = Core(SESS, HOST)
        resp = req.core_active_directory_structure_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_active_directory_test_settings_post(self):
        req = Core(SESS, HOST)
        resp = req.core_active_directory_test_settings_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_backups_get(self):
        req = Core(SESS, HOST)
        resp = req.core_check_backups_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_common_get(self):
        req = Core(SESS, HOST)
        resp = req.core_common_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_common_post(self):
        req = Core(SESS, HOST)
        resp = req.core_common_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_common_test_post(self):
        req = Core(SESS, HOST)
        resp = req.core_common_test_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_component_ml_restart_get(self):
        req = Core(SESS, HOST)
        resp = req.core_component_ml_restart_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_component_picker_restart_get(self):
        req = Core(SESS, HOST)
        resp = req.core_component_picker_restart_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_component_servicedb_restart_get(self):  # считаем 400 ответ правильным, система не даст перезапустить
        req = Core(SESS, HOST)
        resp = req.core_component_servicedb_restart_get()
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_component_datastore_restart_get(self):  # считаем 400 ответ правильным, система не даст перезапустить
        req = Core(SESS, HOST)
        resp = req.core_component_datastore_restart_get()
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_download_settings_get(self):
        req = Core(SESS, HOST)
        resp = req.core_download_settings_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_email_import_cert_post(self):
        req = Core(SESS, HOST)
        resp = req.core_email_import_cert_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_email_send_test_post(self):
        req = Core(SESS, HOST)
        resp = req.core_email_send_test_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_email_in_get(self):
        req = Core(SESS, HOST)
        resp = req.core_email_in_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_email_out_get(self):
        req = Core(SESS, HOST)
        resp = req.core_email_out_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_email_in_post(self):
        req = Core(SESS, HOST)
        resp = req.core_email_out_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_email_out_post(self):
        req = Core(SESS, HOST)
        resp = req.core_email_in_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_flag_get(self):
        req = Core(SESS, HOST)
        resp = req.core_flag_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_ip_get(self):
        req = Core(SESS, HOST)
        resp = req.core_flag_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_list_ml_get(self):
        req = Core(SESS, HOST)
        resp = req.core_nodes_list_ml_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_list_picker_get(self):
        req = Core(SESS, HOST)
        resp = req.core_nodes_list_picker_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_list_servicedb_get(self):
        req = Core(SESS, HOST)
        resp = req.core_nodes_list_servicedb_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_list_datastore_get(self):
        req = Core(SESS, HOST)
        resp = req.core_nodes_list_datastore_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_ml_get(self):
        req = Core(SESS, HOST)
        resp = req.core_nodes_ml_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_picker_get(self):
        req = Core(SESS, HOST)
        resp = req.core_nodes_picker_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_servicedb_get(self):
        req = Core(SESS, HOST)
        resp = req.core_nodes_servicedb_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_nodes_datastore_get(self):
        req = Core(SESS, HOST)
        resp = req.core_nodes_datastore_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # def test_core_nodes_test_datastore(self):
    #     req = Core(sess, host)
    #     resp = req.core_nodes_test_datastore_post()
    #     assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
    #
    # def test_core_nodes_datastore_post(self):
    #     req = Core(sess, host)
    #     resp = req.core_nodes_datastore_post()
    #     assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
    #
    # def test_core_nodes_datastore_delete(self):
    #     req = Core(sess, host)
    #     resp = req.core_nodes_datastore_delete()
    #     assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_alarmer_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_alarmer_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_auth_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_auth_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_core_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_core_get()
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_licenser_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_licenser_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_log_eater_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_log_eater_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_monitor_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_monitor_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_peopler_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_peopler_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_permitter_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_permitter_get()
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_postgres_single_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_postgres_single_get()
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_taskplan_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_taskplan_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_updater_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_updater_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_absorber_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_absorber_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_picker_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_picker_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_storage_single_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_storage_single_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_storage_worker_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_storage_worker_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_ml_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_ml_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_scripter_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_scripter_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_datapie_baker_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_datapie_baker_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_elements_eater_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_elements_eater_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_frontend_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_frontend_get()
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_reporter_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_reporter_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_rm_cook_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_rm_cook_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_rm_ml_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_rm_ml_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_screener_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_screener_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_visualisation_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_visualisation_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_xba_cook_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_xba_cook_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_service_dp_xba_py_get(self):
        req = Core(SESS, HOST)
        resp = req.core_service_dp_xba_py_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_core_service_all_restart_get(self):  # стенд не тянет этот метод!
        req = Core(SESS, HOST)
        resp = req.core_service_all_restart_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_sid_get(self):
        req = Core(SESS, HOST)
        resp = req.core_sid_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_syslog_get(self):
        req = Core(SESS, HOST)
        resp = req.core_syslog_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_core_syslog_post(self):
        req = Core(SESS, HOST)
        resp = req.core_syslog_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestLicenser:

    def test_licenser_activate_post(self):
        req = Licenser(SESS, HOST)
        resp = req.licenser_activate_post()
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_licenser_license_info_get(self):
        req = Licenser(SESS, HOST)
        resp = req.licenser_license_info_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestPeopler:

    def test_peopler_many_users_put(self):
        req = Peopler(SESS, HOST)
        resp = req.peopler_many_users_put()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_peopler_many_users_post(self):
        req = Peopler(SESS, HOST)
        resp = req.peopler_many_users_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_peopler_profile_get(self):
        req = Peopler(SESS, HOST)
        resp = req.peopler_profile_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_peopler_profiles_get(self):
        req = Peopler(SESS, HOST)
        resp = req.peopler_profiles_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_peopler_users_get(self):
        req = Peopler(SESS, HOST)
        resp = req.peopler_users_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_peopler_users_post(self):
        req = Peopler(SESS, HOST)
        resp = req.peopler_users_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_peopler_users_id_get(self):
        req = Peopler(SESS, HOST)
        resp = req.peopler_users_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_peopler_users_id_put(self):
        req = Peopler(SESS, HOST)
        resp = req.peopler_users_id_put()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_peopler_users_delete(self):
        req = Peopler(SESS, HOST)
        resp = req.peopler_users_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestPermitter:

    def test_permitter_check_ui_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_check_ui_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_all_db_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_db_watcher_all_db_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_all_tables_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_db_watcher_all_tables_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_db_tables_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_db_watcher_db_tables_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_empty_role_dbs_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_db_watcher_empty_role_dbs_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_empty_role_tables_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_db_watcher_empty_role_tables_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_empty_role_tables_id_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_db_watcher_empty_role_tables_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_db_watcher_get_tab_name_id_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_db_watcher_get_tab_name_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_flags_query_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_flags_query_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_flags_visualisation_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_flags_visualisation_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_flags_report_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_flags_report_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_flags_mailing_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_flags_report_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_flags_script_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_flags_script_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_flags_script_sequence_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_flags_sscript_sequence_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_flags_query_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_flags_query_post()
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"  # 403 логичный ответ на изменение чужого профиля

    def test_permitter_element_flags_visualisation_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_flags_visualisation_post()
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"  # 403 логичный ответ на изменение чужого профиля

    def test_permitter_element_flags_report_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_flags_report_post()
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"  # 403 логичный ответ на изменение чужого профиля

    def test_permitter_element_flags_mailing_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_flags_report_post()
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"  # 403 логичный ответ на изменение чужого профиля

    def test_permitter_element_flags_script_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_flags_script_post()
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"  # 403 логичный ответ на изменение чужого профиля

    def test_permitter_element_flags_script_sequence_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_flags_sscript_sequence_post()
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"  # 403 логичный ответ на изменение чужого профиля

    def test_permitter_element_rules_all_flags_query_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_all_flags_query_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_all_flags_visualisation_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_all_flags_visualisation_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_all_flags_report_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_all_flags_report_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_all_flags_mailing_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_all_flags_mailing_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_all_flags_script_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_all_flags_script_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_all_flags_script_sequence_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_all_flags_script_sequence_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_query_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_flags_query_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_visualisation_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_flags_visualisation_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_report_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_flags_report_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_mailing_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_flags_mailing_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_script_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_flags_script_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_script_sequence_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_flags_script_sequence_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_query_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_flags_query_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_visualisation_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_flags_visualisation_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_report_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_flags_report_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_mailing_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_flags_mailing_post()
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_script_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_flags_script_post()
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_flags_script_sequence_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_flags_script_sequence_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_delete_element_type_query_element_id_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_delete_element_type_query_element_id_post()
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_roles_editor_roles_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_roles_editor_roles_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_roles_editor_roles_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_roles_editor_roles_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_roles_editor_roles_edit_id_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_roles_editor_roles_edit_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_roles_editor_roles_id_put(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_roles_editor_roles_id_put()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_roles_editor_roles_id_delete(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_roles_editor_roles_id_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_user_rules_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_user_rules_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_users_elements_count_who_id_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_users_elements_count_who_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_users_new_author_who_id(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_users_new_author_who_id_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_who_rules_who_id_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_who_rules_who_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestRmCook:

    def test_id_picker_table_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.id_picker_table_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_groups_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_active_directory_groups_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_groups_id_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_active_directory_groups_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_state_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_active_directory_state_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_top_groups_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_active_directory_top_groups_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_top_users_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_active_directory_top_users_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_users_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_active_directory_users_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_users_id_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_active_directory_users_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_calculation_start_calc_id_post(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_calculation_start_calc_id_post()
        assert resp.status_code == 200 or 429, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_rm_logs_last_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_rm_logs_last_get()
        assert resp.status_code == 200 or 429, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_recommendations_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_rm_recommendations_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_rm_roles_id_alias_post(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_rm_roles_id_alias_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_rm_roles_id_alias_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_rm_roles_id_alias_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_status_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_rm_status_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_role_model_result_export_role_model_to_excel_post(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_role_model_result_export_role_model_to_excel_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_role_model_result_groups_by_role_id_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_role_model_result_groups_by_role_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_resources_by_role_id_get(self):  # Не реализовано
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_role_model_result_resources_by_role_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_role_model_result_roles_by_source_source_id_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_role_model_result_roles_by_source_source_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_role_model_result_source_source_id_users_by_role_role_id_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_role_model_result_source_source_id_users_by_role_role_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_table_role_role_id_resources_by_user_user_id_get(self):  # Не используется
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_role_model_result_table_role_role_id_resources_by_user_user_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_table_role_role_id_users_by_resource_resource_id_get(self):  # Не используется
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_role_model_result_table_role_role_id_users_by_resource_resource_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_form_role_role_id_groups_by_user_user_id_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_role_model_result_form_role_role_id_groups_by_user_user_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_form_role_role_id_users_by_group_user_id_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_role_model_result_form_role_role_id_users_by_group_user_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_settings_calc_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_settings_calc_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_settings_calc_put(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_settings_calc_put()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_settings_mailings_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_settings_mailings_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_settings_mailings_post(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_settings_mailings_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_settings_sources_get(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_settings_sources_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_settings_sources_post(self):
        req = Rm_Cook(SESS, HOST)
        resp = req.rm_cook_settings_sources_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestStorageWorker:

    def test_peopler_users_at_uid_get(self):
        req = StorageWorker(SESS, HOST)
        resp = req.peopler_users_at_uid_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_id_picker_table_get(self):
        req = StorageWorker(SESS, HOST)
        resp = req.id_picker_table_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_ask_one_sql_post(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_ask_one_sql_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_ask_plain_sql_post(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_ask_plain_sql_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_import_rules_get(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_import_rules_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_psevdo_namer_regs_post(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_psevdo_namer_regs_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_psevdo_namer_regs_get(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_psevdo_namer_regs_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_psevdo_namer_regs_pid_get(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_psevdo_namer_regs_pid_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_psevdo_namer_regs_pid_delete(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_psevdo_namer_regs_pid_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_show_base_db_name_get(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_show_base_db_name_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_db_event_stats_db_name_flag_post(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_statistics_db_event_stats_db_name_flag_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_db_one_tab_stats_db_name_tab_name_get(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_statistics_db_one_tab_stats_db_name_tab_name_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_db_search_post(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_statistics_db_search_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_db_status_dbname_get(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_statistics_db_status_dbname_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_db_tabs_event_stats_db_name_tab_name_flag_post(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_statistics_db_tabs_event_stats_db_name_tab_name_flag_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_storage_search_post(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_statistics_storage_search_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_test_selection_post(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_statistics_storage_search_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # def test_storage_worker_storage_db_get(self):
    #     req = StorageWorker(sess, host)
    #     resp = req.storage_worker_storage_db_get()
    #     assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_db_post(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_storage_db_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_db_get(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_storage_db_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_roles_editor_roles_for_storage_worker_put(self):
        req = StorageWorker(SESS, HOST)
        resp = req.permitter_roles_editor_roles_for_storage_worker_put()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_db_put(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_storage_db_put()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_db_delete(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_storage_db_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_import_csv_db_name_table_name_post(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_storage_import_csv_db_name_table_name_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_import_json_db_name_table_name_post(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_storage_import_json_db_name_table_name_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_supported_engines_get(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_storage_supported_engines_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_supported_types_get(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_storage_supported_types_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_table_columns_db_name_tab_name_get(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_storage_table_columns_db_name_tab_name_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_table_columns_db_name_table_name_post(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_storage_table_columns_db_name_table_name_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_table_db_name_table_name_ttl_get(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_storage_table_db_name_table_name_ttl_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_storage_table_db_name_table_name_count_get(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_storage_table_db_name_table_name_count_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestXbaCook:

    # FIXME: кейс почти полностью идентичен TestStorageWorker.test_id_picker_table_get
    @pytest.mark.skip
    def test_id_picker_table_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.id_picker_table_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        print(resp.text)

    # FIXME: кейс почти полностью идентичен TestPeopler.test_peopler_users_at_uid_get
    @pytest.mark.skip
    def test_peopler_users_at_uid_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.peopler_users_at_uid_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_xba_cook_anomalies_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_anomalies_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_anomalies_picker_max_min_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_anomalies_picker_max_min_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_check_entity_type_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_check_entity_type_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_dashboard_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_dashboard_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_entity_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_entity_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_entity_details_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_entity_details_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_entity_info_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_entity_info_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_entity_info_settings_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_entity_info_settings_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_entity_info_settings_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_entity_info_settings_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        assert resp.text == '{"res":"ok"}\n', f"Ошибка, текст ответа {resp.text}"

    def test_xba_cook_entity_info_settings_entity_type_delete(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_entity_info_settings_entity_type_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_entity_picker_min_max_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_entity_picker_min_max_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_entity_risks_description_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_entity_risks_description_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_max_min_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_max_min_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_categories_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_categories_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_export_profiles_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_export_profiles_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_functions_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_functions_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_graph_drilldown_statement_id_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_graph_drilldown_statement_id_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_graph_drilldown_id_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_graph_drilldown_id_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_graph_drilldown_id_post_descriprion_key_check(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_graph_drilldown_id_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        try:
            # отсутствие ключа на любом узле бросит ошибку "KeyError"
            json.loads(resp.text)['res']['info']['description']
        except KeyError:
            assert False, f"Ошибка, отсутствует ключ res>info>description в ответе, {resp.text}"

    def test_xba_cook_profiles_max_min_id_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_max_min_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_graph_personal_id_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_graph_personal_id_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_graph_id_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_graph_id_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_groups_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_groups_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_groups_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_groups_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_groups_put(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_groups_put()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_groups_info_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_groups_info_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_groups_id_delete(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_groups_id_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_groups_group_id_profile_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_groups_group_id_profile_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_xba_cook_profiles_groups_id_max_min_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_groups_id_max_min_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_xba_cook_profiles_groups_profile_id_group_id_weight_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_groups_profile_id_group_id_weight_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_import_profiles_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_import_profiles_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_start_id_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_start_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_stop_id_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_stop_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_id_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_xba_cook_profiles_id_delete(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_id_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_xba_cook_profiles_id_log_last_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_id_log_last_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_id_whitelist_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_id_whitelist_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_id_string_whitelist_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_id_string_whitelist_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_id_list_whitelist_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_id_list_whitelist_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_xba_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_xba_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_xba_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_xba_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestElementsEater:

    def test_elements_eater_reports_export_post(self):
        req = ElementsEater(SESS, HOST)
        resp = req.elements_eater_reports_export_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_elements_eater_reports_import_post(self):
        req = ElementsEater(SESS, HOST)
        resp = req.elements_eater_reports_import_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestLogEater:

    def test_log_eater_audit_users_days_get(self):
        req = LogEater(SESS, HOST)
        resp = req.log_eater_audit_users_days_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestMonitor:

    def test_monitor_anomals_flag_0_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_anomals_flag_0_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_anomals_flag_1_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_anomals_flag_1_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_anomals_flag_2_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_anomals_flag_2_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_anomals_flag_3_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_anomals_flag_3_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_anomals_flag_4_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_anomals_flag_4_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_monitor_dump_server_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_dump_server_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_monitor_dump_nodes_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_dump_nodes_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # -----------------------------------------------------------

    def test_monitor_nodes_graphs_ml_ram_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_ml_ram_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_ml_cpu_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_ml_cpu_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_ml_iops_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_ml_iops_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_ml_network_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_ml_network_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_ml_picked_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_ml_picked_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_picker_ram_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_picker_ram_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_picker_cpu_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_picker_cpu_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_picker_iops_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_picker_iops_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_picker_network_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_picker_network_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_picker_picked_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_picker_picked_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_servicedb_ram_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_servicedb_ram_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_servicedb_cpu_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_servicedb_cpu_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_servicedb_iops_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_servicedb_iops_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_servicedb_network_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_servicedb_network_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_servicedb_picked_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_servicedb_picked_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_datastore_ram_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_datastore_ram_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_datastore_cpu_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_datastore_cpu_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_datastore_iops_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_datastore_iops_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_datastore_network_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_datastore_network_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_graphs_datastore_picked_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_graphs_datastore_picked_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # -----------------------------------------------------------

    def test_monitor_nodes_stats_ml_get(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_stats_ml_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_stats_picker_get(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_stats_picker_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_stats_servicedb_get(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_stats_servicedb_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_nodes_stats_datastore_get(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_nodes_stats_datastore_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_graphs_ram_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_webserver_graphs_ram_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_graphs_cpu_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_webserver_graphs_cpu_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_graphs_iops_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_webserver_graphs_iops_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_graphs_network_post(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_webserver_graphs_network_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_groups_get(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_webserver_groups_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_stats_sys_get(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_webserver_stats_sys_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_stats_visual_get(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_webserver_stats_visual_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_stats_analytics_get(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_webserver_stats_analytics_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_stats_datastore_get(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_webserver_stats_datastore_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_monitor_webserver_stats_dataproc_get(self):
        req = Monitor(SESS, HOST)
        resp = req.monitor_webserver_stats_dataproc_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestReporter:

    def test_peopler_users_at_uid_get(self):
        req = Reporter(SESS, HOST)
        resp = req.peopler_users_at_uid_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_reporter_mailing_post(self):
        req = Reporter(SESS, HOST)
        resp = req.reporter_mailing_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_reporter_mailing_sample_post(self):
        req = Reporter(SESS, HOST)
        resp = req.reporter_mailing_sample_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_reporter_mailing_get(self):
        req = Reporter(SESS, HOST)
        resp = req.reporter_mailing_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_reporter_mailing_put(self):
        req = Reporter(SESS, HOST)
        resp = req.reporter_mailing_put()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_reporter_mailing_type_0_1_get(self):
        req = Reporter(SESS, HOST)
        resp = req.reporter_mailing_type_0_1_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_reporter_mailing_type_2_3_get(self):
        req = Reporter(SESS, HOST)
        resp = req.reporter_mailing_type_2_3_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_reporter_mailing_id_get(self):
        req = Reporter(SESS, HOST)
        resp = req.reporter_mailing_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_reporter_screener_fast_png_post(self):
        req = Reporter(SESS, HOST)
        resp = req.reporter_screener_fast_png_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_reporter_screener_fast_pdf_post(self):
        req = Reporter(SESS, HOST)
        resp = req.reporter_screener_fast_pdf_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # def test_reporter_screener_fast_png_id_get(self): # ---- не используется ----
    #     req = Reporter(sess, host)
    #     resp = req.reporter_screener_fast_png_id_get()
    #     assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
    #
    # def test_reporter_screener_fast_pdf_id_get(self):
    #     req = Reporter(sess, host)
    #     resp = req.reporter_screener_fast_pdf_id_get()
    #     assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_reporter_screener_fast_xlsx_id_get(self):  # xlsx формируется на фронте
        req = Reporter(SESS, HOST)
        resp = req.reporter_screener_fast_xlsx_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_reporter_visualisation_cached_role_report_report_id_role_id_post(self):
        req = Reporter(SESS, HOST)
        resp = req.reporter_visualisation_cached_role_report_report_id_role_id_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_reporter_mailing_id_delete(self):
        req = Reporter(SESS, HOST)
        resp = req.reporter_mailing_id_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_reporter_visualisation_cached_user_report_get(self):
        req = Reporter(SESS, HOST)
        resp = req.reporter_visualisation_cached_user_report_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_reporter_visualisation_cached_user_report_report_id_post(self):
        req = Reporter(SESS, HOST)
        resp = req.reporter_visualisation_cached_user_report_report_id_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestScripter:

    # FIXME: replace in right class
    def test_peopler_users_at_uid_get(self):
        req = Absorber(SESS, HOST)
        resp = req.peopler_users_at_uid_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_category_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_category_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_libs_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_libs_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_post(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_put(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_put()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_exec_list_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_exec_list_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_id_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_start_post(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_start_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_stop_id_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_stop_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_id_files_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_id_files_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_id_files_put(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_id_files_put()
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_id_log_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_id_log_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_id_log_last_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_id_log_last_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_id_log_log_id_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_id_log_log_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_id_log_log_id_delete(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_id_log_log_id_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_id_log_delete(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_id_log_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_type_user_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_type_user_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_type_admin_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_type_admin_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_sequence_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_sequence_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_sequence_post(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_sequence_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_sequence_put(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_sequence_put()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_sequence_log_id_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_sequence_log_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_sequence_id_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_sequence_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_sequence_start_post(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_sequence_start_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_sequence_stop_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_sequence_stop_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_sequence_id_log_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_sequence_id_log_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_sequence_id_log_id_id_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_sequence_id_log_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_sequence_sequence_type_admin_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_sequence_sequence_type_admin_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_sequence_sequence_type_user_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_sequence_sequence_type_user_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_sequence_id_delete(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_sequence_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_id_delete(self):  # удаление скрипта
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_id_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestTaskplan:

    def test_taskplan_get_shedule_post(self):
        req = Taskplan(SESS, HOST)
        resp = req.taskplan_get_shedule_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_taskplan_tasks_post(self):
        req = Taskplan(SESS, HOST)
        resp = req.taskplan_tasks_post()
        assert resp.status_code == 200 or 404, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestUpdater:

    def test_updater_additions_get(self):
        req = Updater(SESS, HOST)
        resp = req.updater_additions_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_updater_additions_addition_delete(self):
        req = Updater(SESS, HOST)
        resp = req.updater_additions_addition_delete()
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_updater_additions_addition_post(self):
        req = Updater(SESS, HOST)
        resp = req.updater_additions_addition_post()
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_updater_check_updates_get(self):
        req = Updater(SESS, HOST)
        resp = req.updater_check_updates_get()
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestVisualisation:

    def test_peopler_users_at_uid_get(self):
        req = Visualisation(SESS, HOST)
        resp = req.peopler_users_at_uid_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_id_picker_table_get(self):
        req = Visualisation(SESS, HOST)
        resp = req.id_picker_table_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_query_get(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_query_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_query_do_query_id_post(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_query_do_query_id_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_query_save_post(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_query_save_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_query_do_query_usage_id_get(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_query_do_query_usage_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_query_do_query_id_get(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_query_do_query_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_query_do_query_id_delete(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_query_do_query_id_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_reports_post(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_reports_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_reports_get(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_reports_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_reports_report_id_get(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_reports_report_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_reports_report_id_delete(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_reports_report_id_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_visualisation_get(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_visualisation_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_visualisation_post(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_visualisation_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_visualisation_dataseries_visualisation_id_post(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_visualisation_dataseries_visualisation_id_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_visualisation_types_get(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_visualisation_types_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_visualisation_usage_visualisation_id_get(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_visualisation_usage_visualisation_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_visualisation_visualisation_id_get(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_visualisation_usage_visualisation_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_visualisation_visualisation_id_delete(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_visualisation_visualisation_id_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
