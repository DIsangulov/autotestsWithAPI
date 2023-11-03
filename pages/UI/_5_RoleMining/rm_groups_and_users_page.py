from playwright.sync_api import Page
from pages.Helpers.base_page import BasePage


class RMGroupsAndUsersPage(BasePage):

    page_path = "/role-mining/groups-and-users"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        self.TAB_GROUPS = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Группы')]")
        self.TAB_USERS = self.page.locator("//ul[contains(@class, 'ngr-tabs-ul')]/li/div[contains(text(), 'Пользователи')]")


class RMGroupsPage(RMGroupsAndUsersPage):

    page_path = "/role-mining/groups-and-users/groups"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # self.SOMETHING = self.page.locator("//locator")


class RMUsersPage(RMGroupsAndUsersPage):

    page_path = "/role-mining/groups-and-users/users"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = self.__class__.page_path

        # self.SOMETHING = self.page.locator("//locator")
