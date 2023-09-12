import pytest
import urllib3

from resourses.credentials import TARGET_URL
from tests.case.api.auth import AuthApiCase
from tests.case.api.absorber import AbsorberCase
from tests.case.api.alarmer import AlarmerCase
from tests.case.api.core import CoreCase
from tests.case.api.elements_eater import ElementsEaterCase
from tests.case.api.licenser import LicenserCase
from tests.case.api.log_eater import LogEaterCase
from tests.case.api.monitor import MonitorCase
from tests.case.api.peopler import PeoplerCase
from tests.case.api.permitter import PermitterCase
from tests.case.api.reporter import ReporterCase
from tests.case.api.rm_cook import RmCookCase
from tests.case.api.scripter import ScripterCase
from tests.case.api.storage_worker import StorageWorkerCase
from tests.case.api.taskplan import TaskplanCase
from tests.case.api.updater import UpdaterCase
from tests.case.api.visualisation import VisualisationCase
from tests.case.api.xba_cook import XbaCookCase

urllib3.disable_warnings()


@pytest.fixture(autouse=True, scope='session')
def _print_debug_info():
    print("\n" + "="*42)
    print(f"TARGET_URL: {TARGET_URL}")
    print("="*42 + "\n")
    yield


class TestAuth:

    def test_auth_ad_struct_get(self):
        AuthApiCase().case_auth_ad_struct_get()

    def test_auth_local_register_post(self):
        AuthApiCase(with_auth=False).case_auth_local_register_post()

    def test_auth_logout_get(self):
        AuthApiCase().case_auth_logout_get()

    def test_auth_ou_users_post(self):
        AuthApiCase().case_auth_ou_users_post()

    def test_auth_sessions_get(self):
        AuthApiCase().case_auth_sessions_get()

    def test_auth_sessions_uid_get(self):
        AuthApiCase().case_auth_sessions_uid_get()

    def test_auth_sessions_one_sid_del(self):
        AuthApiCase().case_auth_sessions_one_sid_del()

    def test_auth_sessions_all_uid_del(self):
        AuthApiCase().case_auth_sessions_all_uid_del()


class TestAbsorber:

    def test_absorber_library_columns_get(self):
        AbsorberCase().case_absorber_library_columns_get()

    def test_absorber_library_conn_type_get(self):
        AbsorberCase().case_absorber_library_conn_type_get()

    def test_absorber_library_conn_type_id_get(self):
        AbsorberCase().case_absorber_library_conn_type_id_get()

    def test_absorber_library_connector_get(self):
        AbsorberCase().case_absorber_library_connector_get()

    def test_absorber_library_connector_post(self):
        AbsorberCase().case_absorber_library_connector_post()

    def test_absorber_library_connector_put(self):
        AbsorberCase().case_absorber_library_connector_put()

    def test_absorber_library_connector_id_get(self):
        AbsorberCase().case_absorber_library_connector_id_get()

    def test_absorber_library_connector_id_delete(self):
        AbsorberCase().case_absorber_library_connector_id_delete()

    @pytest.mark.skip   # todo: new
    def test_absorber_library_external_driver_post(self):
        AbsorberCase().case_absorber_library_external_driver_post()

    @pytest.mark.skip   # todo: new
    def test_absorber_library_external_pattern_post(self):
        AbsorberCase().case_absorber_library_external_pattern_post()

    def test_absorber_library_logo_post(self):
        AbsorberCase().case_absorber_library_logo_post()

    def test_library_logo_put(self):
        AbsorberCase().case_absorber_library_logo_put()

    def test_absorber_library_logo_get(self):
        AbsorberCase().case_absorber_library_logo_get()

    def test_absorber_library_logo_id_get(self):
        AbsorberCase().case_absorber_library_logo_id_get()

    def test_absorber_library_logo_delete(self):
        AbsorberCase().case_absorber_library_logo_delete()

    def test_absorber_source_get(self):
        AbsorberCase().case_absorber_source_get()

    def test_absorber_source_post(self):
        AbsorberCase().case_absorber_source_post()

    def test_absorber_source_put(self):
        AbsorberCase().case_absorber_source_put()

    def test_absorber_source_id_get(self):
        AbsorberCase().case_absorber_source_id_get()

    @pytest.mark.skip   # fixme:
    def test_absorber_source_id_debug_get(self):
        AbsorberCase().case_absorber_source_id_debug_get()

    def test_absorber_source_id_log_get(self):
        AbsorberCase().case_absorber_source_id_log_get()

    def test_absorber_source_id_delete(self):
        AbsorberCase().case_absorber_source_id_delete()


class TestAlarmer:

    def test_alarmer_alert_service_names_get(self):
        AlarmerCase().case_alarmer_alert_service_names_get()

    @pytest.mark.skip   # todo: new
    def test_alarmer_email_server_post(self):
        AlarmerCase().case_alarmer_email_server_post()

    def test_alarmer_email_server_get(self):
        AlarmerCase().case_alarmer_email_server_get()

    @pytest.mark.skip   # todo: new
    def test_alarmer_email_server_id_get(self):
        AlarmerCase().case_alarmer_email_server_id_get()

    @pytest.mark.skip   # todo: new
    def test_alarmer_email_server_id_delete(self):
        AlarmerCase().case_alarmer_email_server_id_delete()

    def test_alarmer_notification_admin_all_get(self):
        AlarmerCase().case_alarmer_notification_admin_all_get()

    def test_alarmer_notification_read_admin_get(self):
        AlarmerCase().case_alarmer_notification_read_admin_get()

    def test_alarmer_notification_read_type_admin_post(self):
        AlarmerCase().case_alarmer_notification_read_type_admin_post()

    def test_alarmer_notification_settings_admin_get(self):
        AlarmerCase().case_alarmer_notification_settings_admin_get()

    def test_alarmer_notification_settings_common_get(self):
        AlarmerCase().case_alarmer_notification_settings_common_get()

    def test_alarmer_notification_settings_common_post(self):
        AlarmerCase().case_alarmer_notification_settings_common_post()

    def test_alarmer_notification_settings_user_get(self):
        AlarmerCase().case_alarmer_notification_settings_user_get()

    def test_alarmer_notification_settings_userone_post(self):
        AlarmerCase().case_alarmer_notification_settings_userone_post()

    def test_alarmer_notification_settings_type_post(self):
        AlarmerCase().case_alarmer_notification_settings_type_post()

    def test_alarmer_notification_user_all_get(self):
        AlarmerCase().case_alarmer_notification_settings_user_all_get()

    def test_alarmer_notification_user_get(self):
        AlarmerCase().case_alarmer_notification_user_get()

    def test_alarmer_notification_type_read_post(self):
        AlarmerCase().case_alarmer_notification_type_read_post()

    def test_alarmer_notifications_page_size_x_read_notify_type_page_x_get(self):
        AlarmerCase().case_alarmer_notifications_page_size_x_read_notify_type_page_x_get()

    def test_alarmer_send_invitation_post(self):
        AlarmerCase().case_alarmer_send_invitation_post()

    def test_alarmer_send_invitations_post(self):
        AlarmerCase().case_alarmer_send_invitations_post()

    def test_alarmer_send_msg_post(self):
        AlarmerCase().case_alarmer_send_msg_post()


