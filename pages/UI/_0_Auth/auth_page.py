from playwright.sync_api import Page

from pages.Helpers.base_page import BasePage
from resourses.credentials import TestUsers
from resourses.locators import AuthLocators, MainLocators


class AuthPage(BasePage):

    page_path = "/auth"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = AuthPage.page_path

        self.LOGIN_INPUT = page.locator(AuthLocators.LOGIN_INPUT)
        self.PASSWORD_INPUT = page.locator(AuthLocators.PASSWORD_INPUT)
        self.PASSWORD_VISIBLE = page.locator(AuthLocators.PASS_VISIBLE)

        self.CHECKBOX_LOCAL = page.locator(AuthLocators.CHECKBOX_LOCAL)
        self.ENTER_BUTTON = page.locator(AuthLocators.ENTER_BUTTON)

        self.WRONG_LOGPASS_ALERT = page.locator(AuthLocators.WRONG_LOG_PASS_ALERT)

        # self.REGISTER_LINK = page.locator()   # todo:
