from pages.Helpers.base_page import BasePage
from resourses.locators import AnalyticsLocators, MainLocators, AdminLocators


class Reports(BasePage):
    def open_an_reports(self):
        self.browser.find_element(*AnalyticsLocators.REPORTS).click()

    def should_enter_an_reports_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_OLD)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_OLD).text == "Отчеты", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/report", \
            "URL не совпадают"
