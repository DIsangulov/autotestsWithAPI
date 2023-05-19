import time

from pages.Helpers.base_page import BasePage
from resourses.locators import AdminLocators


class Licenses(BasePage):
    def open_adm_licenses(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.page.click(AdminLocators.LICENSES)
        time.sleep(1)

    def should_enter_adm_licenses_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Сведения о лицензии платформы" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/license", "URL's do not match"
