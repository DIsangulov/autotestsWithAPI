from playwright.sync_api import Page
from pages.Helpers.base_page import BasePage
from resourses.locators import AnalyticsLocators, AdminLocators


class MailingsPage(BasePage):

    page_path = "/mailings/report"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        self.TAB_REPORTS = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Отчетов')]")
        self.TAB_NEW_DATA = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Новых данных')]")

        # todo: Кнопка "Создать рассылку


class MailingsReportPage(MailingsPage):

    page_path = "/mailings/report"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo:


class MailingNewData(MailingsPage):

    page_path = "/mailings/new"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo:


# fixme: зависимости
class MailingLists(BasePage):
    def open_an_mailing_lists_reports(self):
        self.page.click(AnalyticsLocators.ANALYTICS)
        self.page.click(AnalyticsLocators.MAILING_LISTS)
        self.page.click(AnalyticsLocators.MAILING_LISTS_REPORTS)
