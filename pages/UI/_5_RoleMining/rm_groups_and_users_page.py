from playwright.sync_api import Page
from pages.Helpers.base_page import BasePage


class RMGroupsAndUsersPage(BasePage):

    page_path = "/role-mining/groups-and-users"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # todo: добавить элементы взаимодействия
