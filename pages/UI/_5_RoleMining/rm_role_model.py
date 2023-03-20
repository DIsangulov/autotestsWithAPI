from selenium.webdriver.common.by import By

from pages.Helpers.base_page import BasePage
from resourses.locators import RoleMiningLocators, MainLocators


class RoleModel(BasePage):

    def open_rm_role_model(self):
        self.browser.find_element(*MainLocators.SIDE_BAR).click()
        # self.wait_until_elem_be_clickable(*RoleMiningLocators.ROLE_MINING)
        self.browser.find_element(*RoleMiningLocators.ROLE_MINING).click()
        self.browser.find_element(*RoleMiningLocators.ROLE_MODEL).click()

    def should_enter_rm_role_model_successful(self):
        assert (self.is_element_present(By.XPATH, "//*[contains(text(),'Ролевая модель')]")), \
            "Найдено несовпадение ожидаемого результата с фактическим"
