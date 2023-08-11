from playwright.sync_api import Page
from pages.Helpers.base_page import BasePage


# abc -> ConnectorsPage & LogoPage
class LibraryPage(BasePage):

    page_path = "/library"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        self.TAB_CONNECTORS = page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Коннекторы')]")
        self.TAB_LOGOS = page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Логотипы')]")


class ConnectorsPage(LibraryPage):

    page_path = "/library/connectors"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo: toolbar импортировать из файла
        # todo: МО загрузить файл

        self.CREATE_CONNECTOR_BUTTON = page.locator("//div[button//text()='Создать коннектор']")

        # todo: Поля поиска

        # todo: действия


class ConnectorsCreatePage(BasePage):

    page_path = "/library/connectors/create"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo:


class LogoPage(LibraryPage):

    page_path = "/library/logo"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        self.CREATE_LOGO_BUTTON = page.locator("//div[button//text()='Создать логотип']")

        self.MODAL_WINDOW = page.locator("//div[@class='ngr-modal upload-modal']")
        # todo: MO Создать новый логотип
        self.MW_CLOSE = self.MODAL_WINDOW.locator("//div[contains(@class, 'ngr-modal__close')]")

        # todo: Поле поиска лого по названию

        # todo: действия
