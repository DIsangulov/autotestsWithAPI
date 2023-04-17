from PIL import Image, ImageChops
from selenium.webdriver.common.by import By

from pages.Helpers.base_page import BasePage
from resourses.locators import MainLocators, XbaLocators, AdminLocators


class Statistic(BasePage):
    def open_xba_statistic(self):
        self.page.click(XbaLocators.XBA_STATISTIC)

    def should_enter_xba_statistic_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Статистика xBA" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/xBA-statistics/profiles", "URL's do not match"

    # def save_xba_diagram_image(self):
    #     self.save_image(*XbaLocators.PUK)
    #
    # @staticmethod
    # def compare_images():
    #     img1 = Image.open("test-datas/images/screenshot.png")
    #     img2 = Image.open('test-datas/images/img_for_compare/screenshot1.png')
    #     result = ImageChops.difference(img1, img2)
    #     assert result is None, f"{img1} and {img2} do not match"
    #     # print(f"{img1} and {img2} match")
