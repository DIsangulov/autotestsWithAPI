from playwright.sync_api import Page
from pages.Helpers.base_page import BasePage
from resourses.locators import DataLocators, AdminLocators


class StoragePage(BasePage):

    page_path = "/storage"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path
