import json

import requests

from pages.Helpers.base_page import BasePage
from resourses.locators import AdminLocators


class Roles(BasePage):
    def open_adm_roles(self):
        self.page.click(AdminLocators.ADMINISTRATION)
        self.page.click(AdminLocators.ROLES)

    def should_enter_adm_roles_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_OLD)
        assert "Роли" in self.is_element_present(AdminLocators.TITLE_MSG_OLD).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/roles", "URL's do not match"

    def try_to_ui_fonts_and_styles(self):
        unique_fonts = set()
        elements = self.page.query_selector_all('body *')
        for element in elements:
            font = element.evaluate_handle('''(el) => {
                const style = window.getComputedStyle(el);
                return {
                    family: style.getPropertyValue('font-family'),
                    size: style.getPropertyValue('font-size'),
                    weight: style.getPropertyValue('font-weight'),
                    style: style.getPropertyValue('font-style'),
                    color: style.getPropertyValue('color'),
                };
            }''')
            font_dict = font.json_value()
            font_str = f"{font_dict['family']}, {font_dict['size']}, {font_dict['weight']}, {font_dict['style']}, {font_dict['color']}"
            if font_str not in unique_fonts:
                unique_fonts.add(font_str)
                print(font_str)

    @staticmethod
    def try_to_figma_fonts_and_styles_by_pwr():
        access_token = "figd_4q5Ya2IGbIFZ5l5whAjuRbCVRIQX0Gj5ob-0mofE"
        file_id = "HKU560npofUSJr8rrdHi7k"
        url = f'https://api.figma.com/v1/files/{file_id}'
        headers = {'X-Figma-Token': access_token}
        response = requests.get(url, headers=headers)
        data = response.json()
        with open('test-datas/figma_json/file.json', 'w') as f:
            json.dump(data, f)
        print("JSON object saved to file.")

    @staticmethod
    def try_to_get_figma_fonts_and_styles_parse_json():
        access_token = "figd_4q5Ya2IGbIFZ5l5whAjuRbCVRIQX0Gj5ob-0mofE"
        file_id = "HKU560npofUSJr8rrdHi7k"
        url = f'https://api.figma.com/v1/files/{file_id}'
        headers = {'X-Figma-Token': access_token}
        response = requests.get(url, headers=headers)

        def find_font_families(node, font_families):
            if 'style' in node and 'fontFamily' in node['style']:
                font_families.append(node['style']['fontFamily'])
            if 'children' in node:
                for child in node['children']:
                    find_font_families(child, font_families)

        font_families = []
        for node in response.json()['document']['children']:
            find_font_families(node, font_families)
        unique_font_families = list(set(font_families))
        print(f"fontFamily: {unique_font_families}")

        def find_font_size(node, font_size):
            if 'style' in node and 'fontSize' in node['style']:
                font_size.append(node['style']['fontSize'])
            if 'children' in node:
                for child in node['children']:
                    find_font_size(child, font_size)

        font_size = []
        for node in response.json()['document']['children']:
            find_font_size(node, font_size)
        unique_font_size = list(set(font_size))
        print(f"fontSize: {unique_font_size}")

        def find_font_weight(node, font_weight):
            if 'style' in node and 'fontWeight' in node['style']:
                font_weight.append(node['style']['fontWeight'])
            if 'children' in node:
                for child in node['children']:
                    find_font_weight(child, font_weight)

        font_weight = []
        for node in response.json()['document']['children']:
            find_font_weight(node, font_weight)
        unique_font_weight = list(set(font_weight))
        print(f"fontWeight: {unique_font_weight}")

        # def find_font_style(node, font_style):
        #     if 'style' in node and 'fontStyle' in node['style']:
        #         font_style.append(node['style']['fontStyle'])
        #     if 'children' in node:
        #         for child in node['children']:
        #             find_font_style(child, font_style)
        # font_style = []
        # for node in response.json()['document']['children']:
        #     find_font_style(node, font_style)
        # unique_font_style = list(set(font_style))
        # print(unique_font_style)
