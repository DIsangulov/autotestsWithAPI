import os

import pytest
import requests
import urllib3

from req.Api.req_permitter import Permitter
from req.Api.req_rm_cook import RmCook
from req.Api.req_storage_worker import StorageWorker
from req.Api.req_xba_cook import XbaCook
from req.Api.req_reporter import Reporter
from req.Api.req_scripter import Scripter
from req.Api.req_taskplan import Taskplan
from req.Api.req_updater import Updater
from req.Api.req_visualisation import Visualisation
from tests.case.api.auth import AuthApiCase
from tests.case.api.absorber import AbsorberCase
from tests.case.api.alarmer import AlarmerCase
from tests.case.api.core import CoreCase
from tests.case.api.elements_eater import ElementsEaterCase
from tests.case.api.licenser import LicenserCase
from tests.case.api.log_eater import LogEaterCase
from tests.case.api.monitor import MonitorCase
from tests.case.api.peopler import PeoplerCase

urllib3.disable_warnings()

# TODO: перекинуть в base_req?
SESS = requests.Session()
HOST = os.environ.get('TARGET_URL', "https://10.130.0.22")


class TestAuth:

    def test_auth_ad_struct_get(self):
        AuthApiCase(SESS, HOST).case_auth_ad_struct_get()

    def test_auth_local_register_post(self):
        AuthApiCase(SESS, HOST, withauth=False).case_auth_local_register_post()

    def test_auth_logout_get(self):
        AuthApiCase(SESS, HOST).case_auth_logout_get()

    def test_auth_ou_users_post(self):
        AuthApiCase(SESS, HOST).case_auth_ou_users_post()

    def test_auth_sessions_get(self):
        AuthApiCase(SESS, HOST).case_auth_sessions_get()

    def test_auth_sessions_uid_get(self):
        AuthApiCase(SESS, HOST).case_auth_sessions_uid_get()

    def test_auth_sessions_one_sid_del(self):
        AuthApiCase(SESS, HOST).case_auth_sessions_one_sid_del()

    def test_auth_sessions_all_uid_del(self):
        AuthApiCase(SESS, HOST).case_auth_sessions_all_uid_del()


class TestAbsorber:

    def test_absorber_library_columns_get(self):
        AbsorberCase(SESS, HOST).case_absorber_library_columns_get()

    def test_absorber_library_conn_type_get(self):
        AbsorberCase(SESS, HOST).case_absorber_library_conn_type_get()

    def test_absorber_library_conn_type_id_get(self):
        AbsorberCase(SESS, HOST).case_absorber_library_conn_type_id_get()

    def test_absorber_library_connector_get(self):
        AbsorberCase(SESS, HOST).case_absorber_library_connector_get()

    def test_absorber_library_connector_post(self):
        AbsorberCase(SESS, HOST).case_absorber_library_connector_post()

    def test_absorber_library_connector_put(self):
        AbsorberCase(SESS, HOST).case_absorber_library_connector_put()

    def test_absorber_library_connector_id_get(self):
        AbsorberCase(SESS, HOST).case_absorber_library_connector_id_get()

    def test_absorber_library_connector_id_delete(self):
        AbsorberCase(SESS, HOST).case_absorber_library_connector_id_delete()

    def test_absorber_library_logo_get(self):
        AbsorberCase(SESS, HOST).case_absorber_library_logo_get()

    def test_absorber_library_logo_post(self):
        AbsorberCase(SESS, HOST).case_absorber_library_logo_post()

    def test_library_logo_put(self):
        AbsorberCase(SESS, HOST).case_absorber_library_logo_put()

    def test_absorber_library_logo_delete(self):
        AbsorberCase(SESS, HOST).case_absorber_library_logo_delete()

    def test_absorber_source_get(self):
        AbsorberCase(SESS, HOST).case_absorber_source_get()

    def test_absorber_source_post(self):
        AbsorberCase(SESS, HOST).case_absorber_source_post()

    def test_absorber_source_put(self):
        AbsorberCase(SESS, HOST).case_absorber_source_put()

    def test_absorber_source_id_get(self):
        AbsorberCase(SESS, HOST).case_absorber_source_id_get()

    def test_absorber_source_id_debug_get(self):
        AbsorberCase(SESS, HOST).case_absorber_source_id_debug_get()

    def test_absorber_source_id_delete(self):
        AbsorberCase(SESS, HOST).case_absorber_source_id_delete()


