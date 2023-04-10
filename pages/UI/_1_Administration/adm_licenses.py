import time

from pages.Helpers.base_page import BasePage
from resourses.locators import AdminLocators


class Licenses(BasePage):
    def open_adm_licenses(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*AdminLocators.LICENSES).click()
        time.sleep(1)

    def should_enter_adm_licenses_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Сведения о лицензии платформы", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/license", \
            "URL не совпадают"
