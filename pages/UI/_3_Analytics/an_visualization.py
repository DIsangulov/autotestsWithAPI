import time

from pages.Helpers.base_page import BasePage
from resourses.locators import AnalyticsLocators, MainLocators, AdminLocators


class Visualisation(BasePage):
    def open_an_visualisation(self):
        self.browser.find_element(*AnalyticsLocators.VISUALIZATIONS).click()
        time.sleep(1)

    def should_enter_an_visualisation_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_OLD)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_OLD).text == "Визуализации", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/visualisations", \
            "URL не совпадают"
