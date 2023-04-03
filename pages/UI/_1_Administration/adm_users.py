from pages.Helpers.base_page import BasePage
from resourses.locators import MainLocators, AdminLocators


class Users(BasePage):
    def open_adm_users(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*AdminLocators.USERS).click()

    def should_enter_adm_users_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_OLD)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_OLD).text == "Пользователи", \
            "Найдено несовпадение ожидаемого результата с фактическим"
