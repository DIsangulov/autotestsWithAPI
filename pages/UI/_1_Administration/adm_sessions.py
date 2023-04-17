import time

from pages.Helpers.base_page import BasePage
from resourses.locators import AdminLocators


class Sessions(BasePage):
    def open_adm_sessions(self):
        # self.page.click(AdminLocators.ADMINISTRATION)
        self.page.click(AdminLocators.SESSIONS)

    def should_enter_adm_sessions_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Сессии" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/sessions", "URL's do not match"
