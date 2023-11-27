from playwright.sync_api import Page
from pages.Helpers.base_page import BasePage


class UpdatesPage(BasePage):

    page_path = "/administration/system-update/versions"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        self.TAB_VERSIONS = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Версии компонентов')]")
        self.TAB_ADDITIONS = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Дополнения')]")


class UpdatesVersionsPage(UpdatesPage):

    page_path = "/administration/system-update/versions"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo:


class UpdatesAdditionsPage(UpdatesPage):

    page_path = "/administration/system-update/additions"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo:
