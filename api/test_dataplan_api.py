import requests
import pytest
import self as self
import urllib3
import  faker
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

    def test_ad_struct(self):
        header = {"token": auth_token}
        url = main_url + 'back/dp.auth/ad_struct'
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_ou_users(self):
        header = {"token": auth_token}
        body = {
            "ou": "OU=Отдел внедрения и сервиса,OU=Центр профессиональных сервисов,OU=NGR,OU=Employees,DC=angaratech,DC=ru"}
        url = main_url + 'back/dp.auth/ou_users'
        response = self.session.post(url, headers=header, json=body, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"


class TestSessionsApi:
    session = requests.Session()

    def test_sessions_user_id(self):
        url = main_url + 'back/dp.auth/sessions/413'
        header = {"token": auth_token}
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_session(self):
        url = main_url + 'back/dp.auth/sessions'
        header = {"token": auth_token}
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    # def test_session_one_delete(self):
    #     url = main_url + 'back/dp.auth/sessions/one/933'
    #     header = {"token": auth_token}
    #     response = self.session.delete(url, headers=header, verify=False)
    #     print(response.status_code, response.text)
    #     assert response.status_code == 200, "Wrong response code"
    #
    # def test_session_all_delete(self):
    #     url = main_url + 'back/dp.auth/sessions/all/413'
    #     header = {"token": auth_token}
    #     response = self.session.delete(url, headers=header, verify=False)
    #     print(response.status_code, response.text)
    #     assert response.status_code == 200, "Wrong response code"


class TestServiceAPI:
    session = requests.Session()

    def test_tasks_do(self):
        url = main_url + 'back/tasks/do'
        header = {"token": auth_token}
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_healthIs(self):
        url = main_url + 'healthIs'
        header = {"token": auth_token}
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_update_settings(self):
        url = main_url + 'back/update_settings'
        header = {"token": auth_token}
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_kill(self):
        url = main_url + 'kill'
        header = {"token": auth_token}
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"


class TestVisualisationAPI:
    session = requests.Session()

    def test_visualisation_query(self):
        url = main_url + 'back/dp.visualisation/query'
        header = {"token": auth_token}
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_back_visualisation_query_do_id(self):  # field - low это дичь
        header = {"token": auth_token}
        body = {"filters": [
            {"action": "contains",
             "value": "1",
             "value_type": "Nullable(Float64)"}],
            "params": [{
                "default": "dict",
                "name": "tab",
                "type": "UInt8",
                "value": "dict"}]}
        url = main_url + 'back/dp.visualisation/query/do/133'
        response = self.session.post(url, headers=header, json=body, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_visualisation_query_save(self):  # field - low это дичь
        header = {"token": auth_token}
        body = {
            "id": 133,
            "name": "khsdf",
            "description": "adskjfjhk",
            "published": True,
            "opened": False,
            "author_id": 434,
            "author": "Снытко Татьяна",
            "editor_id": 434,
            "editor": "Снытко Татьяна",
            "created": "2021-09-27T08:20:18Z",
            "modified": "2021-09-27T08:20:18Z",
            "query": "",
            "auto": True,
            "settings":
                {
                    "base_id": 108934,
                    "tab_name": "zabbix",
                    "columns":
                        [{
                            "name": "id",
                            "type": "UInt16"
                        }],
                    "groupby": [],
                    "filters": [],
                    "agregators": [],
                    "limit": 50
                },
            "db_id": 108934,
            "db_name": "angara",
            "tables": "zabbix",
            "selective": True,
            "params": ""
        }
        url = main_url + 'back/dp.visualisation/query/save'
        response = self.session.post(url, headers=header, json=body, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_visualisation_query_usage(self):
        url = main_url + 'back/dp.visualisation/query/usage/133'
        header = {"token": auth_token}
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_visualisation_query_id(self):
        url = main_url + 'back/dp.visualisation/query/133'
        header = {"token": auth_token}
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    # def test_visualisation_reports_params_report_id(self):
    #     header = {"token": auth_token}
    #     body = {
    #         "column": "1",
    #         "dataseries_id": "1",
    #         "grid_id": "145",
    #         "other_id": "145",
    #         "other_name": "1"
    #     }
    #     url = main_url + 'back/dp.visualisation/reports/params/147'
    #     response = self.session.post(url, headers=header, json=body, verify=False)
    #     print(response.status_code, response.text)
    #     assert response.status_code == 200, "Wrong response code"

    def test_visualisation_reports(self):
        url = main_url + 'back/dp.visualisation/reports'
        header = {"token": auth_token}
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_visualisation_reports_report_id(self):
        url = main_url + 'back/dp.visualisation/reports/147'
        header = {"token": auth_token}
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_visualisation_reports_POST(self):
        pass

    def test_visualisation_visualisation(self):
        url = main_url + 'back/dp.visualisation/visualisation'
        header = {"token": auth_token}
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_visualisation_visualisation_post(self):
        pass

    def test_visualisation_visualisation_types(self):
        url = main_url + 'back/dp.visualisation/visualisation/types'
        header = {"token": auth_token}
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_visualisation_visualisation_usage_visualisation_id(self):
        url = main_url + 'back/dp.visualisation/visualisation/usage/273'
        header = {"token": auth_token}
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    def test_visualisation_visualisation_visualisation_id(self):
        url = main_url + 'back/dp.visualisation/visualisation/273'
        header = {"token": auth_token}
        response = self.session.get(url, headers=header, verify=False)
        print(response.status_code, response.text)
        assert response.status_code == 200, "Wrong response code"

    # def test_logout(self): #  end of test scope
    #     url = 'https://10.130.0.22/back/dp.auth/logout'
    #     response = self.session.get(url, verify=False)
    #     print(response.status_code, response.text)
    #     assert response.status_code == 401, "Wrong response code"
