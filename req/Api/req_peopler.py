import json
import random

from req.Helpers.base_req import BaseReq
from resourses.credentials import DpQaa


class Peopler(BaseReq):

    @staticmethod
    def get_user_id(req: BaseReq):
        """Возвращает 'user_id' текущего пользователя"""
        header = {'token': req.token}
        resp = req.sess.get(f"{req.host}/back/dp.peopler/profile", headers=header, verify=False)
        dct = json.loads(resp.text)
        return dct['res']['user_id']

    def peopler_many_users_put(self):
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
        header = {'token': self.token}
        resp = self.sess.put(f"{self.host}/back/dp.peopler/many_users", headers=header, json=body, verify=False)
        return resp

    def peopler_many_users_post(self):
        rand = random.randint(1200, 12500)
        body = {
            "role_id": rand,
            "users": [
                {
                    "department": "123456789",
                    "email": DpQaa.USER,
                    "local": True,
                    "mobile": "123456789",
                    "password": DpQaa.PASS,
                    "rusname": "Тест",
                    "title": "123456789",
                    "username": DpQaa.USER
                }
            ]
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.peopler/many_users", headers=header, json=body, verify=False)
        return resp

    def peopler_profile_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/profile", headers=header, verify=False)
        return resp

    def peopler_profiles_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/profiles", headers=header, verify=False)
        return resp

    def peopler_users_get(self):
        """Получить список пользователей"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/users", headers=header, verify=False)
        return resp

    def peopler_users_post(self):
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
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.peopler/users", headers=header, json=body, verify=False)
        dct = json.loads(resp.text)

        print(resp.text)
        user_id = dct['res']
        print(user_id)
        return resp

    def peopler_users_id_get(self, user_id=None):
        """Получить информацию пользователя по **ID**"""
        if user_id is None:
            user_id = self.get_user_id(self)

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/users/" + str(user_id), headers=header, verify=False)
        return resp


    def peopler_users_id_put(self):
        # FIXME: Сейчас еп ничего не меняет
        user_id = 7741  # Dnaikk1
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
        header = {'token': self.token}
        resp = self.sess.put(f"{self.host}/back/dp.peopler/users/" + str(user_id), headers=header, json=body, verify=False)
        return resp

    # FIXME: Прежде, чем что-то удалять ОБЯЗАТЕЛЬНО, нужно создавать шаблонистый профиль
    def peopler_users_delete(self, user_id=None):
        """Удалить пользователя по **ID**"""
        if user_id is None:
            # Создание нового пользователя, затем удаление
            assert False, f"Нечего удалять"

        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.peopler/users/" + str(user_id), headers=header, verify=False)
        return resp
