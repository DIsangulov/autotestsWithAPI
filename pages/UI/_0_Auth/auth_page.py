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

    # FIXME: зависимости
    def enter_as_user(self):
        self.page.fill(AuthLocators.LOGIN_INPUT, TestUsers.DpQaa.get("username"))
        self.page.fill(AuthLocators.PASSWORD_INPUT, TestUsers.DpQaa.get("password"))
        self.page.click(AuthLocators.PASS_VISIBLE)
        self.page.click(AuthLocators.ENTER_BUTTON)
        self.page.click(MainLocators.SIDE_BAR)

    # FIXME: зависимости
    def should_enter_be_successful(self):
        assert self.is_element_present(MainLocators.SUCCESS_ENTER), "Unsuccessful enter"

    # FIXME: зависимости
    def log_out(self):
        self.page.mouse.click(0, 0)
        self.page.click(MainLocators.HUMAN_ICON)
        self.page.click(MainLocators.SIGN_OUT)

    # FIXME: зависимости
    def enter_as_local_user(self):
        self.page.fill(AuthLocators.LOGIN_INPUT, TestUsers.DpQaaLocal.get("username"))
        self.page.fill(AuthLocators.PASSWORD_INPUT, TestUsers.DpQaaLocal.get("password"))
        self.page.click(AuthLocators.PASS_VISIBLE)
        self.page.click(AuthLocators.CHECKBOX_LOCAL)
        self.page.click(AuthLocators.ENTER_BUTTON)

    # FIXME: зависимости -> C_SideBar
    def open_side_bar(self):  # открытие бокового меню
        self.page.click(MainLocators.SIDE_BAR)
