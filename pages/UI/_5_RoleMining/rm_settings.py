from selenium.webdriver.common.by import By


from pages.Helpers.base_page import BasePage
from resourses.locators import RoleMiningLocators, MainLocators


class RmSettings(BasePage):
    def open_rm_settings(self):
        self.browser.find_element(*MainLocators.SIDE_BAR).click()
        self.wait_until_elem_be_clickable(*RoleMiningLocators.ROLE_MINING)
        self.browser.find_element(*RoleMiningLocators.ROLE_MINING).click()
        self.browser.find_element(*RoleMiningLocators.SETTINGS).click()

    def should_enter_rm_settings_be_successful(self):
        assert (self.browser.find_element(By.XPATH, "//*[contains(text(),'Настройки Role mining')]")), \
            "Найдено несовпадение ожидаемого результата с фактическим"

    def clear_sources_rm_settings(self):
        self.browser.find_element(*RoleMiningLocators.CLEAR_BUTTON).click()

    def not_confirm_cleaning_rm_settings(self):
        self.wait_until_elem_be_clickable(*RoleMiningLocators.CLEAR_BUTTON_NO)
        self.browser.find_element(*RoleMiningLocators.CLEAR_BUTTON_NO).click()

    def confirm_cleaning_rm_settings(self):
        self.wait_until_elem_be_clickable(*RoleMiningLocators.CLEAR_BUTTON_YES)
        self.browser.find_element(*RoleMiningLocators.CLEAR_BUTTON_YES).click()

    def selecting_values_from_dropdown_list(self):
        self.browser.find_element(*RoleMiningLocators.SELECT_DB).click()
        self.browser.find_element(*RoleMiningLocators.SELECT_DB_CHOISE).click()
        self.browser.find_element(*RoleMiningLocators.SELECT_TABLE).click()
        self.browser.find_element(*RoleMiningLocators.SELECT_DB_CHOISE).click()
        self.browser.find_element(*RoleMiningLocators.SELECT_TABLE).click()
        self.browser.find_element(*RoleMiningLocators.SELECT_DB_CHOISE).click()
        self.browser.find_element(*RoleMiningLocators.SAVE_BUTTON).click()

    def should_sources_saved(self):
        self.browser.find_element(*RoleMiningLocators.SAVE_BUTTON).click()
        assert (self.browser.find_element(By.XPATH, "//*[contains(text(),'Источники сохранены')]")), \
            "Найдено несовпадение ожидаемого результата с фактическим"

    def should_sources_recalculated(self):
        self.browser.find_element(*RoleMiningLocators.SAVE_DROPDOWN_BUTTON).click()
        self.browser.find_element(*RoleMiningLocators.RECALCULATE_BUTTON).click()
        self.browser.find_element(*RoleMiningLocators.RERUN_BUTTON).click()
        assert (self.browser.find_element(By.XPATH, "//*[contains(text(),'Расчёт запущен')]")), \
            "Найдено несовпадение ожидаемого результата с фактическим"

    def calculation_settings(self):
        self.browser.find_element(*RoleMiningLocators.CALCULATION_SETTINGS).click()

    def configuring_anomaly_distribution(self):
        self.browser.find_element(*RoleMiningLocators.GEAR_BUTTON).click()

    def input_server_address_and_port(self):
        self.browser.find_element(*RoleMiningLocators.SERVER_ADDERESS).send_keys('100.123.0.11')
        self.browser.find_element(*RoleMiningLocators.PORT).send_keys('333')

    def select_tcp_exchange_protocol(self):
        self.browser.find_element(*RoleMiningLocators.DROPDOWN_EXCHANGE_PROTOCOL).click()
        self.browser.find_element(*MainLocators.DROPDOWN1).click()

    def select_udp_exchange_protocol(self):
        self.browser.find_element(*RoleMiningLocators.DROPDOWN_EXCHANGE_PROTOCOL).click()
        self.browser.find_element(*MainLocators.DROPDOWN1).click()

    def click_add_button(self):
        self.browser.find_element(*RoleMiningLocators.ADD_BUTTON).click()

    def should_tcp_distribution_protocol_save_sucsess(self):
        assert (self.browser.find_element(By.XPATH, "//*[contains(text(),'100.123.0.11;333;TCP')]")), \
            "Найдено несовпадение ожидаемого результата с фактическим"

    def should_udp_distribution_protocol_save_sucsess(self):
        assert (self.browser.find_element(By.XPATH, "//*[contains(text(),'100.123.0.11;333;UDP')]")), \
            "Найдено несовпадение ожидаемого результата с фактическим"

    def enter_email(self):
        self.browser.find_element(*RoleMiningLocators.CHECKBOX_SYSLOG).click()
        self.browser.find_element(*RoleMiningLocators.CHECKBOX_EMAIL).click()
        self.browser.find_element(*RoleMiningLocators.INPUT_EMAIL).send_keys('dataplan_qaa@ngrsoftlab.ru')

    def should_email_save_sucsess(self):
        assert (self.browser.find_element(By.XPATH, "//*[contains(text(),'dataplan_qaa@ngrsoftlab.ru')]")), \
            "Найдено несовпадение ожидаемого результата с фактическим"

    def delete_last_entry(self):
        self.browser.find_element(*RoleMiningLocators.TRASH_ICON).click()
        self.browser.find_element(*RoleMiningLocators.DELETE_BUTTON).click()

    def should_last_entry_deleted(self):
        assert (self.browser.find_element(By.XPATH, "//*[contains(text(),'Настройка рассылки успешно удалена')]")), \
            "Найдено несовпадение ожидаемого результата с фактическим"
