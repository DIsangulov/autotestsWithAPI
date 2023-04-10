from pages.Helpers.base_page import BasePage
from resourses.locators import DataLocators, AdminLocators


class Scripts(BasePage):
    def open_data_scripts(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*DataLocators.SCRIPTS).click()

    def should_enter_data_scripts_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_OLD)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_OLD).text == "Скрипты", \
            "Найдено несовпадение ожидаемого результата с фактическим"
