import json

from req.Helpers.base_req import BaseReq
import random

rand = None
user_id = None


class Peopler(BaseReq):

    def peopler_many_users_put(self, token):
        body = {"users":
            [
                {"id": 1339,
                 "name": "testapi2",
                 "role_id": 61
                 },
                {"id": 1338,
                 "name": "testusers@angaratech.ru",
                 "role_id": 58
                 },
                {"id": 1337,
                 "name": "testapi@angaratech.ru",
                 "role_id": 61
                 }
            ],
            "role_id": 58
        }
        header = {'token': token}
        resp = self.sess.put(f"{self.host}/back/dp.peopler/many_users", headers=header, json=body, verify=False)
        return resp

    def peopler_many_users_post(self, token):
        global rand
        rand = random.randint(1200, 12500)
        body = {
            "role_id": rand,
            "users": [
                {
                    "department": "123456789",
                    "email": "dataplan_qaa@ngrsoftlab.ru",
                    "local": True,
                    "mobile": "123456789",
                    "password": "fHNHQBc7jEKfaO0kywZz!",
                    "rusname": "Тест",
                    "title": "123456789",
                    "username": "dataplan_qaa@ngrsoftlab.ru"
                }
            ]
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.peopler/many_users", headers=header, json=body, verify=False)
        return resp

    def peopler_profile_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/profile", headers=header, verify=False)
        return resp

    def peopler_profiles_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/profiles", headers=header, verify=False)
        return resp

    def peopler_users_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/users", headers=header, verify=False)
        return resp

    def peopler_users_post(self, token):
        body = {
            "department": "TestAPI1",
            "email": "testapi1@tesapi1.ru",
            "local": True,
            "mobile": "89269876761",
            "password": "89269876761",
            "rusname": "ТестАПИ1",
            "title": "TestAPI1",
            "username": "testapi1"
        }
        header = {'token': token}
        resp = self.sess.post(f"{self.host}/back/dp.peopler/users", headers=header, json=body, verify=False)
        dct = json.loads(resp.text)
        global user_id
        user_id = dct['res']
        print(user_id)
        return resp

    def peopler_users_id_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/users/"+str(user_id), headers=header, verify=False)
        return resp

    def peopler_users_id_put(self, token):
        body = {
            "department": "TestAPI1",
            "email": "testapi1@tesapi1.ru",
            "local": True,
            "mobile": "89269876761",
            "password": "89269876761",
            "rusname": "ТестАПИ2",
            "title": "TestAPI1",
            "username": "testapi1"
        }
        header = {'token': token}
        resp = self.sess.put(f"{self.host}/back/dp.peopler/users/"+str(user_id), headers=header, json=body, verify=False)
        return resp

    def peopler_users_delete(self, token):
        header = {'token': token}
        resp = self.sess.delete(f"{self.host}/back/dp.peopler/users/"+str(user_id), headers=header, verify=False)
        return resp
