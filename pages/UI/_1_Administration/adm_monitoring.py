import time

from pages.Helpers.base_page import BasePage
from resourses.locators import AdminLocators


class Monitoring(BasePage):
    def open_adm_monitoring(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.page.click(AdminLocators.MONITORING)

    def should_enter_adm_monitoring_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_OLD)
        assert "Общее состояние системы" in self.is_element_present(AdminLocators.TITLE_MSG_OLD).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.host + "/system-state/system-state/webserver", "URL's do not match"
