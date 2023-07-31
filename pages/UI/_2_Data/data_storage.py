import time

from pages.Helpers.base_page import BasePage
from resourses.locators import DataLocators, AdminLocators


class Storage(BasePage):
    def open_data_storage_structure(self):
        self.page.click(DataLocators.STORAGE)
        self.page.click(DataLocators.STRUCTURE)

    def should_enter_data_storage_structure_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Хранилище" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.host + "/storage/structure", "URL's do not match"

    def open_data_storage_statistics(self):
        self.page.click(DataLocators.STATISTICS)

    def should_enter_data_storage_statistics_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Хранилище" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.host + "/storage/statistic", "URL's do not match"

    def open_data_storage_search_content(self):
        self.page.click(DataLocators.STORAGE_SEARCH)
        self.page.click(DataLocators.STORAGE_SEARCH_CONTENT)

    def should_enter_data_storage_search_content_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Хранилище" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.host + "/storage/search/content", "URL's do not match"

    def open_data_storage_search_column(self):
        self.page.click(DataLocators.STORAGE_SEARCH)
        self.page.click(DataLocators.STORAGE_SEARCH_COLUMN)

    def should_enter_data_storage_search_column_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Хранилище" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.host + "/storage/search/column", "URL's do not match"

    def open_data_storage_import_rules(self):
        self.page.click(DataLocators.IMPORT_RULES)

    def should_enter_data_storage_import_rules_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Хранилище" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.host + "/storage/rules", "URL's do not match"
