import time

from pages.Helpers.base_page import BasePage
from resourses.locators import AdminLocators


class Settings(BasePage):
    def open_adm_settings_admin_node(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*AdminLocators.SETTINGS).click()
        self.browser.find_element(*AdminLocators.ADMIN_NODE).click()
        time.sleep(1)

    def should_enter_adm_settings_admin_node_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Настройки", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/settings/common", \
            "URL не совпадают"

    def open_adm_settings_domain_controller(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*AdminLocators.DOMAIN_CONTROLLER).click()
        time.sleep(1)

    def should_enter_adm_settings_domain_controller_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Настройки", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/settings/domain", \
            "URL не совпадают"

    def open_adm_settings_service_db(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*AdminLocators.SERVICE_DB).click()
        time.sleep(1)

    def should_enter_adm_settings_service_db_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Настройки", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/settings/cluster", \
            "URL не совпадают"

    def open_adm_settings_storage(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*AdminLocators.STORAGE).click()
        time.sleep(1)

    def should_enter_adm_settings_storage_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Настройки", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/settings/storage", \
            "URL не совпадают"

    def open_adm_settings_data_collection(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*AdminLocators.DATA_COLLECTION).click()
        time.sleep(1)

    def should_enter_adm_settings_data_collection_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Настройки", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/settings/collector", \
            "URL не совпадают"

    def open_adm_settings_data_analysis(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*AdminLocators.DATA_ANALYSIS).click()
        time.sleep(1)

    def should_enter_adm_settings_data_analysis_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Настройки", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/settings/ml", \
            "URL не совпадают"

    def open_adm_settings_post(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*AdminLocators.POST).click()
        time.sleep(1)

    def should_enter_adm_settings_post_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Настройки", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/settings/ms", \
            "URL не совпадают"

    def open_adm_settings_syslog(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*AdminLocators.SYSLOG).click()
        time.sleep(1)

    def should_enter_adm_settings_syslog_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Настройки", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/settings/sys", \
            "URL не совпадают"

    def open_adm_settings_secrets(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*AdminLocators.SECRETS).click()
        time.sleep(1)

    def should_enter_adm_settings_secrets_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_NEW)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Настройки", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/settings/secrets", \
            "URL не совпадают"
