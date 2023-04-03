from pages.Helpers.base_page import BasePage
from resourses.locators import MainLocators, AdminLocators


class Sessions(BasePage):
    def open_adm_sessions(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*AdminLocators.SESSIONS).click()

    def should_enter_adm_sessions_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Сессии", \
            "Найдено несовпадение ожидаемого результата с фактическим"
