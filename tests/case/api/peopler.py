import json
import random

from req.Helpers.base_req import BaseReq
from req.Api.req_peopler import Peopler
from resourses.credentials import DpRoles

API_AUTO_TEST_ = "API_AUTO_TEST_"
# sys_api_test = self.get_role_id_by_name(DpRoles.sys_api_test) # FIXME: реализовать геттер для получения роли
sys_api_test = DpRoles.sys_api_test

auto_user_id = set()   # список для пользователей, созданных автоматически


class PeoplerCase(BaseReq):

    def _collect_auto_user_id(self):
        # resp_all_users = self.peopler_users_get()
        resp_all_users = Peopler(self.sess, self.host).peopler_users_get()   # получить список ВСЕХ пользователей
        all_users_info_rows = json.loads(resp_all_users.text)['res']
        for _row in all_users_info_rows:                                        # фильтровать по API_AUTO_TEST_
            # .lower автоматически применяется при регистрации @доменных пользователей
            if str(_row['name']).startswith(API_AUTO_TEST_.lower()) or str(_row['name']).startswith(API_AUTO_TEST_):
                auto_user_id.add(int(_row['id']))
        # FIXME: можно возвращаемым значением длину конечного списка возвращать, для ветвлений 'if'

    def _get_auto_user_id(self) -> int:
        """get from global auto_user_id: API_AUTO_TEST_x"""
        if len(auto_user_id) == 0:
            self._collect_auto_user_id()

        if len(auto_user_id) == 0:
            resp_new_user = self.case_peopler_users_post()                  # Создание нового @доменного пользователя
            assert resp_new_user.status_code == 200, \
                f"Ошибка при создании нового пользователя, код: {resp_new_user.status_code}, {resp_new_user.text}"

            new_user_id = json.loads(resp_new_user.text)['res']             # {"res":12345}
            auto_user_id.add(int(new_user_id))                              # добавление нового пользователя в auto_user_id

        return auto_user_id.pop()                                           # возвращает случайное значение из auto_user_id

    def case_peopler_mainpage_get(self):
        req = Peopler(self.sess, self.host)

        resp = req.peopler_mainpage_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    # FIXME: работа ключей | name, rolename | под вопросом ещё (c) Swagger
    # на фронте оно только меняет "роль" группе?
    def case_peopler_many_users_put(self):
        req = Peopler(self.sess, self.host)
        # FIXME: может дважды выпасть один и тот же user_id
        auto_user_id_1 = self._get_auto_user_id()
        auto_user_id_2 = self._get_auto_user_id()
        body = {"users":
            [
                {"id": auto_user_id_1},
                {"id": auto_user_id_2}
            ],
            "role_id": sys_api_test,
        }
        resp = req.peopler_many_users_put(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_peopler_many_users_post(self):
        req = Peopler(self.sess, self.host)

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
        resp = req.peopler_many_users_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_peopler_profile_get(self):
        req = Peopler(self.sess, self.host)
        resp = req.peopler_profile_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_peopler_profiles_get(self):
        req = Peopler(self.sess, self.host)
        resp = req.peopler_profiles_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_peopler_users_get(self):
        req = Peopler(self.sess, self.host)
        resp = req.peopler_users_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_peopler_users_post(self):
        req = Peopler(self.sess, self.host)

        str_random_num = str(random.randint(1000, 1500))
        body = {
            "name": API_AUTO_TEST_ + str_random_num,
            "role_id": sys_api_test,
            # "is_admin":     True,
            # "is_system":    True,
            # "is_tech":      True
        }
        resp = req.peopler_users_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)
        return resp     # исп: def _get_auto_user_id(self)

    def case_peopler_users_id_get(self):
        req = Peopler(self.sess, self.host)
        user_id = self.get_self_user_id()
        resp = req.peopler_users_id_get(user_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_peopler_users_id_put(self):
        req = Peopler(self.sess, self.host)
        user_id = self._get_auto_user_id()
        body = {
                "role_id":     sys_api_test,
                "is_admin":    False,
                "is_system":   False,
                "is_tech":     False
        }
        resp = req.peopler_users_id_put(user_id, body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_peopler_users_delete(self):
        req = Peopler(self.sess, self.host)
        user_id = self._get_auto_user_id()
        resp = req.peopler_users_delete(user_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(f"Пользователь {user_id}, был удален")

    # __del__

    # Главное - не прострелить ногу # метод удаляет всех пользователей c приставкой API_AUTO_TEST_
    def all_api_auto_test_user_delete(self):
        self._collect_auto_user_id()
        while len(auto_user_id) > 0:
            Peopler(self.sess, self.host).peopler_users_delete(auto_user_id.pop())
