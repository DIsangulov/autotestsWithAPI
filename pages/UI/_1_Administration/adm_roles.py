from pages.Helpers.base_page import BasePage
from resourses.locators import MainLocators, AdminLocators


class Roles(BasePage):
    def open_adm_roles(self):
        self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*AdminLocators.ROLES).click()

    def should_enter_adm_roles_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_OLD)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_OLD).text == "Роли", \
            "Найдено несовпадение ожидаемого результата с фактическим"
