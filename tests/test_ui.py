import time

import allure

from pages.Helpers.base_page import BasePage
from pages.UI._0_Auth.auth_page import AuthPage
from pages.UI._5_RoleMining._1_Settings.rm_settings_page import RoleMining
from resourses.locators import AuthLocators, MainLocators, RoleMiningLocators

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
        page.should_enter_be_successful()

    def test_open_role_mining_settings(self, browser):
        link = host
        page = RoleMining(browser, link)
        page.open()
        page.open_rm_settings()