class TestAlarmer:

    def test_alarmer_notification_admin_all_get(self):
        AlarmerCase(SESS, HOST).case_alarmer_notification_admin_all_get()

    def test_alarmer_notification_read_admin_get(self):
        AlarmerCase(SESS, HOST).case_alarmer_notification_read_admin_get()

    def test_alarmer_notification_read_type_admin_post(self):
        AlarmerCase(SESS, HOST).case_alarmer_notification_read_type_admin_post()

    def test_alarmer_notification_settings_admin_get(self):
        AlarmerCase(SESS, HOST).case_alarmer_notification_settings_admin_get()

    def test_alarmer_notification_settings_common_get(self):
        AlarmerCase(SESS, HOST).case_alarmer_notification_settings_common_get()

    def test_alarmer_notification_settings_common_post(self):
        AlarmerCase(SESS, HOST).case_alarmer_notification_settings_common_post()

    def test_alarmer_notification_settings_user_get(self):
        AlarmerCase(SESS, HOST).case_alarmer_notification_settings_user_get()

    def test_alarmer_notification_settings_userone_post(self):
        AlarmerCase(SESS, HOST).case_alarmer_notification_settings_userone_post()

    def test_alarmer_notification_settings_type_post(self):
        AlarmerCase(SESS, HOST).case_alarmer_notification_settings_type_post()

    def test_alarmer_notification_user_all_get(self):
        AlarmerCase(SESS, HOST).case_alarmer_notification_settings_user_all_get()

    def test_alarmer_notification_user_get(self):
        AlarmerCase(SESS, HOST).case_alarmer_notification_user_get()

    def test_alarmer_send_invitation_post(self):
        AlarmerCase(SESS, HOST).case_alarmer_send_invitation_post()

    def test_alarmer_send_invitations_post(self):
        AlarmerCase(SESS, HOST).case_alarmer_send_invitations_post()

    def test_alarmer_send_msg_post(self):
        AlarmerCase(SESS, HOST).case_alarmer_send_msg_post()


