from playwright.sync_api import Page

from resourses.credentials import TestUsers
from resourses.locators import AuthLocators, MainLocators


class BasePage:

    HOST: str = None

    @staticmethod
    def set_host(new_host: str):
        BasePage.HOST = new_host

    # def __init__(self, page: Page, host: str, timeout: int = 10):
    def __init__(self, page: Page):
        self.page = page

        self.username = None

        self.host = BasePage.HOST
        self.page_path = "/"

        # self.page.set_default_timeout(timeout * 1000)

    def auth(self, *, auth_data: dict = TestUsers.DpQaaLocal):
        self.host = BasePage.HOST
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

    def goto_page(self, page_path: str):
        self.page.goto(self.host + page_path)

    def open_new_tab(self, link):
        self.page.click(f'text={link}')
        self.page.wait_for_selector(f'//a[@href="{link}"]', timeout=3000)
        self.page.click(f'xpath=//a[@href="{link}"]')
        self.page.wait_for_selector(f':not([href="{link}"])')

    def is_element_present(self, selector: str):
        return self.page.query_selector(selector)

    def switch(self, handle_number: int):
        handles = self.page.context.pages
        self.page = handles[handle_number]

    def close_handle(self, handle_num: int):
        self.switch(handle_num)
        self.page.close()

    def clear_input(self, selector: str):
        input_field = self.page.query_selector(selector)
        input_field.fill('')
        self.page.keyboard.press('Tab')

    def browser_close(self):
        self.page.close()

    def save_image(self, selector: str):
        image = self.page.query_selector(selector)
        image.screenshot(path='features/images/screenshot.png')
