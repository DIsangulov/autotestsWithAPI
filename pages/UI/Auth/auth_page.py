from playwright.sync_api import Page

from pages.Helpers.base_page import BasePage


class AuthPage(BasePage):
    page_path = "/auth"

    def __init__(self, page: Page):
        self.registration = AuthPageRegistrationModalCard(page)

        super().__init__(page, auto_auth=False)
        self.page_path = AuthPage.page_path

        self.LOGIN_INPUT = self.AUTH_LOGIN_INPUT
        self.PASSWORD_INPUT = self.AUTH_PASSWORD_INPUT
        self.PASSWORD_VISIBLE = page.locator("//span[@class='icon is-right has-text-primary is-clickable']")

        self.CHECKBOX_LOCAL = self.AUTH_CHECKBOX_LOCAL
        self.ENTER_BUTTON = self.AUTH_ENTER_BUTTON

        self.WRONG_LOGPASS_ALERT = page.locator("//div[@role='alert'][contains(text(), 'Неверный логин или пароль')]")

        self.REGISTER_LINK = page.locator("//a[@class='router-link' and contains(text, Регистрация)]")


class AuthPageRegistrationModalCard(BasePage):

    def __init__(self, page: Page):
        super().__init__(page, auto_auth=False)

        self.MODAL_CARD = page.locator("//div[@class='modal is-active']")

        self.INPUT_RUSNAME = page.locator("//div[@class='modal is-active']//input[contains(@placeholder, 'Имя и фамилия')]")
        self.INPUT_USERNAME = page.locator("//div[@class='modal is-active']//input[contains(@placeholder, 'Логин')]")
        self.INPUT_PASSWORD = page.locator("//div[@class='modal is-active']//input[contains(@placeholder, 'Пароль')]")
        self.INPUT_PASSWORD_IS_VISIBLE = page.locator("//div[@class='modal is-active']//input[contains(@placeholder, 'Пароль')]/../span")
        self.INPUT_EMAIL = page.locator("//div[@class='modal is-active']//div[label[text()='Почта *']]/div/input")
        self.INPUT_MOBILE = page.locator("//div[@class='modal is-active']//div[label[text()='Телефон *']]/div/input")
        self.INPUT_DEPARTMENT = page.locator("//div[@class='modal is-active']//input[contains(@placeholder, 'Отдел')]")
        self.INPUT_TITLE = page.locator("//div[@class='modal is-active']//input[contains(@placeholder, 'Должность')]")

        self.BUTTON_REGISTRATION = page.locator("//div[@class='modal is-active']//button[span[text()='Зарегистрировать']]")
        self.BUTTON_CLOSE = page.locator("//div[@class='modal is-active']//button[span[text()='Закрыть']]")

    def open(self):
        assert False, f"Method not allowed for {self.__class__} class"
