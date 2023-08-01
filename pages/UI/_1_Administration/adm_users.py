import time

from pages.Helpers.base_page import BasePage
from resourses.locators import AdminLocators


class Users(BasePage):
    def open_adm_users(self):
        # self.page.click(AdminLocators.ADMINISTRATION)
        self.page.click(AdminLocators.USERS)

    def should_enter_adm_users_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_OLD)
        assert "Пользователи" in self.is_element_present(AdminLocators.TITLE_MSG_OLD).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.host + "/users", "URL's do not match"
