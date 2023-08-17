from playwright.sync_api import Page


class Navigation:
    def __init__(self, page: Page):
        self.page = page

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

        self.BACK_BUTTON = page.locator("//div[@class='back-button__icon']")

        self.TOOLBAR_REFRESH = self.page.locator("//div[contains(@class, 'main-toolbar__buttons')]/button[div[contains(text(), 'Обновить')]]")
        self.TOOLBAR_SAVE_PDF = self.page.locator("//div[contains(@class, 'main-toolbar__buttons')]/button[div[contains(text(), 'Скачать PDF')]]")

        self.TOOLBAR_PIN_BUTTON = self.page.locator("//div[contains(@class, 'main-toolbar__buttons')]/div/div[div[contains(text(), 'Закрепить на Главной')]]")
        # todo: Закрепить на главной дропдавн 2 кнопки
        # todo: Закрепить на главной модалка
