# TODO: переместить >> pages/Helpers/n_navigation
class AuthLocators:
    LOGIN_INPUT = "//input[@type='email']"
    PASSWORD_INPUT = "//input[@id='password']"
    CHECKBOX_LOCAL = "//input[@type='checkbox']/.."
    ENTER_BUTTON = "//button[span[contains(text(), 'Войти')]]"
    PASS_VISIBLE = "//span[@class='icon is-right has-text-primary is-clickable']"
    WRONG_LOG_PASS_ALERT = "//div[@role='alert'][contains(text(), 'Неверный логин или пароль')]"


class MainLocators:
    HEADER_LOGO = "//div[@class='n-app-navigation__header']"
