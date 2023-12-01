from playwright.sync_api import Page
from pages.Helpers.base_page import BasePage


class MailingsPage(BasePage):

    page_path = "/mailings/mailings/report"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        self.TAB_REPORTS = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Отчетов')]")
        self.TAB_NEW_DATA = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Новых данных')]")

        # todo: Кнопка "Создать рассылку


class MailingsReportPage(MailingsPage):

    page_path = "/mailings/mailings/report"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo:


class MailingNewData(MailingsPage):

    page_path = "/mailings/mailings/new"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo:
