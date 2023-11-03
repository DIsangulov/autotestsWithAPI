import allure
from playwright.sync_api import Page

from resourses.credentials import TestUsers, TARGET_URL


class DrivenPage:

    def __init__(self, page: Page):
        self.page = page

        self.host = TARGET_URL
        self.page_path = "/"

        self.HEADER_LOGO = self.page.locator("//div[@class='n-app-navigation__header']")

        self.AUTH_LOGIN_INPUT = page.locator("//input[@type='email']")
        self.AUTH_PASSWORD_INPUT = page.locator("//input[@id='password']")
        self.AUTH_CHECKBOX_LOCAL = page.locator("//input[@type='checkbox']/..")
        self.AUTH_ENTER_BUTTON = page.locator("//button[span[contains(text(), 'Войти')]]")

    def open(self):
        self.page.goto(self.host + self.page_path)
        self.page.wait_for_url(self.host + self.page_path)

    def goto_page(self, page_path: str):
        self.page.goto(self.host + page_path)


class MainNavigation(DrivenPage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.IS_LOADING = self.page.locator("//div[contains(@class, 'isLoading')]")

        self.PROFILE_BUTTON = self.page.locator("//button[@class='n-app-profile__ny n-app-button']")
        self.PB_USER_PROFILE = self.page.locator("//a[*[contains(text(),'Профиль пользователя')]]")
        self.PB_NOTIFICATION_SETTINGS = self.page.locator("//a[*[contains(text(),'Настройки уведомлений')]]")
        self.PB_SIGN_OUT = self.page.locator("//*[contains(text(),'Выйти')]")

        self.SIDE_BAR = self.page.locator("//div[@class='n-app-navigation__button']")

        self.SB_ADMINISTRATION = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Администрирование')]][1]")
        self.SB_ADM_ROLES = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Роли')]][1]")
        self.SB_ADM_USERS = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Пользователи')]][1]")
        self.SB_ADM_SESSIONS = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Сессии')]][1]")
        self.SB_ADM_MONITORING = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Мониторинг')]][1]")
        self.SB_ADM_LICENSE = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Лицензии')]][1]")
        self.SB_ADM_UPDATES = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Обновление')]][1]")
        self.SB_ADM_NOTIFICATION_LIST = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Журнал уведомлений')]][1]")
        self.SB_ADM_SETTINGS = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Настройки')]][1]")

        self.SB_DATA = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Данные')]][1]")
        self.SB_DATA_SOURCES = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Источники')]][1]")
        self.SB_DATA_SCRIPTS = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Скрипты')]][1]")
        self.SB_DATA_STORAGE = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Хранилище')]][1]")

        self.SB_ANALYTICS = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Аналитика')]][1]")
        self.SB_ANALYTICS_MAILINGS = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Рассылки')]][1]")
        self.SB_ANALYTICS_REPORTS = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Отчеты')]][1]")
        self.SB_ANALYTICS_VISUALISATIONS = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Визуализации')]][1]")
        self.SB_ANALYTICS_QUERIES = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Запросы')]][1]")

        self.SB_XBA = self.page.locator("//*[contains(@class, 'n-app-navigation__firstlvl') and ./../div/span[contains(text(), 'xBA')]]")
        self.SB_XBA_PROFILES = self.page.locator("//*[contains(@class, 'n-app-navigation__secondlvl') and ./../div/span[contains(text(), 'Профили')]]")
        self.SB_XBA_METAPROFILES = self.page.locator("//*[contains(@class, 'n-app-navigation__secondlvl') and ./../div/span[contains(text(), 'Метапрофили')]]")
        self.SB_XBA_STATISTICS = self.page.locator("//*[contains(@class, 'n-app-navigation__secondlvl') and ./../div/span[contains(text(), 'Статистика xBA')]]")

        self.SB_ROLE_MINING = self.page.locator("//*[contains(@class, 'n-app-navigation__firstlvl') and ./../div/span[contains(text(), 'Role mining')]]")
        self.SB_RM_SETTINGS = self.page.locator("//a[contains(@href, '/role-mining/settings')]")
        self.SB_RM_STATE_AD = self.page.locator("//a[contains(@href, '/role-mining/state-ad')]")
        self.SB_RM_GROUPS_AND_USERS = self.page.locator("//a[contains(@href, '/role-mining/groups-and-users') and .//span[contains(text(), 'Группы и пользователи')]]")
        self.SB_RM_ROLE_MODEL = self.page.locator("//a[contains(@href, '/role-mining/role-model') and .//span[contains(text(), 'Ролевая модель')]]")

        self.BACK_BUTTON = page.locator("//div[@class='back-button__icon']")

        self.TOOLBAR_REFRESH = self.page.locator("//div[contains(@class, 'main-toolbar__buttons')]/button[div[contains(text(), 'Обновить')]]")
        self.TOOLBAR_SAVE_PDF = self.page.locator("//div[contains(@class, 'main-toolbar__buttons')]/button[div[contains(text(), 'Скачать PDF')]]")

        self.TOOLBAR_PIN_BUTTON = self.page.locator("//div[contains(@class, 'main-toolbar__buttons')]/div/div[div[contains(text(), 'Закрепить на Главной')]]")
        # todo: Закрепить на главной дропдавн 2 кнопки # Закрепить на главной модалка


class BasePage(MainNavigation):

    def __init__(self, page: Page, *, auto_auth: bool = True):
        # TODO: --> luk at zis!! self.navigation = MainNavigation(page)
        super().__init__(page)
        if auto_auth:
            if not self.check_auth():
                self.auth()

    def check_auth(self) -> bool:
        if not self.HEADER_LOGO.is_visible(timeout=300):
            # print(f"check_auth:return FALSE")
            return False
        else:
            # print(f"check_auth:return TRUE")
            return True

    @allure.step("Авторизация")
    def auth(self, *, auth_data: dict = TestUsers.DpQaaLocal):

        auth_page_path = "/auth"

        with allure.step("Перейти на страницу Авторизации"):
            self.goto_page(auth_page_path)
            current_url = self.page.url
            assert current_url.startswith(self.host + auth_page_path), f"Страница авторизации не открылась"

        with allure.step("Ввести значение в поле 'Логин'"):
            self.AUTH_LOGIN_INPUT.fill(auth_data.get("username"))
        with allure.step("Ввести значение в поле 'Пароль'"):
            self.AUTH_PASSWORD_INPUT.fill(auth_data.get("password"))
        if auth_data.get("local"):
            with allure.step("Выбрать чекбокс 'локально'"):
                self.AUTH_CHECKBOX_LOCAL.click()

        with allure.step('Кликнуть по кнопке "Войти"'):
            self.AUTH_ENTER_BUTTON.click()
        with allure.step("Авторизация прошла"):
            self.HEADER_LOGO.wait_for(state="visible")

    @allure.step("Logout:")
    def logout(self):
        with allure.step("Кликнуть на выпадающее меню 'Пользователь'"):
            self.PROFILE_BUTTON.click()
        with allure.step("Кликнуть по кнопке 'Выйти'"):
            self.PB_SIGN_OUT.click()
