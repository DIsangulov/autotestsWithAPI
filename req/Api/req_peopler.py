import json
import random

from req.Helpers.base_req import BaseReq


class Peopler(BaseReq):

    def _get_user_id(self) -> int:
        """Возвращает 'user_id' текущего пользователя"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/profile", headers=header, verify=False)
        dct = json.loads(resp.text)
        return dct['res']['user_id']

    # def peopler_mainpage_get(self):

    # FIXME: работа ключей email, name и .т.п. под вопросом ещё (c) Swagger
    # на фронте оно только меняет "роль" группе?
    def peopler_many_users_put(self):
        body = {"users":
            [
                {"id": 7741},       # Dnaikk1
                {"id": 8975}        # auto_dp_4421
            ],
            "role_id": 76,  # sys_api_test
        }
        header = {'token': self.token}
        resp = self.sess.put(f"{self.host}/back/dp.peopler/many_users", headers=header, json=body, verify=False)
        return resp

    def peopler_many_users_post(self):
        random_num = random.randint(1500, 1996)
        body = {
            # "role_id": 76,  # sys_api_test
            "users": [
                {
                    "role_id": 76,  # sys_api_test
                    "name": f"auto_dp_many_users_{random_num}",
                    # "is_admin":     True,
                    # "is_system":    True,
                    # "is_tech":      True
                },
                {
                    "role_id": 76,  # sys_api_test
                    "name": f"auto_dp_many_users_{random_num+1}",
                },
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
        """Создание нового '@доменного' пользователя"""
        random_num = random.randint(1000, 1500)

        body = {
            "name": f"auto_dp_{random_num}",
            "role_id": 76,  # sys_api_test
            # "is_admin":     True,
            # "is_system":    True,
            # "is_tech":      True
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.peopler/users", headers=header, json=body, verify=False)

        # print(json.loads(resp.text)['res'])
        return resp

    def peopler_users_id_get(self, user_id=None):
        """Получить информацию пользователя по **ID**"""
        if user_id is None:
            user_id = self._get_user_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/users/" + str(user_id), headers=header, verify=False)
        return resp

    def peopler_users_id_put(self, user_id=None, body=None):
        header = {'token': self.token}
        resp = self.sess.put(f"{self.host}/back/dp.peopler/users/" + str(user_id), headers=header, json=body, verify=False)
        return resp

    def peopler_users_delete(self, user_id=None):
        """Удалить пользователя по **ID**"""

        if user_id is None:
            resp_new_user = self.peopler_users_post()           # Создание нового пользователя
            assert resp_new_user.status_code == 200, \
                f"Ошибка при создании нового пользователя, код: {resp_new_user.status_code}, {resp_new_user.text}"
            user_id = json.loads(resp_new_user.text)['res']     # Получение user_id нового пользователя

        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.peopler/users/" + str(user_id), headers=header, verify=False)
        # print(f"Пользователь {user_id}, был удален")
        return resp
