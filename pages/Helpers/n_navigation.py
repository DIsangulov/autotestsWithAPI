from playwright.sync_api import Page


class Navigation:
    def __init__(self, page: Page):
        self.page = page

        # todo: выцепить селектор на лоадер

        self.PROFILE_BUTTON = self.page.locator("//button[@class='n-app-profile__ny n-app-button']")
        self.PB_USER_PROFILE = self.page.locator("//a[*[contains(text(),'Профиль пользователя')]]")
        self.PB_NOTIFICATION_SETTINGS = self.page.locator("//a[*[contains(text(),'Настройки уведомлений')]]")
        self.PB_SIGN_OUT = self.page.locator("//*[contains(text(),'Выйти')]")

        self.SIDE_BAR = self.page.locator("//div[@class='n-app-navigation__button']")

        self.SB_DATA = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Данные')]][1]")
        self.SB_DATA_SOURCES = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Источники')]][1]")
        self.SB_DATA_SCRIPTS = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Скрипты')]][1]")
        self.SD_DATA_STORAGE = self.page.locator("//*[@class='n-app-navigation__menu']//*[*[contains(text(), 'Хранилище')]][1]")

        # todo: toolbar>
        # todo: tb > reload
        # todo: tb > закрепить на главной
        # todo: tb > скачать PDF
        # todo: Закрепить на главной дропдавн 2 кнопки
        # todo: Закрепить на главной модалка
