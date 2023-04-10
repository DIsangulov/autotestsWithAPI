from pages.Helpers.base_page import BasePage
from resourses.locators import DataLocators, AdminLocators


class Sources(BasePage):
    def open_data_sources(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*DataLocators.DATAS).click()
        self.browser.find_element(*DataLocators.SOURCES).click()

    def should_enter_data_sources_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Источники данных", \
            "Найдено несовпадение ожидаемого результата с фактическим"
