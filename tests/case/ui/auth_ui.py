from pages.UI._0_Auth.auth_page import AuthPage

from resourses.credentials import TestUsers


class AuthCase:

    def __init__(self, browser, host):
        self.browser = browser
        self.host = host

    def valid_auth(self):
        page = AuthPage(self.browser, self.host)
        page.open()

        page.LOGIN_INPUT_1.fill(TestUsers.DpQaa.get("username"))
        page.PASSWORD_INPUT_1.fill(TestUsers.DpQaa.get("password"))
        page.PASSWORD_VISIBLE_1.click()
        page.ENTER_BUTTON.click()

        # page.enter_as_user()

        # todo: hint: поле обязательно для заполнения логин
        # todo: hint: поле обязательно для заполнения пароль
