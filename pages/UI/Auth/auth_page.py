from playwright.sync_api import Page

from pages.Helpers.base_page import BasePage


class AuthPage(BasePage):
    page_path = "/auth"

    def __init__(self, page: Page):
        super().__init__(page, auto_auth=False)
        self.page_path = AuthPage.page_path

        self.LOGIN_INPUT = self.AUTH_LOGIN_INPUT
        self.PASSWORD_INPUT = self.AUTH_PASSWORD_INPUT
        self.PASSWORD_VISIBLE = page.locator("//span[@class='icon is-right has-text-primary is-clickable']")

        self.CHECKBOX_LOCAL = self.AUTH_CHECKBOX_LOCAL
        self.ENTER_BUTTON = self.AUTH_ENTER_BUTTON

        self.WRONG_LOGPASS_ALERT = page.locator("//div[@role='alert'][contains(text(), 'Неверный логин или пароль')]")

        # self.REGISTER_LINK = page.locator()
