import json
import random

from req.Helpers.user_session import UserSession
from req.Api.req_peopler import Peopler
from resourses.constants import API_AUTO_TEST_

officer_role_id = 3

auto_test_user_id = set()   # список для пользователей, созданных автоматически


class PeoplerCase(UserSession):

    def _collect_auto_user_id(self):
        resp = Peopler(self.sess, self.host).peopler_users_get()    # получить список ВСЕХ пользователей
        assert resp.status_code == 200, f"assert::peopler_users_get, failed. status_code: {resp.status_code}, text: {resp.text}"

        all_users_info_rows = json.loads(resp.text)['res']
        for _row in all_users_info_rows:                            # фильтровать по API_AUTO_TEST_
            # .lower автоматически применяется при регистрации @доменных пользователей
            if str(_row['name']).startswith(API_AUTO_TEST_.lower()) or str(_row['name']).startswith(API_AUTO_TEST_):
                auto_test_user_id.add(int(_row['id']))

    def get_auto_test_user_id(self) -> int:
        """get from global auto_user_id: API_AUTO_TEST_x"""
        if len(auto_test_user_id) == 0:
            self._collect_auto_user_id()

        if len(auto_test_user_id) == 0:
            resp_new_user = self.case_peopler_users_post()          # Создание нового @доменного пользователя
            assert resp_new_user.status_code == 200, \
                f"Ошибка при создании нового пользователя, код: {resp_new_user.status_code}, {resp_new_user.text}"

            new_user_id = json.loads(resp_new_user.text)['res']     # {"res":12345}
            return int(new_user_id)                                 # вернуть 'id' нового пользователя

        return auto_test_user_id.pop()                                   # возвращает случайное значение из auto_user_id

    def case_peopler_mainpage_get(self):
        req = Peopler(self.sess, self.host)
        resp = req.peopler_mainpage_get()
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # LOOK: работа ключей | name, rolename | под вопросом ещё (c) Swagger
    # на фронте оно только меняет "роль" группе?
    def case_peopler_many_users_put(self):
        req = Peopler(self.sess, self.host)
        # FIXME: может дважды выпасть один и тот же user_id
        auto_user_id_1 = self.get_auto_test_user_id()
        auto_user_id_2 = self.get_auto_test_user_id()
        body = {
            "users": [
                {
                    "id": auto_user_id_1
                },
                {
                    "id": auto_user_id_2
                }
            ],
            "role_id": officer_role_id,
        }

        resp = req.peopler_many_users_put(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_peopler_many_users_post(self):
        req = Peopler(self.sess, self.host)

        random_num = random.randint(1500, 1996)
        body = {
            # "role_id": 76,
            "users": [
                {
                    "role_id": officer_role_id,
                    "name": API_AUTO_TEST_ + f"many_users_{random_num}",
                    # "is_admin":     True,
                    # "is_system":    True,
                    # "is_tech":      True
                },
                {
                    "role_id": officer_role_id,
                    "name": API_AUTO_TEST_ + f"many_users_{random_num + 1}",
                },
            ]
        }
        resp = req.peopler_many_users_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    # == peopler/pin_page/x ========================================
    # https://tasks.ngrsoftlab.ru/browse/DAT-4982
    def _peopler_pin_page_current_user_path_post(self, pin_path):
        # закрепить страницу "pin_path" за текущим пользователем
        req = Peopler(self.sess, self.host)
        data = {
            # "obj_id": 0,
            # "obj_type": "script",
            "path": pin_path        # sample: "/scripts"
        }
        resp = req.peopler_pin_page_current_user_post(data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # todo: get_mainpage >> assert на ответ resp.text = pin_path
        return resp

    def case_peopler_pin_page_current_user_post(self):
        path = "/scripts"
        self._peopler_pin_page_current_user_path_post(path)

    def case_peopler_pin_page_current_user_delete(self):
        # открепить закреп от текущего пользователя
        req = Peopler(self.sess, self.host)
        resp = req.peopler_pin_page_current_user_delete()
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # {"error":{"code":400,"msg":"страницу не удалось открепить (она не была закреплена для данного субъекта)"}}

    def _peopler_pin_page_list_type_subject_post(self, type_subject, path):
        # получить список закрепленных пользователей "user" или ролей "role" для "path"
        req = Peopler(self.sess, self.host)
        data = {
            "path": path
        }
        resp = req.peopler_pin_page_list_type_subject_post(type_subject, data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        return resp

    def case_peopler_pin_page_list_role_post(self):
        type_subject = "role"
        path = "/scripts"
        self._peopler_pin_page_list_type_subject_post(type_subject, path)

    def case_peopler_pin_page_list_user_post(self):
        type_subject = "user"
        path = "/scripts"
        self._peopler_pin_page_list_type_subject_post(type_subject, path)

    def case_peopler_pin_page_type_subject_post(self):
        # закрепить у пользователя|роли (subject_id), что (path)
        req = Peopler(self.sess, self.host)

        # todo: user / role
        subject_type = "user"
        # subject_type = "role"

        data = {
            "obj_id": 0,                  # look: закрепление конкретной сущности
            "obj_type": "metaprofiles",   # look: тип этой сущности
            "path": "/metaprofiles",
            "subject_id": self.get_self_user_id()
        }

        resp = req.peopler_pin_page_type_subject_post(subject_type, data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_peopler_pin_page_type_subject_id_delete(self):
        # убрать закреп у пользователя|роли (id)
        req = Peopler(self.sess, self.host)

        # todo: user \ role
        # subject_type = "role"
        subject_type = "user"
        # subject_id = "5"  # sysop
        subject_id = self.get_self_user_id()    # == peopler_pin_page_current_user_delete

        resp = req.peopler_pin_page_type_subject_id_delete(subject_type, subject_id)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # {"error":{"code":400,"msg":"страницу не удалось открепить (она не была закреплена для данного субъекта)"}}

    def case_peopler_pinned_page_status_post(self):
        # закреплен ли "path" за текущим пользователем
        req = Peopler(self.sess, self.host)
        _path = "/scripts"
        data = {
            "path": _path
        }
        resp = req.peopler_pinned_page_status_post(data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # {"res":0}     # {"res":1}     # ?? {"res":2}
    # == peopler/pin_page/x ========================================

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
            "role_id": officer_role_id,
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
        user_id = self.get_auto_test_user_id()
        body = {
                "id": user_id,
                "role_id":     officer_role_id,
                "is_admin":    False,
                "is_system":   False,
                "is_tech":     False
        }
        resp = req.peopler_users_id_put(user_id, body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    def case_peopler_users_delete(self):
        req = Peopler(self.sess, self.host)
        user_id = self.get_auto_test_user_id()
        resp = req.peopler_users_id_delete(user_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(f"Пользователь {user_id}, был удален")

    # __del__

    # Главное - не прострелить ногу # метод удаляет всех пользователей c приставкой API_AUTO_TEST_
    def all_api_auto_test_user_delete(self):
        self._collect_auto_user_id()
        while len(auto_test_user_id) > 0:
            Peopler(self.sess, self.host).peopler_users_id_delete(auto_test_user_id.pop())
