from playwright.sync_api import Page
from pages.Helpers.base_page import BasePage


class SourcesPage(BasePage):

    page_path = "/datasource"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = SourcesPage.page_path

        # todo: кнопка перейти в библиотеку шаблонов
        # todo: кнопка импорт драйвера
        # todo: модалка импорт драйвера
        # todo: импорт файла паттернов
        # todo: модалка импорт паттернов

        self.NEW_SOURCE_BUTTON = page.locator("//div[contains(@class, 'ngr-button-dropdown') and ./*/button//text()='Подключить источник']")
        self.NSB_FROM_CONNECTOR = page.locator("//div[contains(@class, 'ngr-button-dropdown__options') and ./div/div/text()='Из коннектора']")
        self.NSB_IN_EDITOR = page.locator("//div[contains(@class, 'ngr-button-dropdown__options') and ./div/div/text()='В редакторе']")

        # todo: локатор на поле ввода "Источник"
        # > тип подключения
        # > статус
        # > изменено

        # | Действие |
        self.ACTION_EDIT = page.locator("//tr[@class='ngr-table__item']/td[last()]//button[*[contains(text(), 'Редактировать')]]")
        self.ACTION_DELETE = page.locator("//tr[@class='ngr-table__item']/td[last()]//button[*[contains(text(), 'Удалить')]]")
        self.ACTION_DETAILS = page.locator("//tr[@class='ngr-table__item']/td[last()]//button[*[contains(text(), 'Детали')]]")

        # Детали > [Модальное окно]
        self.MODAL_WINDOW = page.locator("//div[@class='ngr-modal datasource-status-modal']")
        self.MW_TITLE = self.MODAL_WINDOW.locator("//div[@class='ngr-modal__title']")
        self.MW_ROW = self.MODAL_WINDOW.locator("//div[@class='datasource-status-modal__row']")
        self.MWR_IP_ADDRESS = self.MW_ROW.locator("//div[contains(text(), 'IP адрес')]")
        self.MWR_VERSION_SOFTWARE_SOURCE = self.MW_ROW.locator("//div[contains(text(), 'Версия ПО источника')]")
        self.MWR_TIME_GET_SOURCE = self.MW_ROW.locator("//div[contains(text(), 'Время последнего получения данных')]")
        self.MWR_EDITOR = self.MW_ROW.locator("//div[contains(text(), 'Редактор')]")
        self.MWR_INTERVAL = self.MW_ROW.locator("//div[contains(text(), 'Интервал обновления данных')]")

        self.MW_STATUS_DROPDOWN = self.MODAL_WINDOW.locator("//div[@class='datasource-status-modal__row datasource-status-modal__row_status']")
        self.MW_SD_ROW = self.MODAL_WINDOW.locator("//tr[@class='ngr-table__item']")

        self.MW_CLOSE = self.MODAL_WINDOW.locator("//div[contains(@class, 'ngr-modal__close')]")
