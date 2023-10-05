from playwright.sync_api import Page
from pages.Helpers.base_page import BasePage


class RMSettingsPage(BasePage):

    page_path = "/role-mining/settings"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        self.TAB_SOURCES = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Источники')]")
        self.TAB_CALC_SETTINGS = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Настройка расчета')]")


class RMSettingsSourcePage(RMSettingsPage):

    page_path = "/role-mining/settings/source"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # self.SOMETHING = self.page.locator("//locator")


class RMSettingsCalcPage(RMSettingsPage):

    page_path = "/role-mining/settings/calc"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # self.SOMETHING = self.page.locator("//locator")
