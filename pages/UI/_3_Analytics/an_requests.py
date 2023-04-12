import time

from pages.Helpers.base_page import BasePage
from resourses.locators import AnalyticsLocators, MainLocators, AdminLocators


class Requests(BasePage):
    def open_an_requests(self):
        self.browser.find_element(*AnalyticsLocators.REQUESTS).click()
        # self.wait_for_page_load(*AdminLocators.TITLE_MSG_OLD)
        time.sleep(1)

    def should_enter_an_requests_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_OLD)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_OLD).text == "Запросы", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/query-list", \
            "URL не совпадают"