class TestCore:

    def test_core_active_directory_get(self):
        CoreCase().case_core_active_directory_get()

    @pytest.mark.skip   # fixme: изменение настроек
    def test_core_active_directory_post(self):
        CoreCase().case_core_active_directory_post()

    @pytest.mark.skip   # fixme: изменение настроек
    def test_core_active_directory_structure_post(self):
        CoreCase().case_core_active_directory_structure_post()

    @pytest.mark.skip   # fixme: изменение настроек
    def test_core_active_directory_test_settings_post(self):
        CoreCase().case_core_active_directory_test_settings_post()

    def test_core_backups_get(self):
        CoreCase().case_core_backups_get()

    @pytest.mark.skip   # todo: empty
    def test_core_backups_post(self):
        CoreCase().case_core_backups_post()

    def test_core_backups_last_get(self):
        CoreCase().case_core_backups_last_get()

    @pytest.mark.skip   # todo: empty
    def test_core_backups_id_get(self):
        CoreCase().case_core_backups_id_get()

    @pytest.mark.skip   # todo: empty
    def test_core_backups_id_delete(self):
        CoreCase().case_core_backups_id_delete()

    @pytest.mark.skip   # todo: empty
    def test_core_backups_id_restore_post(self):
        CoreCase().case_core_backups_id_restore_post()

    @pytest.mark.skip   # todo: empty
    def test_core_backups_type_upload_post(self):
        CoreCase().case_core_backups_type_upload_post()

    @pytest.mark.skip   # todo: empty
    def test_core_backups_type_id_download_get(self):
        CoreCase().case_core_backups_type_id_download_get()

    def test_core_check_get(self):
        CoreCase().case_core_check_get()

    def test_core_common_get(self):
        CoreCase().case_core_common_get()

    @pytest.mark.skip   # fixme: изменение настроек
    def test_core_common_post(self):
        CoreCase().case_core_common_post()

    @pytest.mark.skip   # fixme: изменение настроек
    def test_core_common_test_post(self):
        CoreCase().case_core_common_test_post()

    def test_core_component_ml_restart_get(self):
        CoreCase().case_core_component_ml_restart_get()

    def test_core_component_picker_restart_get(self):
        CoreCase().case_core_component_picker_restart_get()

    # "code":400
    def test_core_component_servicedb_restart_get(self):  # считаем 400 ответ правильным, система не даст перезапустить
        CoreCase().case_core_component_servicedb_restart_get()

    # "code":400
    def test_core_component_datastore_restart_get(self):
        CoreCase().core_component_datastore_restart_get()

    def test_core_download_settings_get(self):
        CoreCase().case_core_download_settings_get()

    # @pytest.mark.skip   # fixme: изменение настроек
    def test_core_email_import_cert_post(self):
        CoreCase().case_core_email_import_cert_post()

    # @pytest.mark.skip   # fixme: изменение настроек
    def test_core_email_send_test_post(self):
        CoreCase().case_core_email_send_test_post()

    def test_core_email_in_get(self):
        CoreCase().case_core_email_in_get()

    def test_core_email_out_get(self):
        CoreCase().case_core_email_out_get()

    # @pytest.mark.skip   # fixme: изменение настроек
    def test_core_email_in_post(self):
        CoreCase().case_core_email_in_post()

    # @pytest.mark.skip   # fixme: изменение настроек
    def test_core_email_out_post(self):
        CoreCase().case_core_email_out_post()

    def test_core_flag_get(self):
        CoreCase().case_core_flag_get()

    def test_core_ip_get(self):
        CoreCase().case_core_ip_get()

    @pytest.mark.skip   # todo: empty
    def test_core_nodes_delete_what_post(self):
        CoreCase().case_core_nodes_delete_what_post()

    def test_core_nodes_list_ml_get(self):
        CoreCase().case_core_nodes_list_ml_get()

    def test_core_nodes_list_picker_get(self):
        CoreCase().case_core_nodes_list_picker_get()

    def test_core_nodes_list_servicedb_get(self):
        CoreCase().case_core_nodes_list_servicedb_get()

    def test_core_nodes_list_datastore_get(self):
        CoreCase().case_core_nodes_list_datastore_get()

    @pytest.mark.skip   # todo: empty
    def test_core_nodes_test_what_post(self):
        CoreCase().case_core_nodes_test_what_post()

    def test_core_nodes_ml_get(self):
        CoreCase().case_core_nodes_ml_get()

    def test_core_nodes_picker_get(self):
        CoreCase().case_core_nodes_picker_get()

    def test_core_nodes_servicedb_get(self):
        CoreCase().case_core_nodes_servicedb_get()

    def test_core_nodes_datastore_get(self):
        CoreCase().case_core_nodes_datastore_get()

    @pytest.mark.skip   # todo: empty
    def test_core_nodes_what_post(self):
        CoreCase().case_core_nodes_what_post()

    @pytest.mark.skip   # todo: empty
    def test_core_save_get(self):
        CoreCase().case_core_save_get()

    @pytest.mark.skip   # todo: empty
    def test_core_secrets_get(self):
        CoreCase().case_core_secrets_get()

    @pytest.mark.skip   # todo: empty
    def test_core_secrets_post(self):
        CoreCase().case_core_secrets_post()

    @pytest.mark.skip   # todo: empty
    def test_core_secrets_id_get(self):
        CoreCase().case_core_secrets_id_get()

    @pytest.mark.skip   # todo: empty
    def test_core_secrets_id_put(self):
        CoreCase().case_core_secrets_id_put()

    @pytest.mark.skip   # todo: empty
    def test_core_secrets_id_delete(self):
        CoreCase().case_core_secrets_id_delete()

    def test_core_service_dp_alarmer_restart_get(self):
        CoreCase().case_core_service_dp_alarmer_restart_get()

    def test_core_service_dp_auth_restart_get(self):
        CoreCase().case_core_service_dp_auth_restart_get()

    # "code":400
    def test_core_service_dp_core_restart_get(self):
        CoreCase().case_core_service_dp_core_restart_get()

    def test_core_service_dp_licenser_restart_get(self):
        CoreCase().case_core_service_dp_licenser_restart_get()

    def test_core_service_dp_log_eater_restart_get(self):
        CoreCase().case_core_service_dp_log_eater_restart_get()

    def test_core_service_dp_monitor_restart_get(self):
        CoreCase().case_core_service_dp_monitor_restart_get()

    def test_core_service_dp_peopler_restart_get(self):
        CoreCase().case_core_service_dp_peopler_restart_get()

    # "code":400
    def test_core_service_dp_permitter_restart_get(self):
        CoreCase().case_core_service_dp_permitter_restart_get()

    # "code":400
    def test_core_service_dp_postgres_single_restart_get(self):
        CoreCase().case_core_service_dp_postgres_single_restart_get()

    def test_core_service_dp_taskplan_restart_get(self):
        CoreCase().case_core_service_dp_taskplan_restart_get()

    def test_core_service_dp_updater_restart_get(self):
        CoreCase().case_core_service_dp_updater_restart_get()

    def test_core_service_dp_absorber_restart_get(self):
        CoreCase().case_core_service_dp_absorber_restart_get()

    def test_core_service_dp_picker_restart_get(self):
        CoreCase().case_core_service_dp_picker_restart_get()

    def test_core_service_dp_storage_single_restart_get(self):
        CoreCase().case_core_service_dp_storage_single_restart_get()

    def test_core_service_dp_storage_worker_restart_get(self):
        CoreCase().case_core_service_dp_storage_worker_restart_get()

    def test_core_service_dp_ml_restart_get(self):
        CoreCase().case_core_service_dp_ml_restart_get()

    def test_core_service_dp_scripter_restart_get(self):
        CoreCase().case_core_service_dp_scripter_restart_get()

    def test_core_service_dp_datapie_baker_restart_get(self):
        CoreCase().case_core_service_dp_datapie_baker_restart_get()

    def test_core_service_dp_elements_eater_restart_get(self):
        CoreCase().case_core_service_dp_elements_eater_restart_get()

    # "code":400
    def test_core_service_dp_frontend_restart_get(self):
        CoreCase().case_core_service_dp_frontend_restart_get()

    def test_core_service_dp_reporter_restart_get(self):
        CoreCase().case_core_service_dp_reporter_restart_get()

    def test_core_service_dp_rm_cook_restart_get(self):
        CoreCase().case_core_service_dp_rm_cook_restart_get()

    def test_core_service_dp_rm_ml_restart_get(self):
        CoreCase().case_core_service_dp_rm_ml_restart_get()

    def test_core_service_dp_screener_restart_get(self):
        CoreCase().case_core_service_dp_screener_restart_get()

    def test_core_service_dp_visualisation_restart_get(self):
        CoreCase().case_core_service_dp_visualisation_restart_get()

    def test_core_service_dp_xba_cook_restart_get(self):
        CoreCase().case_core_service_dp_xba_cook_restart_get()

    def test_core_service_dp_xba_py_restart_get(self):
        CoreCase().case_core_service_dp_xba_py_restart_get()

    @pytest.mark.skip   # стенд не тянет этот метод!
    def test_core_service_all_restart_get(self):
        CoreCase().case_core_service_all_restart_get()

    def test_core_sid_get(self):
        CoreCase().case_core_sid_get()

    def test_core_syslog_get(self):
        CoreCase().case_core_syslog_get()

    @pytest.mark.skip  # fixme: изменение настроек
    def test_core_syslog_post(self):
        CoreCase().case_core_syslog_post()


