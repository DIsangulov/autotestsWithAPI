import time
import urllib

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# from resources.locators import MainLocators
from sys import platform

from seleniumwire import webdriver

from resourses.locators import MainLocators


class BasePage:
    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        # if platform == "darwin":
        #     self.cmd_or_ctrl = Keys.COMMAND
        # else:
        #     self.cmd_or_ctrl = Keys.CONTROL

    def open(self):  # открывает страницу по url который мы задали
        self.browser.get(self.url)
        # self.browser.find_element(*SecurLocators.DOP_BUT).click()
        # self.browser.find_element(*SecurLocators.GO_BUT).click()

    def open_new_tab(self, link):  # открытие новой вклдадки
        self.browser.switch_to.new_window('tab')
        self.browser.get(link)

    def is_element_present(self, how, what):  # дефолтная проверка что элемент есть на странице
        # self.browser.find_element(how, what)
        return self.browser.find_element(how, what)

    def go_to_page(self, how, what):  # переход на новую вкладку
        self.wait_until_elem_be_clickable(how, what)
        link = self.browser.find_element(how, what)
        link.click()
        time.sleep(0.7)  # time for animation

    def scroll_down(self):  # скролл вниз до конца
        self.browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

    def switch(self, handle_number):  # переключение между вкладками
        handles = self.browser.window_handles
        self.browser.switch_to.window(handles[handle_number])
        time.sleep(1)

    def exit(self):  # log out
        self.wait_until_elem_be_clickable(*MainLocators.EXIT_BUT)
        self.browser.find_element(*MainLocators.EXIT_BUT).click()

    def wait_until(self, how, what):  # бесконечное ожидание события
        flag = True
        while flag:
            if self.is_element_present(how, what):
                flag = False
            else:
                time.sleep(0.5)  # time for waiting

    def close_handle(self, handle_num):  # закрыть вкладку
        self.switch(handle_num)
        self.browser.close()

    def find_request_in_network(self, part_of_request,
                                expected_status_code):  # искать запрос в network и проверять его статускод
        flag = False
        for request in self.browser.requests:
            if request.response:
                if request.url.find(part_of_request) != -1 and request.response.status_code == expected_status_code:
                    flag = True
        return flag

    def clear_input(self, how, what):  # clean field
        time.sleep(0.2)  # time for stable work
        self.browser.find_element(how, what).send_keys(self.cmd_or_ctrl + "a" + Keys.DELETE)
        time.sleep(0.2)  # time for stable work

    # TODO: it's work unstable... we must try to ise stupid servers:)

    def wait_until_elem_be_clickable(self, how, what):  # expends to send_keys method with inputs too
        wait = WebDriverWait(self.browser, 30)
        wait.until(EC.element_to_be_clickable((how, what)))
        # wait.until(EC.visibility_of_element_located((how, what)))
        time.sleep(0.2)

    def browser_close(self):
        self.browser.close()

    def save_image(self, how, what):
        image = self.browser.find_element(how, what)
        image.screenshot('features/images/screenshot.png')
