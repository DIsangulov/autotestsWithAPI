from playwright.sync_api import Page

from pages.Helpers.base_page import BasePage
from resourses.locators import AdminLocators


class Roles(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = "/roles"

    def open_adm_roles(self):
        self.page.click(AdminLocators.ADMINISTRATION)
        self.page.click(AdminLocators.ROLES)

    def should_enter_adm_roles_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_OLD)
        assert "Роли" in self.is_element_present(AdminLocators.TITLE_MSG_OLD).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.host + "/roles", "URL's do not match"
