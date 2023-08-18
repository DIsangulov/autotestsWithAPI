from playwright.sync_api import Page

from pages.Helpers.n_navigation import Navigation
from resourses.credentials import TestUsers, TARGET_URL
from resourses.locators import AuthLocators, MainLocators


class BasePage(Navigation):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.username = None

        self.host = TARGET_URL
        self.page_path = "/"

        self.page.set_default_timeout(10000)

    def auth(self, *, auth_data: dict = TestUsers.DpQaaLocal):
        self.page.goto(self.host)
        self.page.fill(AuthLocators.LOGIN_INPUT, auth_data.get("username"))
        self.page.fill(AuthLocators.PASSWORD_INPUT, auth_data.get("password"))
        if auth_data.get("local"):
            self.page.click(AuthLocators.CHECKBOX_LOCAL)
        self.page.click(AuthLocators.ENTER_BUTTON)
        self.page.wait_for_selector(MainLocators.HEADER_LOGO)

        self.username = auth_data.get("username")

    def open(self):
        self.page.goto(self.host + self.page_path)
        self.page.wait_for_url(self.host + self.page_path)

    def goto_page(self, page_path: str):
        self.page.goto(self.host + page_path)

    # todo: зависимости -> from playwright.sync_api import expect
    def is_element_present(self, selector: str):
        return self.page.query_selector(selector)
