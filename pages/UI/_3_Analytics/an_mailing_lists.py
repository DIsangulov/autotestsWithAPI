import time

from selenium.webdriver.common.by import By

from pages.Helpers.base_page import BasePage
from resourses.locators import AnalyticsLocators, MainLocators, AdminLocators


class MailingLists(BasePage):
    def open_an_mailing_lists_reports(self):
        self.browser.find_element(*AnalyticsLocators.ANALYTICS).click()
        self.browser.find_element(*AnalyticsLocators.MAILING_LISTS).click()
        self.browser.find_element(*AnalyticsLocators.MAILING_LISTS_REPORTS).click()

    def open_an_mailing_lists_new_data(self):
        self.browser.find_element(*AnalyticsLocators.MAILING_LISTS_NEW_DATA).click()

    def should_enter_an_mailing_lists_reports_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Рассылки", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        # assert self.browser.current_url == self.url + "/mailings/report?reportTitle=Рассылка%20%28имя%20отчета%29&type=0", \
        #     "URL не совпадают"
