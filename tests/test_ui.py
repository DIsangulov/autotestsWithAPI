import allure
import pytest

from pages.UI._0_Auth.auth_page import AuthPage
from pages.UI._1_Administration.adm_licenses import Licenses
from pages.UI._1_Administration.adm_monitoring import Monitoring
from pages.UI._1_Administration.adm_notification_log import NotificationLog
from pages.UI._1_Administration.adm_roles import Roles
from pages.UI._1_Administration.adm_sessions import Sessions
from pages.UI._1_Administration.adm_settings import Settings
from pages.UI._1_Administration.adm_update import Update
from pages.UI._1_Administration.adm_users import Users
from pages.UI._2_Data.data_scripts import Scripts
from pages.UI._2_Data.data_sources import Sources
from pages.UI._2_Data.data_storage import Storage
from pages.UI._4_xBA.xba_profiles import Profiles
from pages.UI._4_xBA.xba_statistic import Statistic
from pages.UI._5_RoleMining.rm_settings import RmSettings
from pages.UI._5_RoleMining.rm_ad_status import AdStatus
from pages.UI._5_RoleMining.rm_groups_and_users import GroupsAndUsers
from pages.UI._5_RoleMining.rm_role_model import RoleModel

# ________ constants __________
# region
link = "https://10.130.0.22"


# endregion
# ________ constants __________

class TestAdministration:  # Администрирование
    def test_valid_auth(self, browser):
        page = AuthPage(browser, link)
        page.open()
        page.enter_as_user()

    def test_open_adm_roles(self, browser):
        page = Roles(browser, link)
        page.open_adm_roles()

    def test_should_enter_adm_roles_be_successful(self, browser):
        page = Roles(browser, link)
        page.should_enter_adm_roles_be_successful()

    def test_open_adm_users(self, browser):
        page = Users(browser, link)
        page.open_adm_users()

    def test_should_enter_adm_users_be_successful(self, browser):
        page = Users(browser, link)
        page.should_enter_adm_users_be_successful()

    def test_open_adm_sessions(self, browser):
        page = Sessions(browser, link)
        page.open_adm_sessions()

    def test_should_enter_adm_sessions_be_successful(self, browser):
        page = Sessions(browser, link)
        page.should_enter_adm_sessions_be_successful()

    def test_open_adm_monitoring(self, browser):
        page = Monitoring(browser, link)
        page.open_adm_monitoring()

    def test_should_enter_adm_monitoring_be_successful(self, browser):
        page = Monitoring(browser, link)
        page.should_enter_adm_monitoring_be_successful()

    def test_open_adm_licenses(self, browser):
        page = Licenses(browser, link)
        page.open_adm_licenses()

    def test_should_enter_adm_licenses_be_successful(self, browser):
        page = Licenses(browser, link)
        page.should_enter_adm_licenses_be_successful()

    def test_open_adm_update(self, browser):
        page = Update(browser, link)
        page.open_adm_update()

    def test_should_enter_adm_update_be_successful(self, browser):
        page = Update(browser, link)
        page.should_enter_adm_update_be_successful()

    def test_open_adm_notification_log_user(self, browser):
        page = NotificationLog(browser, link)
        page.open_adm_notification_log_user()

    def test_should_enter_adm_notification_log_user_be_successful(self, browser):
        page = NotificationLog(browser, link)
        page.should_enter_adm_notification_log_user_be_successful()

    def test_open_adm_notification_log_admin(self, browser):
        page = NotificationLog(browser, link)
        page.open_adm_notification_log_admin()

    def test_should_enter_adm_notification_log_admin_be_successful(self, browser):
        page = NotificationLog(browser, link)
        page.should_enter_adm_notification_log_admin_be_successful()

    def test_open_adm_settings_admin_node(self, browser):
        page = Settings(browser, link)
        page.open_adm_settings_admin_node()

    def test_should_enter_adm_settings_admin_node_be_successful(self, browser):
        page = Settings(browser, link)
        page.should_enter_adm_settings_admin_node_be_successful()

    def test_open_adm_settings_domain_controller(self, browser):
        page = Settings(browser, link)
        page.open_adm_settings_domain_controller()

    def test_should_enter_adm_settings_domain_controller_be_successful(self, browser):
        page = Settings(browser, link)
        page.should_enter_adm_settings_domain_controller_be_successful()

    def test_open_adm_settings_service_db_controller(self, browser):
        page = Settings(browser, link)
        page.open_adm_settings_service_db()

    def test_should_enter_adm_settings_service_db_be_successful(self, browser):
        page = Settings(browser, link)
        page.should_enter_adm_settings_service_db_be_successful()

    def test_open_adm_settings_storage(self, browser):
        page = Settings(browser, link)
        page.open_adm_settings_storage()

    def test_should_enter_adm_settings_storage_be_successful(self, browser):
        page = Settings(browser, link)
        page.should_enter_adm_settings_storage_be_successful()

    def test_open_adm_settings_data_collection(self, browser):
        page = Settings(browser, link)
        page.open_adm_settings_data_collection()

    def test_should_enter_adm_settings_data_collection_be_successful(self, browser):
        page = Settings(browser, link)
        page.should_enter_adm_settings_data_collection_be_successful()

    def test_open_adm_settings_data_analysis(self, browser):
        page = Settings(browser, link)
        page.open_adm_settings_data_analysis()

    def test_should_enter_adm_settings_data_analysis_be_successful(self, browser):
        page = Settings(browser, link)
        page.should_enter_adm_settings_data_analysis_be_successful()

    def test_open_adm_settings_post(self, browser):
        page = Settings(browser, link)
        page.open_adm_settings_post()

    def test_should_enter_adm_settings_post_be_successful(self, browser):
        page = Settings(browser, link)
        page.should_enter_adm_settings_post_be_successful()

    def test_open_adm_settings_syslog(self, browser):
        page = Settings(browser, link)
        page.open_adm_settings_syslog()

    def test_should_enter_adm_settings_syslog_be_successful(self, browser):
        page = Settings(browser, link)
        page.should_enter_adm_settings_syslog_be_successful()

    def test_open_adm_settings_secrets(self, browser):
        page = Settings(browser, link)
        page.open_adm_settings_secrets()

    def test_should_enter_adm_settings_secrets_be_successful(self, browser):
        page = Settings(browser, link)
        page.should_enter_adm_settings_secrets_be_successful()


