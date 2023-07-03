import json
import random

from req.Helpers.base_req import BaseReq
from resourses.credentials import DpRoles

API_AUTO_TEST_ = "API_AUTO_TEST_"
# sys_api_test = self.get_role_id_by_name(DpRoles.sys_api_test) # FIXME: реализовать геттер для получения роли
sys_api_test = DpRoles.sys_api_test

auto_user_id = set()   # список для пользователей, созданных автоматически


class Peopler(BaseReq):

    def _collect_auto_user_id(self):
        resp_all_users = self.peopler_users_get()                           # получить список ВСЕХ пользователей
        all_users_info_rows = json.loads(resp_all_users.text)['res']
        for _row in all_users_info_rows:                                    # фильтровать пользователей по API_AUTO_TEST_
            # .lower автоматически применяется при регистрации @доменных пользователей
            if str(_row['name']).startswith(API_AUTO_TEST_.lower()) or str(_row['name']).startswith(API_AUTO_TEST_):
                auto_user_id.add(int(_row['id']))
        # FIXME: можно возвращаемым значением длину конечного списка возвращать, для ветвлений 'if'

    def _get_auto_user_id(self) -> int:
        """get from global auto_user_id: API_AUTO_TEST_x"""
        if len(auto_user_id) == 0:
            self._collect_auto_user_id()

        if len(auto_user_id) == 0:
            resp_new_user = self.peopler_users_post()                       # Создание нового @доменного пользователя
            assert resp_new_user.status_code == 200, \
                f"Ошибка при создании нового пользователя, код: {resp_new_user.status_code}, {resp_new_user.text}"

            new_user_id = json.loads(resp_new_user.text)['res']             # {"res":12345}
            auto_user_id.add(int(new_user_id))                              # добавление нового пользователя в auto_user_id

        return auto_user_id.pop()                                           # возвращает случайное значение из auto_user_id

    def peopler_mainpage_get(self):
        """process GET req to get pinned main page for user"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/mainpage", headers=header, verify=False)
        return resp

    # FIXME: работа ключей email, name и .т.п. под вопросом ещё (c) Swagger
    # на фронте оно только меняет "роль" группе?
    def peopler_many_users_put(self):
        auto_user_id_1 = self._get_auto_user_id()
        auto_user_id_2 = self._get_auto_user_id()
        body = {"users":
            [
                {"id": auto_user_id_1},
                {"id": auto_user_id_2}
            ],
            "role_id": sys_api_test,
        }
        header = {'token': self.token}
        resp = self.sess.put(f"{self.host}/back/dp.peopler/many_users", headers=header, json=body, verify=False)
        return resp

    def peopler_many_users_post(self):
        """process POST req for creating many users"""
        random_num = random.randint(1500, 1996)
        body = {
            # "role_id": 76,  # sys_api_test
            "users": [
                {
                    "role_id": sys_api_test,
                    "name": API_AUTO_TEST_ + f"many_users_{random_num}",
                    # "is_admin":     True,
                    # "is_system":    True,
                    # "is_tech":      True
                },
                {
                    "role_id": sys_api_test,
                    "name": API_AUTO_TEST_ + f"many_users_{random_num + 1}",
                },
            ]
        }

        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.peopler/many_users", headers=header, json=body, verify=False)
        return resp

    # TODO: [POST] /back/dp.peopler/pin_page/current_user

    # TODO: [DELETE] /back/dp.peopler/pin_page/current_user

    # TODO: [POST] /back/dp.peopler/pin_page/list/{type_subject}

    # TODO: [POST] /back/dp.peopler/pin_page/{type_subject}

    # TODO: [DELETE] /back/dp.peopler/pin_page/{type_subject}/{id}

    # TODO: [POST] /back/dp.peopler/pinned_page_status

    def peopler_profile_get(self):
        """process GET req for getting user profile by token"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/profile", headers=header, verify=False)
        return resp

    def peopler_profiles_get(self):
        """process GET req for getting user profiles"""
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
        str_random_num = str(random.randint(1000, 1500))

        body = {
            "name": API_AUTO_TEST_ + str_random_num,
            "role_id": sys_api_test,
            # "is_admin":     True,
            # "is_system":    True,
            # "is_tech":      True
        }
        header = {'token': self.token}
        resp = self.sess.post(f"{self.host}/back/dp.peopler/users", headers=header, json=body, verify=False)
        return resp

    def peopler_users_id_get(self, user_id=None):
        """Получить информацию пользователя по **ID**"""
        if user_id is None:
            user_id = self.get_self_user_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/users/{user_id}", headers=header, verify=False)
        return resp

    def peopler_users_id_put(self, user_id: int = None, body: dict = None):
        """process PUT req for editing user by id"""

        if user_id is None:
            user_id = self._get_auto_user_id()
            body = {
                "role_id":     sys_api_test,
                "is_admin":    False,
                "is_system":   False,
                "is_tech":     False
            }

        header = {'token': self.token}
        resp = self.sess.put(f"{self.host}/back/dp.peopler/users/{user_id}", headers=header, json=body, verify=False)
        return resp

    def peopler_users_delete(self, user_id=None):
        """Удалить пользователя по **ID**"""

        if user_id is None:
            user_id = self._get_auto_user_id()

        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.peopler/users/{user_id}", headers=header, verify=False)
        # print(f"Пользователь {user_id}, был удален")
        return resp

    # __del__

    # Главное - не прострелить ногу # метод удаляет всех пользователей, которые остались в auto_user_id
    def all_api_auto_test_user_delete(self):
        self._collect_auto_user_id()
        while len(auto_user_id) > 0:
            self.peopler_users_delete(auto_user_id.pop())
