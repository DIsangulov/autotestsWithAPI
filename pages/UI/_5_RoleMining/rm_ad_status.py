import time
from selenium.webdriver import Keys
import pytest
from selenium.webdriver.common.by import By

from pages.Helpers.base_page import BasePage
from resourses.locators import RoleMiningLocators, MainLocators, AdminLocators


class AdStatus(BasePage):

    def open_rm_ad_status_statistic(self):
        self.browser.find_element(*RoleMiningLocators.ADSTATUS).click()
        time.sleep(1)

    def should_enter_rm_ad_status_statistic_be_successful(self):
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Состояние Active Directory", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/role-mining/state-ad/statistics", \
            "URL не совпадают"

    def open_rm_ad_status_recommendation(self):
        self.browser.find_element(*RoleMiningLocators.RECOMMENDATION).click()
        time.sleep(1)

    def should_enter_rm_ad_status_recommendation_be_successful(self):
        assert self.is_element_present(*AdminLocators.TITLE_MSG_NEW).text == "Состояние Active Directory", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/role-mining/state-ad/recommendations", \
            "URL не совпадают"