@pytest.mark.skip
class TestData:  # Данные
    def test_valid_auth(self, browser):
        page = AuthPage(browser, link)
        page.open()
        page.enter_as_user()

    def test_open_data_sources(self, browser):
        page = Sources(browser, link)
        page.open_data_sources()

    def test_should_enter_data_sources_be_successful(self, browser):
        page = Sources(browser, link)
        page.should_enter_data_sources_be_successful()

    def test_open_data_scripts(self, browser):
        page = Scripts(browser, link)
        page.open_data_scripts()

    def test_should_enter_data_scripts_be_successful(self, browser):
        page = Scripts(browser, link)
        page.should_enter_data_scripts_be_successful()

    def test_open_data_storage_structure(self, browser):
        page = Storage(browser, link)
        page.open_data_storage_structure()

    def test_should_enter_data_storage_structure_be_successful(self, browser):
        page = Storage(browser, link)
        page.should_enter_data_storage_structure_be_successful()

    def test_open_data_storage_statistic(self, browser):
        page = Storage(browser, link)
        page.open_data_storage_statistics()

    def test_should_enter_data_storage_statistic_be_successful(self, browser):
        page = Storage(browser, link)
        page.should_enter_data_storage_statistics_be_successful()

    def test_open_data_storage_saerch_content(self, browser):
        page = Storage(browser, link)
        page.open_data_storage_search_content()

    def test_should_enter_data_storage_search_content_be_successful(self, browser):
        page = Storage(browser, link)
        page.should_enter_data_storage_search_content_be_successful()

    def test_open_data_storage_saerch_column(self, browser):
        page = Storage(browser, link)
        page.open_data_storage_search_column()

    def test_should_enter_data_storage_search_column_be_successful(self, browser):
        page = Storage(browser, link)
        page.should_enter_data_storage_search_column_be_successful()

    def test_open_data_storage_import_rules(self, browser):
        page = Storage(browser, link)
        page.open_data_storage_import_rules()

    def test_should_enter_data_storage_import_rules_be_successful(self, browser):
        page = Storage(browser, link)
        page.should_enter_data_storage_import_rules_be_successful()


@pytest.mark.skip
class TestRoleMining:
    def test_valid_auth(self, browser):
        page = AuthPage(browser, link)
        page.open()
        page.enter_as_user()
        # page.should_enter_be_successful()

    def test_open_role_mining_settings(self, browser):
        page = RmSettings(browser, link)
        page.open()
        page.open_rm_settings()

    def test_open_role_mining_ad_status(self, browser):
        page = AdStatus(browser, link)
        page.open()
        page.open_rm_ad_status()

    def test_open_role_mining_groups_and_users(self, browser):
        page = GroupsAndUsers(browser, link)
        page.open()
        page.open_rm_groups_and_users()

    def test_open_role_mining_role_model(self, browser):
        page = RoleModel(browser, link)
        page.open()
        page.open_rm_role_model()


@pytest.mark.skip
class TestStatistic:
    def test_valid_auth(self, browser):
        page = AuthPage(browser, link)
        page.open()
        page.enter_as_user()
        page.should_enter_be_successful()

    def test_open_xba_statistic(self, browser):
        page = Statistic(browser, link)
        page.open_xba_statistic()

    def test_save_xba_diagram_image(self, browser):
        page = Statistic(browser, link)
        page.save_xba_diagram_image()

    def test_compare_images(self, browser):
        page = Statistic(browser, link)
        page.compare_images()
