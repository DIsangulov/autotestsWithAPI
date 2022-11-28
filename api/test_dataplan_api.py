import requests
import pytest
import self as self
import urllib3

main_url = 'https://10.130.0.22/'
auth_token = None


class TestAuthApi:
    session = requests.Session()

    def test_login_no_local(self):
        url = main_url + 'back/dp.auth/login'
        datas = {
            "username": "dataplan_qaa@ngrsoftlab.ru",
            "password": "fHNHQBc7jEKfaO0kywZz!"
        }
        urllib3.disable_warnings()
        response = self.session.post(url, json=datas, verify=False)
        global auth_token
        auth_token = str(response.text)[10:][:-3]
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"
        return auth_token

    def test_ad_struct(self):
        header = {
            "token": auth_token
        }
        url = main_url + 'back/dp.auth/ad_struct'
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_ou_users(self):
        header = {
            "token": auth_token
        }
        body = {
            "ou": "OU=Отдел внедрения и сервиса,OU=Центр профессиональных сервисов,OU=NGR,OU=Employees,DC=angaratech,DC=ru"
        }
        url = main_url + 'back/dp.auth/ou_users'
        response = self.session.post(url, headers=header, json=body, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"


class TestSessionsApi:
    session = requests.Session()

    def test_sessions_user_id(self):
        url = main_url + 'back/dp.auth/sessions/413'
        header = {
            "token": auth_token
        }
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_session(self):
        url = main_url + 'back/dp.auth/sessions'
        header = {
            "token": auth_token
        }
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    # def test_session_one_delete(self):
    #     url = main_url + 'back/dp.auth/sessions/one/933'
    #     header = {
    #         "token": auth_token
    #     }
    #     response = self.session.delete(url, headers=header, verify=False)
    #     print(response.status_code, response.text)
    #     assert response.status_code == 200, "Wrong response code"
    #
    # def test_session_all_delete(self):
    #     url = main_url + 'back/dp.auth/sessions/all/413'
    #     header = {
    #         "token": auth_token
    #     }
    #     response = self.session.delete(url, headers=header, verify=False)
    #     print(response.status_code, response.text)
    #     assert response.status_code == 200, "Wrong response code"


class TestServiceAPI:
    session = requests.Session()

    def test_tasks_do(self):
        url = main_url + 'back/tasks/do'
        header = {
            "token": auth_token
        }
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_healthIs(self):
        url = main_url + 'healthIs'
        header = {
            "token": auth_token
        }
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_update_settings(self):
        url = main_url + 'back/update_settings'
        header = {
            "token": auth_token
        }
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_update_settings(self):
        url = main_url + 'kill'
        header = {
            "token": auth_token
        }
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"


class TestVisualisationAPI:
    session = requests.Session()

    def test_visualisation_query(self):
        url = main_url + 'back/dp.visualisation/query'
        header = {
            "token": auth_token
        }
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_back_visualisation_query_do_id(self): #  какая-то хуйня с телом запроса
        header = {
            "token": auth_token
        }
        data = {
                "field": "low",
                "action": "contains",
                "value": "1",
                "value_type": "Nullable(Float64)"
        }
        params = {
                "name": ":tab",
                "type": "UInt8",
                "value": "dict",
                "default": "dict"
        }
        url = main_url + 'back/dp.visualisation/query/do/1460'
        response = self.session.post(url, headers=header, json=(data, params), verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    # def test_logout(self): #  end of test scope
    #     url = 'https://10.130.0.22/back/dp.auth/logout'
    #     response = self.session.get(url, verify=False)
    #     print(response.status_code, response.text)
    #     assert response.status_code == 401, "Wrong response code"
