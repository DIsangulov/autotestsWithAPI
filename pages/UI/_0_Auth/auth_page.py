import time

from playwright.sync_api import Playwright, Page

from pages.Helpers.base_page import BasePage
from resourses.locators import AuthLocators, MainLocators, RoleMiningLocators

login = 'dataplan_qaa@ngrsoftlab.ru'
password = 'fHNHQBc7jEKfaO0kywZz!!'

login_local = 'dataplan_qaa'
password_local = 'dataplan_qaa'


class AuthPage(BasePage):

    def enter_as_user(self):
        self.page.fill(AuthLocators.LOGIN_INPUT, login)
        self.page.fill(AuthLocators.PAS_INPUT, password)
        self.page.click(AuthLocators.PASS_VISIBLE)
        self.page.click(AuthLocators.ENTER_BUT)
        self.page.click(MainLocators.SIDE_BAR)

    def should_enter_be_successful(self):
        assert self.is_element_present(MainLocators.SUCCESS_ENTER), "Unsuccessful enter"

    def log_out(self):
        self.page.click(MainLocators.HUMAN_ICON)
        self.page.click(MainLocators.SIGN_OUT)

    def enter_as_local_user(self):
        self.page.fill(AuthLocators.LOGIN_INPUT, login_local)
        self.page.fill(AuthLocators.PAS_INPUT, password_local)
        self.page.click(AuthLocators.PASS_VISIBLE)
        self.page.click(MainLocators.LOCAL_CHECK_BOX)
        self.page.click(AuthLocators.ENTER_BUT)
        # self.page.click(MainLocators.SIDE_BAR)