class TestElementsEater:

    def test_elements_eater_reports_export_post(self):
        ElementsEaterCase().case_elements_eater_reports_export_post()

    def test_elements_eater_reports_import_post(self):
        ElementsEaterCase().case_elements_eater_reports_import_post()


class TestLicenser:

    def test_licenser_activate_post(self):
        LicenserCase().case_licenser_activate_post()

    @pytest.mark.skip       # TODO: empty
    def test_licenser_file_activate_post(self):
        LicenserCase().case_licenser_file_activate_post()

    def test_licenser_license_info_get(self):
        LicenserCase().case_licenser_license_info_get()

    @pytest.mark.skip       # TODO: empty
    def test_licenser_set_company_post(self):
        LicenserCase().case_licenser_set_company_post()


class TestLogEater:

    def test_log_eater_audit_users_days_get(self):
        LogEaterCase().case_log_eater_audit_users_days_get()


class TestPeopler:

    def test_peopler_mainpage_get(self):
        PeoplerCase().case_peopler_mainpage_get()

    def test_peopler_many_users_post(self):
        PeoplerCase().case_peopler_many_users_post()

    def test_peopler_many_users_put(self):
        PeoplerCase().case_peopler_many_users_put()

    def test_peopler_pin_page_current_user_post(self):
        PeoplerCase().case_peopler_pin_page_current_user_post()

    def test_peopler_pin_page_current_user_delete(self):
        PeoplerCase().case_peopler_pin_page_current_user_delete()

    def test_peopler_pin_page_list_role_post(self):
        PeoplerCase().case_peopler_pin_page_list_role_post()

    def test_peopler_pin_page_list_user_post(self):
        PeoplerCase().case_peopler_pin_page_list_user_post()

    def test_peopler_pin_page_type_subject_post(self):
        PeoplerCase().case_peopler_pin_page_type_subject_post()

    def test_peopler_pin_page_type_subject_id_delete(self):
        PeoplerCase().case_peopler_pin_page_type_subject_id_delete()

    def test_peopler_pinned_page_status_post(self):
        PeoplerCase().case_peopler_pinned_page_status_post()

    def test_peopler_profile_get(self):
        PeoplerCase().case_peopler_profile_get()

    def test_peopler_profiles_get(self):
        PeoplerCase().case_peopler_profiles_get()

    def test_peopler_users_get(self):
        PeoplerCase().case_peopler_users_get()

    def test_peopler_users_post(self):
        PeoplerCase().case_peopler_users_post()

    def test_peopler_users_id_get(self):
        PeoplerCase().case_peopler_users_id_get()

    def test_peopler_users_id_put(self):
        PeoplerCase().case_peopler_users_id_put()

    def test_peopler_users_delete(self):
        PeoplerCase().case_peopler_users_delete()


