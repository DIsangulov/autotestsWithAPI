from playwright.sync_api import Page
from pages.Helpers.base_page import BasePage


class RMStateADPage(BasePage):

    page_path = "/role-mining/state-ad"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo: добавить элементы взаимодействия
