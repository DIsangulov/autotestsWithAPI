import time

from pages.Helpers.base_page import BasePage
from resourses.locators import AdminLocators


class Users(BasePage):
    def open_adm_users(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*AdminLocators.USERS).click()
        time.sleep(1)

    def should_enter_adm_users_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_OLD)
        assert self.browser.current_url == self.url + "/users", \
            "URL не совпадают"