class TestPermitter:

    def test_permitter_check_ui_get(self):
        PermitterCase().case_permitter_check_ui_get()

    def test_permitter_db_watcher_all_db_get(self):
        PermitterCase().case_permitter_db_watcher_all_db_get()

    def test_permitter_db_watcher_all_tables_get(self):
        PermitterCase().case_permitter_db_watcher_all_tables_get()

    def test_permitter_db_watcher_db_tables_id_get(self):
        PermitterCase().case_permitter_db_watcher_db_tables_id_get()

    def test_permitter_db_watcher_empty_role_dbs_get(self):
        PermitterCase().case_permitter_db_watcher_empty_role_dbs_get()

    def test_permitter_db_watcher_empty_role_tables_get(self):
        PermitterCase().case_permitter_db_watcher_empty_role_tables_get()

    def test_permitter_db_watcher_empty_role_tables_id_get(self):
        PermitterCase().case_permitter_db_watcher_empty_role_tables_id_get()

    def test_permitter_db_watcher_get_tab_name_id_get(self):
        PermitterCase().case_permitter_db_watcher_get_tab_name_id_get()

    def test_permitter_element_flags_query_id_get(self):
        PermitterCase().case_permitter_element_flags_query_id_get()

    def test_permitter_element_flags_visualisation_id_get(self):
        PermitterCase().case_permitter_element_flags_visualisation_id_get()

    def test_permitter_element_flags_report_id_get(self):
        PermitterCase().case_permitter_element_flags_report_id_get()

    def test_permitter_element_flags_mailing_id_get(self):
        PermitterCase().case_permitter_element_flags_mailing_id_get()

    def test_permitter_element_flags_script_id_get(self):
        PermitterCase().case_permitter_element_flags_script_id_get()

    def test_permitter_element_flags_script_sequence_id_get(self):
        PermitterCase().case_permitter_element_flags_script_sequence_id_get()

    def test_permitter_element_flags_query_id_post(self):
        PermitterCase().case_permitter_element_flags_query_id_post()

    def test_permitter_element_flags_visualisation_id_post(self):
        PermitterCase().case_permitter_element_flags_visualisation_id_post()

    def test_permitter_element_flags_report_id_post(self):
        PermitterCase().case_permitter_element_flags_report_id_post()

    def test_permitter_element_flags_mailing_id_post(self):
        PermitterCase().case_permitter_element_flags_mailing_id_post()

    def test_permitter_element_flags_script_id_post(self):
        PermitterCase().case_permitter_element_flags_script_id_post()

    def test_permitter_element_flags_script_sequence_id_post(self):
        PermitterCase().case_permitter_element_flags_script_sequence_id_post()

    def test_permitter_element_rules_all_query_id_get(self):
        PermitterCase().case_permitter_element_rules_all_query_id_get()

    def test_permitter_element_rules_all_visualisation_id_get(self):
        PermitterCase().case_permitter_element_rules_all_visualisation_id_get()

    def test_permitter_element_rules_all_report_id_get(self):
        PermitterCase().case_permitter_element_rules_all_report_id_get()

    def test_permitter_element_rules_all_mailing_id_get(self):
        PermitterCase().case_permitter_element_rules_all_mailing_id_get()

    def test_permitter_element_rules_all_script_id_get(self):
        PermitterCase().case_permitter_element_rules_all_script_id_get()

    def test_permitter_element_rules_all_script_sequence_id_get(self):
        PermitterCase().case_permitter_element_rules_all_script_sequence_id_get()

    def test_permitter_element_rules_query_id_get(self):
        PermitterCase().case_permitter_element_rules_query_id_get()

    def test_permitter_element_rules_visualisation_id_get(self):
        PermitterCase().case_permitter_element_rules_visualisation_id_get()

    def test_permitter_element_rules_report_get(self):
        PermitterCase().case_permitter_element_rules_report_id_get()

    def test_permitter_element_rules_mailing_get(self):
        PermitterCase().case_permitter_element_rules_mailing_id_get()

    def test_permitter_element_rules_script_get(self):
        PermitterCase().case_permitter_element_rules_script_id_get()

    def test_permitter_element_rules_script_sequence_get(self):
        PermitterCase().case_permitter_element_rules_script_sequence_id_get()

    def test_permitter_element_rules_query_id_post(self):
        PermitterCase().case_permitter_element_rules_query_id_post()

    def test_permitter_element_rules_visualisation_id_post(self):
        PermitterCase().case_permitter_element_rules_visualisation_id_post()

    def test_permitter_element_rules_report_id_post(self):
        PermitterCase().case_permitter_element_rules_report_id_post()

    def test_permitter_element_rules_mailing_id_post(self):
        PermitterCase().case_permitter_element_rules_mailing_id_post()

    def test_permitter_element_rules_script_id_post(self):
        PermitterCase().case_permitter_element_rules_script_id_post()

    def test_permitter_element_rules_script_sequence_id_post(self):
        PermitterCase().case_permitter_element_rules_script_sequence_id_post()

    # todo: 200 -> в сообщении 400 статус код
    def test_permitter_element_rules_delete_element_type_query_element_id_post(self):
        PermitterCase().case_permitter_element_rules_delete_query_id_post()

    def test_permitter_roles_editor_roles_get(self):
        PermitterCase().case_permitter_roles_editor_roles_get()

    def test_permitter_roles_editor_roles_post(self):
        PermitterCase().case_permitter_roles_editor_roles_post()

    def test_permitter_roles_editor_roles_edit_id_get(self):
        PermitterCase().case_permitter_roles_editor_roles_edit_id_get()

    def test_permitter_roles_editor_roles_id_put(self):
        PermitterCase().case_permitter_roles_editor_roles_id_put()

    def test_permitter_roles_editor_roles_id_delete(self):
        PermitterCase().case_permitter_roles_editor_roles_id_delete()

    def test_permitter_user_rules_get(self):
        PermitterCase().case_permitter_user_rules_get()

    def test_permitter_users_elements_count_who_id_get(self):
        PermitterCase().case_permitter_users_elements_count_who_id_get()

    def test_permitter_users_new_author_who_id(self):
        PermitterCase().case_permitter_users_new_author_who_id_post()

    def test_permitter_user_rules_who_id_get(self):
        PermitterCase().case_permitter_user_rules_who_id_get()

    def test_permitter_role_rules_who_id_get(self):
        PermitterCase().case_permitter_role_rules_who_id_get()


class TestRmCook:

    def test_rm_cook_active_directory_groups_get(self):
        RmCookCase().case_rm_cook_active_directory_groups_get()

    def test_rm_cook_active_directory_groups_id_get(self):
        RmCookCase().case_rm_cook_active_directory_groups_id_get()

    def test_rm_cook_active_directory_state_get(self):
        RmCookCase().case_rm_cook_active_directory_state_get()

    def test_rm_cook_active_directory_top_groups_get(self):
        RmCookCase().case_rm_cook_active_directory_top_groups_get()

    def test_rm_cook_active_directory_top_users_get(self):
        RmCookCase().case_rm_cook_active_directory_top_users_get()

    def test_rm_cook_active_directory_users_get(self):
        RmCookCase().case_rm_cook_active_directory_users_get()

    def test_rm_cook_active_directory_users_id_get(self):
        RmCookCase().case_rm_cook_active_directory_users_id_get()

    @pytest.mark.skip   # rm calculation
    def test_rm_cook_calculation_start_calc_id_post(self):
        RmCookCase().case_rm_cook_calculation_start_calc_id_post()

    def test_rm_cook_rm_logs_last_get(self):
        RmCookCase().case_rm_cook_rm_logs_last_get()

    def test_rm_recommendations_get(self):
        RmCookCase().case_rm_cook_rm_recommendations_get()

    def test_rm_cook_rm_roles_id_alias_post(self):
        RmCookCase().case_rm_cook_rm_roles_id_alias_post()

    def test_rm_cook_rm_roles_id_alias_ts_get(self):
        RmCookCase().case_rm_cook_rm_roles_id_alias_ts_get()

    def test_rm_status_get(self):
        RmCookCase().case_rm_cook_rm_status_get()

    def test_rm_cook_role_model_result_export_role_model_to_excel_post(self):
        RmCookCase().case_rm_cook_role_model_result_export_role_model_to_excel_post()

    def test_rm_cook_role_model_result_groups_by_role_id_get(self):
        RmCookCase().case_rm_cook_role_model_result_groups_by_role_id_get()

    @pytest.mark.skip   # fixme
    def test_rm_cook_role_model_result_resources_by_role_id_get(self):
        RmCookCase().case_rm_cook_role_model_result_resources_by_role_id_get()

    def test_rm_cook_role_model_result_roles_by_source_source_id_get(self):
        RmCookCase().case_rm_cook_role_model_result_roles_by_source_source_id_get()

    def test_rm_cook_role_model_result_source_source_id_users_by_role_role_id_get(self):
        RmCookCase().case_rm_cook_role_model_result_source_0_users_by_role_0_get()

    @pytest.mark.skip   # fixme
    def test_rm_cook_role_model_result_table_role_role_id_resources_by_user_user_id_get(self):  # Не используется
        RmCookCase().case_rm_cook_role_model_result_table_role_role_id_resources_by_user_user_id_get()

    @pytest.mark.skip   # fixme
    def test_rm_cook_role_model_result_table_role_role_id_users_by_resource_resource_id_get(self):  # Не используется
        RmCookCase().case_rm_cook_role_model_result_table_role_role_id_users_by_resource_resource_id_get()

    def test_rm_cook_role_model_result_form_role_role_id_groups_by_user_user_id_get(self):
        RmCookCase().case_rm_cook_role_model_result_form_role_role_id_groups_by_user_user_id_get()

    def test_rm_cook_role_model_result_form_role_role_id_users_by_group_user_id_get(self):
        RmCookCase().case_rm_cook_role_model_result_form_role_role_id_users_by_group_user_id_get1()

    def test_rm_cook_settings_calc_get(self):
        RmCookCase().case_rm_cook_settings_calc_get()

    def test_rm_cook_settings_calc_put(self):
        RmCookCase().case_rm_cook_settings_calc_put()

    def test_rm_cook_settings_mailings_get(self):
        RmCookCase().case_rm_cook_settings_mailings_get()

    def test_rm_cook_settings_mailings_post(self):
        RmCookCase().case_rm_cook_settings_mailings_post()

    def test_rm_cook_settings_sources_get(self):
        RmCookCase().case_rm_cook_settings_sources_get()

    @pytest.mark.skip   # Поменять настройки источников Role mining
    def test_rm_cook_settings_sources_post(self):
        RmCookCase().case_rm_cook_settings_sources_post()


