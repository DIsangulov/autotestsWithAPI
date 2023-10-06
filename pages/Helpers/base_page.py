from playwright.sync_api import Page

from pages.Helpers.n_navigation import Navigation
from resourses.credentials import TestUsers, TARGET_URL


class BasePage(Navigation):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.username = None

        self.host = TARGET_URL
        self.page_path = "/"

        self.page.set_default_timeout(10000)

    def auth(self, *, auth_data: dict = TestUsers.DpQaaLocal):
        # todo: переложить локаторы надо куда-то...
        LOGIN_INPUT = "//input[@type='email']"
        PASSWORD_INPUT = "//input[@id='password']"
        CHECKBOX_LOCAL = "//input[@type='checkbox']/.."
        ENTER_BUTTON = "//button[span[contains(text(), 'Войти')]]"

        self.page.goto(self.host)
        self.page.fill(LOGIN_INPUT, auth_data.get("username"))
        self.page.fill(PASSWORD_INPUT, auth_data.get("password"))
        if auth_data.get("local"):
            self.page.click(CHECKBOX_LOCAL)
        self.page.click(ENTER_BUTTON)
        self.HEADER_LOGO.wait_for(state="visible")

        self.username = auth_data.get("username")

    def open(self):
        self.page.goto(self.host + self.page_path)
        self.page.wait_for_url(self.host + self.page_path)

    def goto_page(self, page_path: str):
        self.page.goto(self.host + page_path)
