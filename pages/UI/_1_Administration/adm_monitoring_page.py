from playwright.sync_api import Page
from pages.Helpers.base_page import BasePage


class MonitoringPage(BasePage):

    page_path = "/system-state/webserver"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo: