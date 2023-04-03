from PIL import Image, ImageChops
from selenium.webdriver.common.by import By

from pages.Helpers.base_page import BasePage
from resourses.locators import MainLocators, XbaLocators


class Statistic(BasePage):
    def open_xba_statistic(self):
        self.wait_until_elem_be_clickable(*XbaLocators.XBA)
        self.browser.find_element(*XbaLocators.XBA).click()
        self.browser.find_element(*XbaLocators.XBA_STATISTIC).click()

    def should_enter_xba_statistic_be_successful(self):
        assert (self.browser.find_element(By.XPATH, "//*[contains(text(),'Статистика xBA')]")), \
            "Найдено несовпадение ожидаемого результата с фактическим"

    def save_xba_diagram_image(self):
        self.save_image(*XbaLocators.PUK)

    @staticmethod
    def compare_images():
        img1 = Image.open("test-datas/images/screenshot.png")
        img2 = Image.open('test-datas/images/img_for_compare/screenshot1.png')
        result = ImageChops.difference(img1, img2)
        assert result is None, f"{img1} and {img2} do not match"
        # print(f"{img1} and {img2} match")
