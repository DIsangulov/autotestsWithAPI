from pages.Helpers.base_page import BasePage
from resourses.locators import AdminLocators


class Update(BasePage):
    def open_adm_update(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.page.click(AdminLocators.UPDATE)

    def should_enter_adm_update_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Состояние обновления системы" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.host + "/system-update", "URL's do not match"