class TestStorageWorker:

    def test_storage_worker_ask_one_sql_post(self):
        StorageWorkerCase().case_storage_worker_ask_one_sql_post()

    def test_storage_worker_ask_plain_sql_post(self):
        StorageWorkerCase().case_storage_worker_ask_plain_sql_post()

    @pytest.mark.skip   # todo: empty
    def test_storage_worker_backups_get(self):
        StorageWorkerCase().case_storage_worker_backups_get()

    @pytest.mark.skip   # todo: empty
    def test_storage_worker_backups_table_db_name_table_name_post(self):
        StorageWorkerCase().case_storage_worker_backups_table_db_name_table_name_post()

    @pytest.mark.skip   # todo: empty
    def test_storage_worker_backups_id_get(self):
        StorageWorkerCase().case_storage_worker_backups_id_get()

    @pytest.mark.skip   # todo: empty
    def test_storage_worker_backups_id_delete(self):
        StorageWorkerCase().case_storage_worker_backups_id_delete()

    @pytest.mark.skip   # todo: empty
    def test_storage_worker_backups_id_download_get(self):
        StorageWorkerCase().case_storage_worker_backups_id_download_get()

    @pytest.mark.skip   # todo: empty
    def test_storage_worker_backups_id_restore_post(self):
        StorageWorkerCase().case_storage_worker_backups_id_restore_post()

    @pytest.mark.skip   # todo: empty
    def test_storage_worker_backups_type_upload_post(self):
        StorageWorkerCase().case_storage_worker_backups_type_upload_post()

    def test_storage_worker_import_rules_get(self):
        StorageWorkerCase().case_storage_worker_import_rules_get()

    def test_storage_worker_psevdo_namer_regs_post(self):
        StorageWorkerCase().case_storage_worker_psevdo_namer_regs_post()

    def test_storage_worker_psevdo_namer_regs_get(self):
        StorageWorkerCase().case_storage_worker_psevdo_namer_regs_get()

    def test_storage_worker_psevdo_namer_regs_pid_get(self):
        StorageWorkerCase().case_storage_worker_psevdo_namer_regs_pid_get()

    @pytest.mark.skip   # todo: empty
    def test_storage_worker_psevdo_namer_regs_pid_put(self):
        StorageWorkerCase().case_storage_worker_psevdo_namer_regs_pid_put()

    def test_storage_worker_psevdo_namer_regs_pid_delete(self):
        StorageWorkerCase().case_storage_worker_psevdo_namer_regs_pid_delete()

    def test_storage_worker_show_base_db_name_get(self):
        StorageWorkerCase().case_storage_worker_show_base_db_name_get()

    def test_storage_worker_statistics_db_event_stats_db_name_flag_post(self):
        StorageWorkerCase().case_storage_worker_statistics_db_event_stats_db_name_flag_post()

    def test_storage_worker_statistics_db_one_tab_stats_db_name_tab_name_get(self):
        StorageWorkerCase().case_storage_worker_statistics_db_one_tab_stats_db_name_tab_name_get()

    def test_storage_worker_statistics_db_search_post(self):
        StorageWorkerCase().case_storage_worker_statistics_db_search_post()

    def test_storage_worker_statistics_db_stats_dbname_get(self):
        StorageWorkerCase().case_storage_worker_statistics_db_stats_dbname_get()

    def test_storage_worker_statistics_db_tabs_event_stats_db_name_tab_name_flag_post(self):
        StorageWorkerCase().case_storage_worker_statistics_db_tabs_event_stats_db_name_tab_name_flag_post()

    def test_storage_worker_statistics_db_tabs_stats_dbname_get(self):
        StorageWorkerCase().case_storage_worker_statistics_db_tabs_stats_dbname_get()

    def test_storage_worker_statistics_storage_search_post(self):
        StorageWorkerCase().case_storage_worker_statistics_storage_search_post()

    def test_storage_worker_statistics_test_selection_post(self):
        StorageWorkerCase().case_storage_worker_statistics_test_selection_post()

    def test_storage_worker_storage_db_post(self):
        StorageWorkerCase().case_storage_worker_storage_db_post()

    def test_storage_worker_storage_db_get(self):
        StorageWorkerCase().case_storage_worker_storage_db_get()

    def test_storage_worker_storage_db_put(self):
        StorageWorkerCase().case_storage_worker_storage_db_put()

    def test_storage_worker_storage_db_delete(self):
        StorageWorkerCase().case_storage_worker_storage_db_delete()

    @pytest.mark.skip
    def test_storage_worker_storage_import_csv_db_name_table_name_post(self):
        StorageWorkerCase().case_storage_worker_storage_import_csv_db_name_table_name_post()

    @pytest.mark.skip
    def test_storage_worker_storage_import_json_db_name_table_name_post(self):
        StorageWorkerCase().case_storage_worker_storage_import_json_db_name_table_name_post()

    def test_storage_worker_storage_supported_engines_get(self):
        StorageWorkerCase().case_storage_worker_storage_supported_engines_get()

    def test_storage_worker_storage_supported_types_get(self):
        StorageWorkerCase().case_storage_worker_storage_supported_types_get()

    def test_storage_worker_storage_table_columns_db_name_tab_name_get(self):
        StorageWorkerCase().case_storage_worker_storage_table_columns_db_name_tab_name_get()

    @pytest.mark.skip   # fixme: check for DB existing
    def test_storage_worker_storage_table_db_name_post(self):
        StorageWorkerCase().case_storage_worker_storage_table_db_name_post()

    @pytest.mark.skip   # todo: empty
    def test_storage_worker_storage_table_db_name_table_name_post(self):
        StorageWorkerCase().case_storage_worker_storage_table_db_name_table_name_post()

    @pytest.mark.skip   # todo: empty
    def test_storage_worker_storage_view_db_name_post(self):
        StorageWorkerCase().case_storage_worker_storage_view_db_name_post()

    @pytest.mark.skip   # fixme: неверно передаются параметры
    def test_storage_worker_storage_table_columns_db_name_table_name_post(self):
        StorageWorkerCase().case_storage_worker_storage_table_columns_db_name_table_name_post()

    def test_storage_worker_storage_table_db_name_table_name_ttl_get(self):
        StorageWorkerCase().case_storage_worker_storage_table_db_name_table_name_ttl_get()

    @pytest.mark.skip   # todo: empty
    def test_storage_worker_storage_table_db_name_table_name_ttl_put(self):
        StorageWorkerCase().case_storage_worker_storage_table_db_name_table_name_ttl_put()

    def test_storage_worker_storage_table_db_name_table_name_count_get(self):
        StorageWorkerCase().case_storage_worker_storage_table_db_name_table_name_count_get()

    @pytest.mark.skip   # todo: empty
    def test_storage_worker_storage_table_db_name_table_name_column_name_delete(self):
        StorageWorkerCase().case_storage_worker_storage_table_db_name_table_name_column_name_delete()

    @pytest.mark.skip   # todo: empty
    def test_storage_worker_storage_table_db_name_table_name_delete(self):
        StorageWorkerCase().case_storage_worker_storage_table_db_name_table_name_delete()


