import time

from pages.Helpers.base_page import BasePage
from resourses.locators import DataLocators, AdminLocators


class Storage(BasePage):
    def open_data_storage_structure(self):
        self.browser.find_element(*DataLocators.STORAGE).click()
        self.browser.find_element(*DataLocators.STRUCTURE).click()

    def should_enter_data_storage_structure_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Хранилище", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/storage/structure", \
            "URL не совпадают"

    def open_data_storage_statistics(self):
        self.browser.find_element(*DataLocators.STATISTICS).click()
        time.sleep(1)

    def should_enter_data_storage_statistics_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Хранилище", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/storage/statistic", \
            "URL не совпадают"

    def open_data_storage_search_content(self):
        self.browser.find_element(*DataLocators.STORAGE_SEARCH).click()
        self.browser.find_element(*DataLocators.STORAGE_SEARCH_CONTENT).click()
        time.sleep(1)

    def should_enter_data_storage_search_content_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Хранилище", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/storage/search/content", \
            "URL не совпадают"

    def open_data_storage_search_column(self):
        self.browser.find_element(*DataLocators.STORAGE_SEARCH).click()
        self.browser.find_element(*DataLocators.STORAGE_SEARCH_COLUMN).click()
        time.sleep(1)

    def should_enter_data_storage_search_column_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Хранилище", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/storage/search/column", \
            "URL не совпадают"

    def open_data_storage_import_rules(self):
        self.browser.find_element(*DataLocators.IMPORT_RULES).click()
        time.sleep(1)

    def should_enter_data_storage_import_rules_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Хранилище", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/storage/rules", \
            "URL не совпадают"
