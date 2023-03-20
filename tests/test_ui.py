import allure

from pages.UI._0_Auth.auth_page import AuthPage
from pages.UI._5_RoleMining.rm_settings import Settings
from pages.UI._5_RoleMining.rm_ad_status import AdStatus
from pages.UI._5_RoleMining.rm_groups_and_users import GroupsAndUsers
from pages.UI._5_RoleMining.rm_role_model import RoleModel

# ________ constants __________
# region
host = "https://10.130.0.22"


# endregion
# ________ constants __________


@allure.feature("UI - Страница авторизации")
class TestRoleMining:
    @allure.story("Авторизация под доменной учеткой")
    def test_valid_auth(self, browser):
        link = host
        page = AuthPage(browser, link)
        page.open()
        page.enter_as_user()
        # page.should_enter_be_successful()

    def test_open_role_mining_settings(self, browser):
        link = host
        page = Settings(browser, link)
        page.open()
        page.open_rm_settings()

    def test_open_role_mining_ad_status(self, browser):
        link = host
        page = AdStatus(browser, link)
        page.open()
        page.open_rm_ad_status()

    def test_open_role_mining_groups_and_users(self, browser):
        link = host
        page = GroupsAndUsers(browser, link)
        page.open()
        page.open_rm_groups_and_users()

    def test_open_role_mining_role_model(self, browser):
        link = host
        page = RoleModel(browser, link)
        page.open()
        page.open_rm_role_model()