class TestXbaCook:

    def test_xba_cook_profiles_post(self):
        XbaCookCase().case_xba_cook_profiles_post()

    def test_xba_cook_profiles_import_profiles_post(self):
        XbaCookCase().case_xba_cook_profiles_import_profiles_post()

    @pytest.mark.skip   # супер тяжелый запрос 30-120 секунд
    def test_xba_cook_anomalies_get(self):
        XbaCookCase().case_xba_cook_anomalies_get()

    def test_xba_cook_anomalies_picker_max_min_get(self):
        XbaCookCase().case_xba_cook_anomalies_picker_max_min_get()

    def test_xba_cook_check_entity_type_post(self):
        XbaCookCase().case_xba_cook_check_entity_type_post()

    def test_xba_cook_dashboard_entities_post(self):
        XbaCookCase().case_xba_cook_dashboard_entities_post()

    def test_xba_cook_dashboard_entities_more_post(self):
        XbaCookCase().case_xba_cook_dashboard_entities_more_post()

    def test_xba_cook_dashboard_groups_post(self):
        XbaCookCase().case_xba_cook_dashboard_groups_post()

    def test_xba_cook_dashboard_groups_more_post(self):
        XbaCookCase().case_xba_cook_dashboard_groups_more_post()

    def test_xba_cook_dashboard_profiles_post(self):
        XbaCookCase().case_xba_cook_dashboard_profiles_post()

    def test_xba_cook_dashboard_profiles_more_post(self):
        XbaCookCase().case_xba_cook_dashboard_profiles_more_post()

    def test_xba_cook_entity_post(self):
        XbaCookCase().case_xba_cook_entity_post()

    def test_xba_cook_entity_details_post(self):
        XbaCookCase().case_xba_cook_entity_details_post()

    # DAT-5186
    def test_xba_cook_entity_info_post(self):
        XbaCookCase().case_xba_cook_entity_info_post()

    def test_xba_cook_entity_info_settings_get(self):
        XbaCookCase().case_xba_cook_entity_info_settings_get()

    def test_xba_cook_entity_info_settings_post(self):
        XbaCookCase().case_xba_cook_entity_info_settings_post()

    def test_xba_cook_entity_info_settings_entity_type_delete(self):
        XbaCookCase().case_xba_cook_entity_info_settings_entity_type_delete()

    def test_xba_cook_entity_picker_max_min_post(self):
        XbaCookCase().case_xba_cook_entity_picker_max_min_post()

    def test_xba_cook_entity_risks_description_post(self):
        XbaCookCase().case_xba_cook_entity_risks_description_post()

    def test_xba_cook_max_min_post(self):
        XbaCookCase().case_xba_cook_max_min_post()

    def test_xba_cook_profiles_get(self):
        XbaCookCase().case_xba_cook_profiles_get()

    def test_xba_cook_profiles_start_id_get(self):
        XbaCookCase().case_xba_cook_profiles_start_id_get()

    def test_xba_cook_profiles_categories_get(self):
        XbaCookCase().case_xba_cook_profiles_categories_get()

    def test_xba_cook_profiles_export_profiles_post(self):
        XbaCookCase().case_xba_cook_profiles_export_profiles_post()

    def test_xba_cook_profiles_functions_get(self):
        XbaCookCase().case_xba_cook_profiles_functions_get()

    def test_xba_cook_profiles_graph_drilldown_statement_id_post(self):
        XbaCookCase().case_xba_cook_profiles_graph_drilldown_statement_id_post()

    @pytest.mark.skip
    def test_xba_cook_profiles_graph_drilldown_id_post(self):
        XbaCookCase().case_xba_cook_profiles_graph_drilldown_id_post()

    @pytest.mark.skip   # fixme: хк
    def test_xba_cook_profiles_graph_drilldown_34_post(self):
        XbaCookCase().case_xba_cook_profiles_graph_drilldown_34_post()

    def test_xba_cook_profiles_graph_personal_id_post(self):
        XbaCookCase().case_xba_cook_profiles_graph_personal_id_post()

    def test_xba_cook_profiles_graph_id_post(self):
        XbaCookCase().case_xba_cook_profiles_graph_id_post()

    def test_xba_cook_profiles_groups_post(self):
        XbaCookCase().case_xba_cook_profiles_groups_post()

    def test_xba_cook_profiles_groups_get(self):
        XbaCookCase().case_xba_cook_profiles_groups_get()

    def test_xba_cook_profiles_groups_put(self):
        XbaCookCase().case_xba_cook_profiles_groups_put()

    def test_xba_cook_profiles_groups_info_get(self):
        XbaCookCase().case_xba_cook_profiles_groups_info_get()

    def test_xba_cook_profiles_groups_group_id_profiles_get(self):
        XbaCookCase().case_xba_cook_profiles_groups_group_id_profiles_get()

    def test_xba_cook_profiles_groups_id_post(self):
        XbaCookCase().case_xba_cook_profiles_groups_id_post()

    @pytest.mark.skip
    def test_xba_cook_profiles_groups_id_max_min_get(self):
        XbaCookCase().case_xba_cook_profiles_groups_id_max_min_get()

    @pytest.mark.skip   # todo: new
    def test_xba_cook_profiles_groups_profile_id_group_id_delete(self):
        XbaCookCase().case_xba_cook_profiles_groups_profile_id_group_id_delete()

    @pytest.mark.skip
    def test_xba_cook_profiles_groups_profile_id_group_id_weight_get(self):
        XbaCookCase().case_xba_cook_profiles_groups_profile_id_group_id_weight_get()

    def test_xba_cook_profiles_stop_id_get(self):
        XbaCookCase().case_xba_cook_profiles_stop_id_get()

    def test_xba_cook_profiles_id_get(self):
        XbaCookCase().case_xba_cook_profiles_id_get()

    # DAT-5211
    def test_xba_cook_profiles_id_summary_post(self):
        XbaCookCase().case_xba_cook_profiles_id_summary_post()

    # DAT-5230
    def test_xba_cook_profiles_id_graph_post(self):
        XbaCookCase().case_xba_cook_profiles_id_graph_post()

    # DAT-5276
    def test_xba_cook_profiles_id_zones_post(self):
        XbaCookCase().case_xba_cook_profiles_id_zones_post()

    def test_xba_cook_profiles_id_log_last_get(self):
        XbaCookCase().case_xba_cook_profiles_id_log_last_get()

    def test_xba_cook_profiles_id_whitelist_post(self):
        XbaCookCase().case_xba_cook_profiles_id_whitelist_post()

    def test_xba_cook_profiles_id_whitelist_element_post(self):
        XbaCookCase().case_xba_cook_profiles_id_whitelist_element_post()

    def test_xba_cook_profiles_id_string_whitelist_get(self):
        XbaCookCase().case_xba_cook_profiles_id_string_whitelist_get()

    def test_xba_cook_profiles_id_list_whitelist_get(self):
        XbaCookCase().case_xba_cook_profiles_id_list_whitelist_get()

    @pytest.mark.skip   # todo
    def test_xba_cook_profiles_profile_id_whitelist_element_id_delete(self):
        XbaCookCase().case_xba_cook_profiles_profile_id_whitelist_element_id_delete()

    def test_xba_cook_xba_get(self):
        XbaCookCase().case_xba_cook_xba_get()

    @pytest.mark.skip   # TODO: empty
    def case_xba_cook_set_log_level_xba_py_mode_post(self):
        XbaCookCase().case_xba_cook_set_log_level_xba_py_mode_post()

    def test_xba_cook_xba_post(self):
        XbaCookCase().case_xba_cook_xba_post()

    def test_xba_cook_profiles_groups_id_delete(self):
        XbaCookCase().case_xba_cook_profiles_groups_id_delete()

    def test_xba_cook_profiles_max_min_id_get(self):
        XbaCookCase().case_xba_cook_profiles_max_min_id_get()

    def test_xba_cook_profiles_id_delete(self):
        XbaCookCase().case_xba_cook_profiles_id_delete()

    def test_xba_cook_profiles_id_post(self):
        XbaCookCase().case_xba_cook_profiles_id_post()