class TestCore:

    def test_core_active_directory_get(self):
        CoreCase(SESS, HOST).case_core_active_directory_get()

    def test_core_active_directory_post(self):
        CoreCase(SESS, HOST).case_core_active_directory_post()

    def test_core_active_directory_structure_post(self):
        CoreCase(SESS, HOST).case_core_active_directory_structure_post()

    def test_core_active_directory_test_settings_post(self):
        CoreCase(SESS, HOST).case_core_active_directory_test_settings_post()

    def test_core_check_get(self):
        CoreCase(SESS, HOST).case_core_check_get()

    def test_core_common_get(self):
        CoreCase(SESS, HOST).case_core_common_get()

    def test_core_common_post(self):
        CoreCase(SESS, HOST).case_core_common_post()

    def test_core_common_test_post(self):
        CoreCase(SESS, HOST).case_core_common_test_post()

    def test_core_component_ml_restart_get(self):
        CoreCase(SESS, HOST).case_core_component_ml_restart_get()

    def test_core_component_picker_restart_get(self):
        CoreCase(SESS, HOST).case_core_component_picker_restart_get()

    # "code":400
    def test_core_component_servicedb_restart_get(self):  # считаем 400 ответ правильным, система не даст перезапустить
        CoreCase(SESS, HOST).case_core_component_servicedb_restart_get()

    # "code":400
    def test_core_component_datastore_restart_get(self):
        CoreCase(SESS, HOST).core_component_datastore_restart_get()

    def test_core_download_settings_get(self):
        CoreCase(SESS, HOST).case_core_download_settings_get()

    def test_core_email_import_cert_post(self):
        CoreCase(SESS, HOST).case_core_email_import_cert_post()

    def test_core_email_send_test_post(self):
        CoreCase(SESS, HOST).case_core_email_send_test_post()

    def test_core_email_in_get(self):
        CoreCase(SESS, HOST).case_core_email_in_get()

    def test_core_email_out_get(self):
        CoreCase(SESS, HOST).case_core_email_out_get()

    def test_core_email_in_post(self):
        CoreCase(SESS, HOST).case_core_email_in_post()

    def test_core_email_out_post(self):
        CoreCase(SESS, HOST).case_core_email_out_post()

    def test_core_flag_get(self):
        CoreCase(SESS, HOST).case_core_flag_get()

    def test_core_ip_get(self):
        CoreCase(SESS, HOST).case_core_ip_get()

    def test_core_nodes_list_ml_get(self):
        CoreCase(SESS, HOST).case_core_nodes_list_ml_get()

    def test_core_nodes_list_picker_get(self):
        CoreCase(SESS, HOST).case_core_nodes_list_picker_get()

    def test_core_nodes_list_servicedb_get(self):
        CoreCase(SESS, HOST).case_core_nodes_list_servicedb_get()

    def test_core_nodes_list_datastore_get(self):
        CoreCase(SESS, HOST).case_core_nodes_list_datastore_get()

    def test_core_nodes_ml_get(self):
        CoreCase(SESS, HOST).case_core_nodes_ml_get()

    def test_core_nodes_picker_get(self):
        CoreCase(SESS, HOST).case_core_nodes_picker_get()

    def test_core_nodes_servicedb_get(self):
        CoreCase(SESS, HOST).case_core_nodes_servicedb_get()

    def test_core_nodes_datastore_get(self):
        CoreCase(SESS, HOST).case_core_nodes_datastore_get()

    def test_core_service_dp_alarmer_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_alarmer_restart_get()

    def test_core_service_dp_auth_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_auth_restart_get()

    # "code":400
    def test_core_service_dp_core_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_core_restart_get()

    def test_core_service_dp_licenser_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_licenser_restart_get()

    def test_core_service_dp_log_eater_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_log_eater_restart_get()

    def test_core_service_dp_monitor_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_monitor_restart_get()

    def test_core_service_dp_peopler_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_peopler_restart_get()

    # "code":400
    def test_core_service_dp_permitter_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_permitter_restart_get()

    # "code":400
    def test_core_service_dp_postgres_single_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_postgres_single_restart_get()

    def test_core_service_dp_taskplan_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_taskplan_restart_get()

    def test_core_service_dp_updater_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_updater_restart_get()

    def test_core_service_dp_absorber_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_absorber_restart_get()

    def test_core_service_dp_picker_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_picker_restart_get()

    def test_core_service_dp_storage_single_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_storage_single_restart_get()

    def test_core_service_dp_storage_worker_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_storage_worker_restart_get()

    def test_core_service_dp_ml_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_ml_restart_get()

    def test_core_service_dp_scripter_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_scripter_restart_get()

    def test_core_service_dp_datapie_baker_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_datapie_baker_restart_get()

    def test_core_service_dp_elements_eater_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_elements_eater_restart_get()

    # "code":400
    def test_core_service_dp_frontend_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_frontend_restart_get()

    def test_core_service_dp_reporter_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_reporter_restart_get()

    def test_core_service_dp_rm_cook_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_rm_cook_restart_get()

    def test_core_service_dp_rm_ml_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_rm_ml_restart_get()

    def test_core_service_dp_screener_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_screener_restart_get()

    def test_core_service_dp_visualisation_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_visualisation_restart_get()

    def test_core_service_dp_xba_cook_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_xba_cook_restart_get()

    def test_core_service_dp_xba_py_restart_get(self):
        CoreCase(SESS, HOST).case_core_service_dp_xba_py_restart_get()

    @pytest.mark.skip
    def test_core_service_all_restart_get(self):  # стенд не тянет этот метод!
        CoreCase(SESS, HOST).case_core_service_all_restart_get()

    def test_core_sid_get(self):
        CoreCase(SESS, HOST).case_core_sid_get()

    def test_core_syslog_get(self):
        CoreCase(SESS, HOST).case_core_syslog_get()

    def test_core_syslog_post(self):
        CoreCase(SESS, HOST).case_core_syslog_post()


