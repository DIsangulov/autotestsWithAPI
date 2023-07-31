from playwright.sync_api import Page

from pages.Helpers.base_page import BasePage
from resourses.credentials import TestUsers
from resourses.locators import AuthLocators, MainLocators

# login = 'dataplan_qaa@ngrsoftlab.ru'
# password = 'fHNHQBc7jEKfaO0kywZz!!'

# login_local = 'dataplan_qaa'
# password_local = 'dataplan_qaa'

# locators  # fixme: убрать в init
LOGIN_INPUT = "//input[@type='email']"
PASSWORD_INPUT = "//input[@type='password']"
CHECKBOX_LOCAL = "//input[@type='checkbox']/.."  # FIXME: contains text = локально
ENTER_BUTTON = "//*[contains(text(),'Войти')]"
PASS_VISIBLE = "//span[@class='icon is-right has-text-primary is-clickable']"


class AuthPage(BasePage):

    def __init__(self, page: Page, host: str):
        super().__init__(page, host)
        self.page_path = ""

        # TODO: убрать _1
        self.LOGIN_INPUT_1 = page.locator(LOGIN_INPUT)
        self.PASSWORD_INPUT_1 = page.locator(PASSWORD_INPUT)
        self.PASSWORD_VISIBLE_1 = page.locator(PASS_VISIBLE)

        self.CHECKBOX_LOCAL_1 = page.locator(CHECKBOX_LOCAL)
        self.ENTER_BUTTON = page.locator(ENTER_BUTTON)
        # self.REGISTER_LINK = page.locator()   # todo:

    # FIXME: зависимости
    def enter_as_user(self):
        self.page.fill(LOGIN_INPUT, TestUsers.DpQaa.get("username"))
        self.page.fill(PASSWORD_INPUT, TestUsers.DpQaa.get("password"))
        self.page.click(PASS_VISIBLE)
        self.page.click(ENTER_BUTTON)
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
        self.page.fill(LOGIN_INPUT, TestUsers.DpQaaLocal.get("username"))
        self.page.fill(PASSWORD_INPUT, TestUsers.DpQaaLocal.get("password"))
        self.page.click(PASS_VISIBLE)
        self.page.click(CHECKBOX_LOCAL)
        self.page.click(ENTER_BUTTON)

    # FIXME: зависимости -> C_SideBar
    def open_side_bar(self):  # открытие бокового меню
        self.page.click(MainLocators.SIDE_BAR)
