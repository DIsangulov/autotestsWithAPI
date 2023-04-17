import time

from pages.Helpers.base_page import BasePage
from resourses.locators import AdminLocators


class Settings(BasePage):
    def open_adm_settings_admin_node(self):
        self.page.click(AdminLocators.SETTINGS)
        self.page.click(AdminLocators.ADMIN_NODE)

    def should_enter_adm_settings_admin_node_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Настройки" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/settings/common", "URL's do not match"

    def open_adm_settings_domain_controller(self):
        self.page.click(AdminLocators.DOMAIN_CONTROLLER)

    def should_enter_adm_settings_domain_controller_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Настройки" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/settings/domain", "URL's do not match"

    def open_adm_settings_service_db(self):
        self.page.click(AdminLocators.SERVICE_DB)

    def should_enter_adm_settings_service_db_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Настройки" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/settings/cluster", "URL's do not match"

    def open_adm_settings_storage(self):
        self.page.click(AdminLocators.STORAGE)

    def should_enter_adm_settings_storage_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Настройки" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/settings/storage", "URL's do not match"

    def open_adm_settings_data_collection(self):
        self.page.click(AdminLocators.DATA_COLLECTION)

    def should_enter_adm_settings_data_collection_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Настройки" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/settings/collector", "URL's do not match"

    def open_adm_settings_data_analysis(self):
        self.page.click(AdminLocators.DATA_ANALYSIS)

    def should_enter_adm_settings_data_analysis_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Настройки" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/settings/ml", "URL's do not match"

    def open_adm_settings_post(self):
        self.page.click(AdminLocators.POST)

    def should_enter_adm_settings_post_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Настройки" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/settings/ms", "URL's do not match"

    def open_adm_settings_syslog(self):
        self.page.click(AdminLocators.SYSLOG)

    def should_enter_adm_settings_syslog_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Настройки" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/settings/sys", "URL's do not match"

    def open_adm_settings_secrets(self):
        self.page.click(AdminLocators.SECRETS)

    def should_enter_adm_settings_secrets_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Настройки" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/settings/secrets", "URL's do not match"