class TestMonitor:

    def test_monitor_dump_server_post(self):
        MonitorCase().case_monitor_dump_server_post()

    def test_monitor_dump_nodes_post(self):
        MonitorCase().case_monitor_dump_nodes_post()

    def test_monitor_fast_graph_post(self):
        MonitorCase().case_monitor_fast_graph_post()

    def test_monitor_fast_info_get(self):
        MonitorCase().case_monitor_fast_info_get()

    def test_monitor_nodes_graphs_what_metric_post(self):
        MonitorCase().case_monitor_nodes_graphs_what_metric_post()

    def test_monitor_nodes_stats_what_get(self):
        MonitorCase().case_monitor_nodes_stats_what_get()

    def test_monitor_webserver_graphs_metric_post(self):
        MonitorCase().case_monitor_webserver_graphs_metric_post()

    def test_monitor_webserver_groups_get(self):
        MonitorCase().case_monitor_webserver_groups_get()

    def test_monitor_webserver_stats_sys_get(self):
        MonitorCase().case_monitor_webserver_stats_sys_get()

    def test_monitor_webserver_stats_visual_get(self):
        MonitorCase().case_monitor_webserver_stats_visual_get()

    def test_monitor_webserver_stats_analytics_get(self):
        MonitorCase().case_monitor_webserver_stats_analytics_get()

    def test_monitor_webserver_stats_datastore_get(self):
        MonitorCase().case_monitor_webserver_stats_datastore_get()

    def test_monitor_webserver_stats_dataproc_get(self):
        MonitorCase().case_monitor_webserver_stats_dataproc_get()


class TestReporter:

    def test_reporter_mailing_post(self):
        ReporterCase().case_reporter_mailing_post()

    def test_reporter_mailing_sample_post(self):
        ReporterCase().case_reporter_mailing_sample_post()

    def test_reporter_mailing_get(self):
        ReporterCase().case_reporter_mailing_get()

    def test_reporter_mailing_put(self):
        ReporterCase().case_reporter_mailing_put()

    def test_reporter_mailing_typed_0_1_get(self):
        ReporterCase().case_reporter_mailing_typed_0_1_get()

    def test_reporter_mailing_type_2_3_get(self):
        ReporterCase().case_reporter_mailing_typed_2_3_get()

    def test_reporter_mailing_id_get(self):
        ReporterCase().case_reporter_mailing_id_get()

    def test_reporter_screener_fast_png_post(self):
        ReporterCase().case_reporter_screener_fast_png_post()

    def test_reporter_screener_fast_pdf_post(self):
        ReporterCase().case_reporter_screener_fast_pdf_post()

    def test_reporter_mailing_id_delete(self):
        ReporterCase().case_reporter_mailing_id_delete()


