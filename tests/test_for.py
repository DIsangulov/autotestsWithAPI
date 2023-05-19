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

    @pytest.mark.skip
    def test_should_enter_adm_roles_be_successful(self, browser):
        page = Roles(browser, link)
        page.should_enter_adm_roles_be_successful()

    def test_try_to_ui_fonts_and_styles(self, browser):
        page = Roles(browser, link)
        page.try_to_ui_fonts_and_styles()

    # def test_try_to_figma_fonts_and_styles(self, browser):
    #     page = Roles(browser, link)
    #     page.try_to_figma_fonts_and_styles()

    # def test_try_to_figma_fonts_and_styles_by_pwr(self, browser):
    #     page = Roles(browser, link)
    #     page.try_to_figma_fonts_and_styles_by_pwr()

    def test_try_to_figma_fonts_and_styles_parse_json(self, browser):
        page = Roles(browser, link)
        page.try_to_get_figma_fonts_and_styles_parse_json()
