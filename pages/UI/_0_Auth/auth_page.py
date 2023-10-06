from playwright.sync_api import Page

from pages.Helpers.base_page import BasePage


class AuthPage(BasePage):

    page_path = "/auth"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = AuthPage.page_path

        self.LOGIN_INPUT = page.locator("//input[@type='email']")
        self.PASSWORD_INPUT = page.locator("//input[@id='password']")
        self.PASSWORD_VISIBLE = page.locator("//span[@class='icon is-right has-text-primary is-clickable']")

        self.CHECKBOX_LOCAL = page.locator("//input[@type='checkbox']/..")
        self.ENTER_BUTTON = page.locator("//button[span[contains(text(), 'Войти')]]")

        self.WRONG_LOGPASS_ALERT = page.locator("//div[@role='alert'][contains(text(), 'Неверный логин или пароль')]")

        # self.REGISTER_LINK = page.locator()
