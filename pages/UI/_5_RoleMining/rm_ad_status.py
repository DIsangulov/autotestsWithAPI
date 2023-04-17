import time
from selenium.webdriver import Keys
import pytest
from selenium.webdriver.common.by import By

from pages.Helpers.base_page import BasePage
from resourses.locators import RoleMiningLocators, MainLocators, AdminLocators


class AdStatus(BasePage):

    def open_rm_ad_status_statistic(self):
        self.page.click(RoleMiningLocators.ROLE_MINING)
        self.page.click(RoleMiningLocators.ADSTATUS)

    def should_enter_rm_ad_status_statistic_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Состояние Active Directory" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/role-mining/state-ad/statistics", "URL's do not match"

    def open_rm_ad_status_recommendation(self):
        self.page.click(RoleMiningLocators.RECOMMENDATION)

    def should_enter_rm_ad_status_recommendation_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Состояние Active Directory" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/role-mining/state-ad/recommendations", "URL's do not match"