class TestScripter:

    def test_scripter_category_get(self):
        ScripterCase().case_scripter_category_get()

    def test_scripter_libs_get(self):
        ScripterCase().case_scripter_libs_get()

    def test_scripter_script_get(self):
        ScripterCase().case_scripter_script_get()

    def test_scripter_script_post(self):
        ScripterCase().case_scripter_script_post()

    def test_scripter_script_put(self):
        ScripterCase().case_scripter_script_put()

    def test_scripter_script_start_post(self):
        ScripterCase().case_scripter_script_start_post()

    def test_scripter_script_exec_list_get(self):
        ScripterCase().case_scripter_script_exec_list_get()

    def test_scripter_script_id_get(self):
        ScripterCase().case_scripter_script_id_get()

    def test_scripter_script_stop_id_get(self):
        ScripterCase().case_scripter_script_stop_id_get()

    def test_scripter_script_id_files_get(self):
        ScripterCase().case_scripter_script_id_files_get()

    def test_scripter_script_id_files_put(self):
        ScripterCase().case_scripter_script_id_files_put()

    def test_scripter_script_id_log_get(self):
        ScripterCase().case_scripter_script_id_log_get()

    @pytest.mark.skip   # todo: DAT-5427
    def test_scripter_script_id_log_id_get(self):
        ScripterCase().case_scripter_script_id_log_id_get()

    @pytest.mark.skip   # todo: DAT-5427
    def test_scripter_script_id_log_last_get(self):
        ScripterCase().case_scripter_script_id_log_last_get()

    def test_scripter_script_type_admin_get(self):
        ScripterCase().case_scripter_script_type_admin_get()

    def test_scripter_script_type_user_get(self):
        ScripterCase().case_scripter_script_type_user_get()

    def test_scripter_sequence_get(self):
        ScripterCase().case_scripter_sequence_get()

    def test_scripter_sequence_post(self):
        ScripterCase().case_scripter_sequence_post()

    def test_scripter_sequence_put(self):
        ScripterCase().case_scripter_sequence_put()

    def test_scripter_sequence_id_get(self):
        ScripterCase().case_scripter_sequence_id_get()

    def test_scripter_sequence_start_post(self):
        ScripterCase().case_scripter_sequence_start_post()

    def test_scripter_sequence_stop_get(self):
        ScripterCase().case_scripter_sequence_stop_id_get()

    def test_scripter_sequence_log_id_get(self):
        ScripterCase().case_scripter_sequence_log_id_get()

    def test_scripter_sequence_sequence_id_log_log_id_get(self):
        ScripterCase().case_scripter_sequence_sequence_id_log_log_id_get()

    def test_scripter_sequence_id_log_last_get(self):
        ScripterCase().case_scripter_sequence_sequence_id_log_last_get()

    def test_scripter_sequence_sequence_type_admin_get(self):
        ScripterCase().case_scripter_sequence_sequence_type_admin_get()

    def test_scripter_sequence_sequence_type_user_get(self):
        ScripterCase().case_scripter_sequence_sequence_type_user_get()

    def test_scripter_script_id_log_log_id_delete(self):
        ScripterCase().case_scripter_script_script_id_log_log_id_delete()

    def test_scripter_script_id_log_delete(self):
        ScripterCase().case_scripter_script_id_log_delete()

    def test_scripter_script_id_delete(self):
        ScripterCase().case_scripter_script_id_delete()

    def test_scripter_sequence_sequence_id_log_log_id_delete(self):
        ScripterCase().case_scripter_sequence_sequence_id_log_log_id_delete()

    def test_scripter_sequence_id_log_delete(self):
        ScripterCase().case_scripter_sequence_id_log_delete()

    def test_scripter_sequence_id_delete(self):
        ScripterCase().case_scripter_sequence_id_delete()


class TestTaskplan:

    def test_taskplan_add_task_post(self):
        TaskplanCase().case_taskplan_add_task_post()

    @pytest.mark.skip   # TODO: check
    def test_taskplan_delete_task(self):
        TaskplanCase().case_taskplan_delete_task()

    def test_taskplan_get_shedule_post(self):
        TaskplanCase().case_taskplan_get_shedule_post()


class TestUpdater:

    def test_updater_additions_get(self):
        UpdaterCase().case_updater_additions_get()

    def test_updater_additions_addition_post(self):
        UpdaterCase().case_updater_additions_addition_post()

    def test_updater_additions_addition_delete(self):
        UpdaterCase().case_updater_additions_addition_delete()

    def test_updater_check_updates_get(self):
        UpdaterCase().case_updater_check_updates_get()

    @pytest.mark.skip   # todo: check
    def test_updater_update_post(self):
        UpdaterCase().case_updater_update_post()

    @pytest.mark.skip   # todo: check
    def test_updater_update_from_archive_post(self):
        UpdaterCase().case_updater_update_from_archive_post()

    def test_updater_versions_get(self):
        UpdaterCase().case_updater_versions_get()


class TestVisualisation:

    def test_visualisation_query_get(self):
        VisualisationCase().case_visualisation_query_get()

    def test_visualisation_query_do_query_id_post(self):
        VisualisationCase().case_visualisation_query_do_query_id_post()

    # fixme: хк Weather_all_online
    def test_visualisation_query_save_post(self):
        VisualisationCase().case_visualisation_query_save_post()

    def test_visualisation_query_usage_id_get(self):
        VisualisationCase().case_visualisation_query_usage_id_get()

    def test_visualisation_query_query_id_get(self):
        VisualisationCase().case_visualisation_query_query_id_get()

    def test_visualisation_query_id_delete(self):
        VisualisationCase().case_visualisation_query_id_delete()

    def test_visualisation_reports_post(self):
        VisualisationCase().case_visualisation_reports_post()

    def test_visualisation_reports_get(self):
        VisualisationCase().case_visualisation_reports_get()

    @pytest.mark.skip   # todo: empty
    def test_visualisation_reports_params_report_id_post(self):
        VisualisationCase().case_visualisation_reports_params_report_id_post()

    def test_visualisation_reports_report_id_get(self):
        VisualisationCase().case_visualisation_reports_report_id_get()

    def test_visualisation_reports_report_id_delete(self):
        VisualisationCase().case_visualisation_reports_report_id_delete()

    def test_visualisation_visualisation_get(self):
        VisualisationCase().case_visualisation_visualisation_get()

    def test_visualisation_visualisation_post(self):
        VisualisationCase().case_visualisation_visualisation_post()

    def test_visualisation_visualisation_dataseries_visualisation_id_post(self):
        VisualisationCase().case_visualisation_visualisation_dataseries_visualisation_id_post()

    @pytest.mark.skip   # todo: empty
    def test_visualisation_visualisation_dataseries_visualisation_id_dataseries_id_delete(self):
        VisualisationCase().case_visualisation_visualisation_dataseries_visualisation_id_dataseries_id_delete()

    def test_visualisation_visualisation_types_get(self):
        VisualisationCase().case_visualisation_visualisation_types_get()

    def test_visualisation_visualisation_usage_visualisation_id_get(self):
        VisualisationCase().case_visualisation_visualisation_usage_visualisation_id_get()

    def test_visualisation_visualisation_visualisation_id_get(self):
        VisualisationCase().case_visualisation_visualisation_visualisation_id_get()

    def test_visualisation_visualisation_visualisation_id_delete(self):
        VisualisationCase().visualisation_visualisation_visualisation_id_delete()


class TestGarbageCollector:

    def test_all_api_auto_test_entity_delete(self):
        # удаление сущностей, оставленных после прогонки кейсов
        AbsorberCase().all_api_auto_test_entity_delete()
        PeoplerCase().all_api_auto_test_user_delete()
        PermitterCase().all_temp_roles_delete()
        StorageWorkerCase().all_api_auto_test_regs_delete()
        XbaCookCase().all_api_auto_test_entity_delete()
        ReporterCase().all_api_auto_test_mailing_delete()
        ScripterCase().all_api_auto_test_entity_delete()
        VisualisationCase().all_api_auto_test_entity_delete()

        AuthApiCase().case_auth_sessions_all_uid_del()
