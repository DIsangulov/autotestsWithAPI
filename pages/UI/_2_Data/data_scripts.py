from pages.Helpers.base_page import BasePage
from resourses.locators import DataLocators, AdminLocators


class Scripts(BasePage):
    def open_data_scripts(self):
        self.page.click(DataLocators.SCRIPTS)

    def should_enter_data_scripts_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_OLD)
        assert "Скрипты" in self.is_element_present(AdminLocators.TITLE_MSG_OLD).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.host + "/scripts", "URL's do not match"
