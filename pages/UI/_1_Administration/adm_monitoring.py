import time

from pages.Helpers.base_page import BasePage
from resourses.locators import AdminLocators


class Monitoring(BasePage):
    def open_adm_monitoring(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*AdminLocators.MONITORING).click()
        time.sleep(1)

    def should_enter_adm_monitoring_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_OLD)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_OLD).text == "Общее состояние системы", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/system-state/system-state/webserver", \
            "URL не совпадают"
