import requests
import pytest
import self as self
import urllib3
import json  # почитать

main_url = 'https://10.130.0.22/'
auth_token = None


class TestAuthApi:
    session = requests.Session()

    def test_login_no_local(self):
        url = main_url + 'back/dp.auth/login'
        datas = {"username": "dataplan_qaa@ngrsoftlab.ru",
                 "password": "fHNHQBc7jEKfaO0kywZz!"}
        urllib3.disable_warnings()
        response = self.session.post(url, json=datas, verify=False)
        global auth_token
        auth_token = str(response.text)[10:][:-3]
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"
        return auth_token

    def test_absorber_library_columns(self):  #  доработать ассерты
        url = main_url + 'back/dp.absorber/library/columns'
        header = {"token": auth_token}
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"
        assert isinstance(response.json().get('id'), int)