class TestElementsEater:

    def test_elements_eater_reports_export_post(self):
        ElementsEaterCase(SESS, HOST).case_elements_eater_reports_export_post()

    def test_elements_eater_reports_import_post(self):
        ElementsEaterCase(SESS, HOST).case_elements_eater_reports_import_post()


class TestLicenser:

    def test_licenser_activate_post(self):
        LicenserCase(SESS, HOST).case_licenser_activate_post()

    def test_licenser_license_info_get(self):
        LicenserCase(SESS, HOST).case_licenser_license_info_get()


class TestLogEater:

    def test_log_eater_audit_users_days_get(self):
        LogEaterCase(SESS, HOST).case_log_eater_audit_users_days_get()


class TestPeopler:

    def test_peopler_mainpage_get(self):
        PeoplerCase(SESS, HOST).case_peopler_mainpage_get()

    def test_peopler_many_users_post(self):
        PeoplerCase(SESS, HOST).case_peopler_many_users_post()

    def test_peopler_many_users_put(self):
        PeoplerCase(SESS, HOST).case_peopler_many_users_put()

    def test_peopler_profile_get(self):
        PeoplerCase(SESS, HOST).case_peopler_profile_get()

    def test_peopler_profiles_get(self):
        PeoplerCase(SESS, HOST).case_peopler_profiles_get()

    def test_peopler_users_get(self):
        PeoplerCase(SESS, HOST).case_peopler_users_get()

    def test_peopler_users_post(self):
        PeoplerCase(SESS, HOST).case_peopler_users_post()

    def test_peopler_users_id_get(self):
        PeoplerCase(SESS, HOST).case_peopler_users_id_get()

    def test_peopler_users_id_put(self):
        PeoplerCase(SESS, HOST).case_peopler_users_id_put()

    def test_peopler_users_delete(self):
        PeoplerCase(SESS, HOST).case_peopler_users_delete()

    # def __del__(self):    # FIXME >> after class
    def test_all_api_auto_test_user_delete(self):
        PeoplerCase(SESS, HOST).all_api_auto_test_user_delete()


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

    def test_permitter_db_watcher_db_tables_id_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_db_watcher_db_tables_id_get()
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

    @pytest.mark.skip  # FIXME: падает; хз
    def test_permitter_element_flags_mailing_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_flags_mailing_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip  # FIXME: падает; хардкод
    def test_permitter_element_flags_script_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_flags_script_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip  # FIXME: падает; хардкод
    def test_permitter_element_flags_script_sequence_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_flags_script_sequence_get()
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

    def test_permitter_element_rules_query_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_query_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_visualisation_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_visualisation_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_report_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_report_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_mailing_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_mailing_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_script_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_script_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_script_sequence_get(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_script_sequence_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_query_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_query_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_visualisation_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_visualisation_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_report_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_report_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_mailing_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_mailing_post()
        assert resp.status_code == 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_permitter_element_rules_script_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_script_post()
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip  # FIXME: падает; хардкод
    def test_permitter_element_rules_script_sequence_post(self):
        req = Permitter(SESS, HOST)
        resp = req.permitter_element_rules_script_sequence_post()
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

    def test_rm_cook_active_directory_groups_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_active_directory_groups_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_groups_id_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_active_directory_groups_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_state_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_active_directory_state_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_top_groups_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_active_directory_top_groups_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_top_users_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_active_directory_top_users_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_users_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_active_directory_users_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_active_directory_users_id_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_active_directory_users_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_calculation_start_calc_id_post(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_calculation_start_calc_id_post()
        assert resp.status_code == 200 or 429, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_rm_logs_last_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_rm_logs_last_get()
        assert resp.status_code == 200 or 429, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_recommendations_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_rm_recommendations_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_rm_roles_id_alias_post(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_rm_roles_id_alias_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_rm_roles_id_alias_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_rm_roles_id_alias_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_status_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_rm_status_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_role_model_result_export_role_model_to_excel_post(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_role_model_result_export_role_model_to_excel_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_role_model_result_groups_by_role_id_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_role_model_result_groups_by_role_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_resources_by_role_id_get(self):  # Не реализовано
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_role_model_result_resources_by_role_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_role_model_result_roles_by_source_source_id_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_role_model_result_roles_by_source_source_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_role_model_result_source_source_id_users_by_role_role_id_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_role_model_result_source_source_id_users_by_role_role_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_table_role_role_id_resources_by_user_user_id_get(self):  # Не используется
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_role_model_result_table_role_role_id_resources_by_user_user_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_table_role_role_id_users_by_resource_resource_id_get(self):  # Не используется
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_role_model_result_table_role_role_id_users_by_resource_resource_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_form_role_role_id_groups_by_user_user_id_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_role_model_result_form_role_role_id_groups_by_user_user_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_role_model_result_form_role_role_id_users_by_group_user_id_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_role_model_result_form_role_role_id_users_by_group_user_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_settings_calc_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_settings_calc_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_rm_cook_settings_calc_put(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_settings_calc_put()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_settings_mailings_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_settings_mailings_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip # qa@ku.ku
    def test_rm_cook_settings_mailings_post(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_settings_mailings_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_settings_sources_get(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_settings_sources_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_rm_cook_settings_sources_post(self):
        req = RmCook(SESS, HOST)
        resp = req.rm_cook_settings_sources_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestStorageWorker:

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

    def test_storage_worker_statistics_db_stats_dbname_get(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_statistics_db_stats_dbname_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_db_tabs_event_stats_db_name_tab_name_flag_post(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_statistics_db_tabs_event_stats_db_name_tab_name_flag_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_db_tabs_stats_dbname_get(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_statistics_db_tabs_stats_dbname_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_storage_search_post(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_statistics_storage_search_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_storage_worker_statistics_test_selection_post(self):
        req = StorageWorker(SESS, HOST)
        resp = req.storage_worker_statistics_test_selection_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

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

    def test_xba_cook_entity_picker_max_min_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_entity_picker_max_min_post()
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

    @pytest.mark.skip # нужно заполнение при prof_id=None, data=None
    def test_xba_cook_profiles_graph_drilldown_id_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_graph_drilldown_id_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_graph_drilldown_id_post_xx_descriprion_key_check(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_graph_drilldown_id_post_xx_descriprion_key_check()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

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

    def test_xba_cook_profiles_groups_group_id_profiles_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_groups_group_id_profiles_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip # нужен group_id хотя бы с одним пользователем
    def test_xba_cook_profiles_groups_id_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_groups_id_post()
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

    # @pytest.mark.skip
    def test_xba_cook_profiles_id_log_last_get(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_id_log_last_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_id_whitelist_post(self):
        req = XbaCook(SESS, HOST)
        resp = req.xba_cook_profiles_id_whitelist_post()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_xba_cook_profiles_id_whitelist_element_post(self):
            req = XbaCook(SESS, HOST)
            resp = req.xba_cook_profiles_id_whitelist_element_post()
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


class TestMonitor:

    def test_monitor_anomals_flag_0_post(self):
        MonitorCase(SESS, HOST).case_monitor_anomals_flag_0_post()

    def test_monitor_anomals_flag_1_post(self):
        MonitorCase(SESS, HOST).case_monitor_anomals_flag_1_post()

    def test_monitor_anomals_flag_2_post(self):
        MonitorCase(SESS, HOST).case_monitor_anomals_flag_2_post()

    def test_monitor_anomals_flag_3_post(self):
        MonitorCase(SESS, HOST).case_monitor_anomals_flag_3_post()

    def test_monitor_anomals_flag_4_post(self):
        MonitorCase(SESS, HOST).case_monitor_anomals_flag_4_post()

    def test_monitor_dump_server_post(self):
        MonitorCase(SESS, HOST).case_monitor_dump_server_post()

    def test_monitor_dump_nodes_post(self):
        MonitorCase(SESS, HOST).case_monitor_dump_nodes_post()

    def test_monitor_nodes_graphs_ml_metrics_post(self):
        MonitorCase(SESS, HOST).case_monitor_nodes_graphs_ml_metrics_post()

    def test_monitor_nodes_graphs_picker_metrics_post(self):
        MonitorCase(SESS, HOST).case_monitor_nodes_graphs_picker_metrics_post()

    def test_monitor_nodes_graphs_servicedb_metrics_post(self):
        MonitorCase(SESS, HOST).case_monitor_nodes_graphs_servicedb_metrics_post()

    def test_monitor_nodes_graphs_datastore_ram_post(self):
        MonitorCase(SESS, HOST).case_monitor_nodes_graphs_datastore_metrics_post()

    def test_monitor_nodes_stats_ml_get(self):
        MonitorCase(SESS, HOST).case_monitor_nodes_stats_ml_get()

    def test_monitor_nodes_stats_picker_get(self):
        MonitorCase(SESS, HOST).case_monitor_nodes_stats_picker_get()

    def test_monitor_nodes_stats_servicedb_get(self):
        MonitorCase(SESS, HOST).case_monitor_nodes_stats_servicedb_get()

    def test_monitor_nodes_stats_datastore_get(self):
        MonitorCase(SESS, HOST).case_monitor_nodes_stats_datastore_get()

    def test_monitor_webserver_graphs_ram_post(self):
        MonitorCase(SESS, HOST).case_monitor_webserver_graphs_ram_post()

    def test_monitor_webserver_graphs_cpu_post(self):
        MonitorCase(SESS, HOST).case_monitor_webserver_graphs_cpu_post()

    def test_monitor_webserver_graphs_iops_post(self):
        MonitorCase(SESS, HOST).case_monitor_webserver_graphs_iops_post()

    def test_monitor_webserver_graphs_network_post(self):
        MonitorCase(SESS, HOST).case_monitor_webserver_graphs_network_post()

    def test_monitor_webserver_groups_get(self):
        MonitorCase(SESS, HOST).case_monitor_webserver_groups_get()

    def test_monitor_webserver_stats_sys_get(self):
        MonitorCase(SESS, HOST).case_monitor_webserver_stats_sys_get()

    def test_monitor_webserver_stats_visual_get(self):
        MonitorCase(SESS, HOST).case_monitor_webserver_stats_visual_get()

    def test_monitor_webserver_stats_analytics_get(self):
        MonitorCase(SESS, HOST).case_monitor_webserver_stats_analytics_get()

    def test_monitor_webserver_stats_datastore_get(self):
        MonitorCase(SESS, HOST).case_monitor_webserver_stats_datastore_get()

    def test_monitor_webserver_stats_dataproc_get(self):
        MonitorCase(SESS, HOST).case_monitor_webserver_stats_dataproc_get()


class TestReporter:

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

    @pytest.mark.skip
    def test_reporter_screener_fast_xlsx_id_get(self):  # xlsx формируется на фронте
        req = Reporter(SESS, HOST)
        resp = req.reporter_screener_fast_xlsx_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_reporter_mailing_id_delete(self):
        req = Reporter(SESS, HOST)
        resp = req.reporter_mailing_id_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

class TestScripter:

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
        resp = req.scripter_script_script_id_log_log_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_script_id_log_log_id_delete(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_script_script_id_log_log_id_delete()
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
        resp = req.scripter_sequence_stop_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_scripter_sequence_id_log_get(self):
        req = Scripter(SESS, HOST)
        resp = req.scripter_sequence_sequence_id_log_last_get()
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


class TestUpdater:

    def test_updater_additions_get(self):
        req = Updater(SESS, HOST)
        resp = req.updater_additions_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # TODO: check 200 or 400
    def test_updater_additions_addition_delete(self):
        req = Updater(SESS, HOST)
        resp = req.updater_additions_addition_delete()
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    # TODO: check 200 or 400
    def test_updater_additions_addition_post(self):
        req = Updater(SESS, HOST)
        resp = req.updater_additions_addition_post()
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    # TODO: check 200 or 400
    def test_updater_check_updates_get(self):
        req = Updater(SESS, HOST)
        resp = req.updater_check_updates_get()
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestVisualisation:

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

    def test_visualisation_query_query_id_get(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_query_query_id_get()
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
        resp = req.visualisation_visualisation_visualisation_id_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_visualisation_visualisation_visualisation_id_delete(self):
        req = Visualisation(SESS, HOST)
        resp = req.visualisation_visualisation_visualisation_id_delete()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
