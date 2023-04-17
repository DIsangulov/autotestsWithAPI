import time

from pages.Helpers.base_page import BasePage
from resourses.locators import AnalyticsLocators, MainLocators, AdminLocators


class Visualisation(BasePage):
    def open_an_visualisation(self):
        self.page.click(AnalyticsLocators.VISUALIZATIONS)

    def should_enter_an_visualisation_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_OLD)
        assert "Визуализации" in self.is_element_present(AdminLocators.TITLE_MSG_OLD).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/visualisations", "URL's do not match"
