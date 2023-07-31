from selenium.webdriver.common.by import By

from pages.Helpers.base_page import BasePage
from resourses.locators import MainLocators, XbaLocators, AdminLocators


class Metaprofiles(BasePage):
    def open_xba_metaprofiles(self):
        self.page.click(XbaLocators.METAPROFILES)

    def should_enter_xba_metaprofiles_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Метапрофили" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.host + "/metaprofiles", "URL's do not match"
