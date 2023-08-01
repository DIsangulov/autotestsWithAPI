from pages.Helpers.base_page import BasePage
from resourses.locators import DataLocators, AdminLocators


class Sources(BasePage):
    def open_data_sources(self):
        self.page.click(DataLocators.DATAS)
        self.page.click(DataLocators.SOURCES)

    def should_enter_data_sources_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Источники данных" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.host + "/datasource", "URL's do not match"
