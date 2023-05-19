from selenium.webdriver.common.by import By

from pages.Helpers.base_page import BasePage
from resourses.locators import MainLocators, XbaLocators, AdminLocators


class Profiles(BasePage):
    def open_xba_profiles(self):
        self.page.click(XbaLocators.XBA)
        self.page.click(XbaLocators.PROFILES)

    def should_enter_xba_profiles_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Профили хВА" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/profiles", "URL's do not match"
