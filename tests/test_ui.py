import allure
import pytest

from pages.UI._0_Auth.auth_page import AuthPage
from pages.UI._1_Administration.adm_roles import Roles
from pages.UI._1_Administration.adm_sessions import Sessions
from pages.UI._1_Administration.adm_users import Users
from pages.UI._4_xBA.xba_profiles import Profiles
from pages.UI._4_xBA.xba_statistic import Statistic
from pages.UI._5_RoleMining.rm_settings import Settings
from pages.UI._5_RoleMining.rm_ad_status import AdStatus
from pages.UI._5_RoleMining.rm_groups_and_users import GroupsAndUsers
from pages.UI._5_RoleMining.rm_role_model import RoleModel

# ________ constants __________
# region
link = "https://10.130.0.22"


# endregion
# ________ constants __________

class TestAdministration:
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


@pytest.mark.skip
class TestRoleMining:
    def test_valid_auth(self, browser):
        page = AuthPage(browser, link)
        page.open()
        page.enter_as_user()
        # page.should_enter_be_successful()

    def test_open_role_mining_settings(self, browser):
        page = Settings(browser, link)
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
