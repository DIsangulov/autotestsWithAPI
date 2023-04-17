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
from pages.UI._3_Analytics.an_mailing_lists import MailingLists
from pages.UI._3_Analytics.an_reports import Reports
from pages.UI._3_Analytics.an_requests import Requests
from pages.UI._3_Analytics.an_visualization import Visualisation
from pages.UI._4_xBA.xba_metaprofiles import Metaprofiles
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
@pytest.mark.skip
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
class TestAnalytics:  # Аналитика
    def test_valid_auth(self, browser):
        page = AuthPage(browser, link)
        page.open()
        page.enter_as_user()

    def test_open_an_mailing_lists_reports(self, browser):
        page = MailingLists(browser, link)
        page.open_an_mailing_lists_reports()

    def test_should_enter_an_mailing_lists_reports_be_successful(self, browser):
        page = MailingLists(browser, link)
        page.should_enter_an_mailing_lists_reports_be_successful()

    def test_open_an_reports(self, browser):
        page = Reports(browser, link)
        page.open_an_reports()

    def test_should_enter_an_reports_be_successful(self, browser):
        page = Reports(browser, link)
        page.should_enter_an_reports_be_successful()

    def test_open_an_visualisation(self, browser):
        page = Visualisation(browser, link)
        page.open_an_visualisation()

    def test_should_enter_an_visualisation_be_successful(self, browser):
        page = Visualisation(browser, link)
        page.should_enter_an_visualisation_be_successful()

    def test_open_an_requests(self, browser):
        page = Requests(browser, link)
        page.open_an_requests()

    def test_should_enter_an_requests_be_successful(self, browser):
        page = Requests(browser, link)
        page.should_enter_an_requests_be_successful()


@pytest.mark.skip
class TestXBA:
    def test_valid_auth(self, browser):
        page = AuthPage(browser, link)
        page.open()
        page.enter_as_user()
        page.should_enter_be_successful()

    def test_open_xba_profiles(self, browser):
        page = Profiles(browser, link)
        page.open_xba_profiles()

    def test_should_enter_xba_profiles_be_successful(self, browser):
        page = Profiles(browser, link)
        page.should_enter_xba_profiles_be_successful()

    def test_open_xba_metaprofiles(self, browser):
        page = Metaprofiles(browser, link)
        page.open_xba_metaprofiles()

    def test_should_enter_xba_metaprofiles_be_successful(self, browser):
        page = Metaprofiles(browser, link)
        page.should_enter_xba_metaprofiles_be_successful()

    def test_open_xba_statistic(self, browser):
        page = Statistic(browser, link)
        page.open_xba_statistic()

    def test_should_enter_xba_statistic_be_successful(self, browser):
        page = Statistic(browser, link)
        page.should_enter_xba_statistic_be_successful()


class TestRoleMining:
    def test_valid_auth(self, browser):
        page = AuthPage(browser, link)
        page.open()
        page.enter_as_user()
        page.should_enter_be_successful()

    def test_open_rm_ad_status_statistic(self, browser):
        page = AdStatus(browser, link)
        page.open_rm_ad_status_statistic()

    def test_should_enter_rm_ad_status_statistic_be_successful(self, browser):
        page = AdStatus(browser, link)
        page.should_enter_rm_ad_status_statistic_be_successful()

    def test_open_rm_ad_status_recommendation(self, browser):
        page = AdStatus(browser, link)
        page.open_rm_ad_status_recommendation()

    def test_should_enter_rm_ad_status_recommendation_be_successful(self, browser):
        page = AdStatus(browser, link)
        page.should_enter_rm_ad_status_recommendation_be_successful()

    def test_role_mining_settings_page(self, browser):
        page = RmSettings(browser, link)
        page.open_rm_settings_sources()
        # page.should_enter_rm_settings_sources_be_successful()
        # page.open_rm_settings_calculation_settings()
        # page.should_enter_rm_settings_calculation_settings_be_successful()
        page.clear_sources_rm_settings()
        page.not_confirm_cleaning_rm_settings()
        page.clear_sources_rm_settings()
        page.confirm_cleaning_rm_settings()
        page.selecting_values_from_dropdown_list()
        page.should_sources_saved()
        page.should_sources_recalculated()
