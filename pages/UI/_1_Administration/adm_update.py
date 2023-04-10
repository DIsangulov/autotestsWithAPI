import time

from pages.Helpers.base_page import BasePage
from resourses.locators import AdminLocators


class Update(BasePage):
    def open_adm_update(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*AdminLocators.UPDATE).click()
        time.sleep(1)

    def should_enter_adm_update_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Состояние обновления системы", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/system-update", \
            "URL не совпадают"
