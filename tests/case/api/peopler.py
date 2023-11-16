import json

from req.Helpers.user_session import UserSession
from req.Api.req_peopler import Peopler
from resourses.constants import API_AUTO_TEST_, UI_AUTO_TEST_
from resourses.static_methods import get_str_random_num

officer_role_id = 3     # or any test_role_id

test_user_id = set()    # список тестовых пользователей, созданных автоматически


class PeoplerCase(UserSession):

    def _collect_auto_user_id(self, *, username_prefix) -> set:

        if username_prefix not in (API_AUTO_TEST_, UI_AUTO_TEST_):
            assert False, f"""
            Not allowed to use function {self.__class__._collect_auto_user_id.__name__}
            for prefix: '{username_prefix}'"""

        # получить список ВСЕХ пользователей
        resp = Peopler(self.sess, self.host).peopler_users_get()
        assert resp.status_code == 200, f"""
        assert::peopler_users_get, failed.
        status_code: {resp.status_code}
        resp.text: {resp.text}"""

        collected_user_id = set()

        all_users_info_rows = json.loads(resp.text)['res']
        # фильтровать по username_starts_with
        for _row in all_users_info_rows:
            # .lower автоматически применяется при регистрации @доменных пользователей
            if str(_row['name']).startswith(username_prefix.lower()) or str(_row['name']).startswith(username_prefix):
                collected_user_id.add(int(_row['id']))
        return collected_user_id

    def get_test_user_id(self) -> int:
        """get from global auto_user_id: API_AUTO_TEST_x"""
        global test_user_id
        if len(test_user_id) == 0:
            test_user_id = self._collect_auto_user_id(username_prefix=API_AUTO_TEST_)

        if len(test_user_id) == 0:
            resp_new_user = self.case_peopler_users_post()          # Создание нового @доменного пользователя
            assert resp_new_user.status_code == 200, \
                f"Ошибка при создании нового пользователя, код: {resp_new_user.status_code}, {resp_new_user.text}"

            new_user_id = json.loads(resp_new_user.text)['res']     # {"res":12345}
            return int(new_user_id)

        return test_user_id.pop()

    def case_peopler_mainpage_get(self):
        req = Peopler(self.sess, self.host)
        resp = req.peopler_mainpage_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_peopler_many_users_put(self):
        # front: поменять роль группе пользователей
        req = Peopler(self.sess, self.host)
        # FIXME: может дважды выпасть один и тот же user_id
        auto_user_id_1 = self.get_test_user_id()
        auto_user_id_2 = self.get_test_user_id()
        body = {
            "users": [
                {
                    "id": auto_user_id_1,
                },
                {
                    "id": auto_user_id_2
                }
            ],
            "role_id": officer_role_id,
        }

        resp = req.peopler_many_users_put(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_peopler_many_users_post(self):
        req = Peopler(self.sess, self.host)

        random_num = get_str_random_num(3)
        body = {
            "users": [
                {
                    "role_id": officer_role_id,
                    "name": API_AUTO_TEST_ + f"many_users_1_{random_num}",
                    # "is_admin":     True,
                    # "is_system":    True,
                    # "is_tech":      True
                },
                {
                    "role_id": officer_role_id,
                    "name": API_AUTO_TEST_ + f"many_users_2_{random_num}",
                },
            ]
        }
        resp = req.peopler_many_users_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # == peopler/pin_page/x ========================================
    def case_peopler_pin_page_current_user_post(self, page_path):
        # Закрепление страницы 'page_path' за текущим пользователем
        req = Peopler(self.sess, self.host)
        post_data = {
            # "obj_id": 0,
            # "obj_type": "script",
            "path": page_path  # sample: "/scripts"
        }
        resp = req.peopler_pin_page_current_user_post(post_data)
        assert resp.status_code == 200, f"1.Ошибка, код {resp.status_code}, {resp.text}"

        # Проверка новой закрепленной страницы за текущим пользователем
        resp_mainpage = req.peopler_mainpage_get()
        expecting_resp = '{"res":\"' + page_path + '\"}\n'
        assert resp_mainpage.text == expecting_resp, f"""0.Ошибка,
            status_code: {resp_mainpage.status_code}
            expecting_resp: {expecting_resp}
            resp.text: {resp_mainpage.text}"""

    def case_peopler_pin_page_current_user_delete(self):
        # открепить закреп от текущего пользователя
        req = Peopler(self.sess, self.host)
        resp = req.peopler_pin_page_current_user_delete()
        # {"error":{"code":400,"msg":"страницу не удалось открепить (она не была закреплена для данного субъекта)"}}
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_peopler_pin_page_list_type_subject_post(self, sub_type: str, page_path: str):
        # получить список закрепленных пользователей (sub_type='user') или ролей (sub_type='role') для "page_path"
        req = Peopler(self.sess, self.host)
        data = {
            "path": page_path
        }
        resp = req.peopler_pin_page_list_type_subject_post(sub_type, data)
        assert resp.status_code == 200, f"""Ошибка,
            subject_type:   {sub_type}
            page_path:      {page_path}
            
            status_code:    {resp.status_code}
            resp: {resp.text}"""

    def case_peopler_pin_page_type_subject_post(self, sub_type: str, sub_id: int | None, replace_None: bool):
        # закрепить у пользователя (sub_type='user') или роли (sub_type='role')
        req = Peopler(self.sess, self.host)

        if replace_None and sub_id is None:
            if sub_type == "user":
                sub_id = self.get_self_user_id()    # == peopler_pin_page_current_user_delete
            if sub_type == "role":
                sub_id = officer_role_id

        post_data = {
            "obj_id": 0,                  # закрепление конкретной сущности
            "obj_type": "metaprofiles",   # тип этой сущности
            "path": "/metaprofiles",
            "subject_id": sub_id
        }

        resp = req.peopler_pin_page_type_subject_post(sub_type, post_data)
        assert resp.status_code == 200, f"""Ошибка,
            subject_type:   {sub_type}
            subject_id:     {sub_id}
            
            post_data:      {post_data}
            status_code:    {resp.status_code}
            resp: {resp.text}"""

    def case_peopler_pin_page_type_subject_id_delete(self, sub_type: str, sub_id: int | None, replace_None: bool):
        # убрать закреп у пользователя (sub_type='user') или роли (sub_type='role')
        req = Peopler(self.sess, self.host)

        if replace_None and sub_id is None:
            if sub_type == "user":
                sub_id = self.get_self_user_id()    # == peopler_pin_page_current_user_delete
            if sub_type == "role":
                sub_id = officer_role_id

        resp = req.peopler_pin_page_type_subject_id_delete(sub_type, sub_id)
        assert resp.status_code == 200, f"""Ошибка,
            subject_type:   {sub_type}
            subject_id:     {sub_id}
            
            status_code:    {resp.status_code}
            resp: {resp.text}"""
        # {"error":{"code":400,"msg":"страницу не удалось открепить (она не была закреплена для данного субъекта)"}}

    def case_peopler_pinned_page_status_post(self, page_path):
        # закреплен ли "path" за текущим пользователем
        # {"res":0} - не закреплен
        # {"res":1} - закреплен для пользователя
        # {"res":2} - закреплен для роли (роли установленной для пользователя)
        req = Peopler(self.sess, self.host)
        data = {
            "path": page_path
        }
        resp = req.peopler_pinned_page_status_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
    # == peopler/pin_page/x ========================================

    def case_peopler_profile_get(self):
        req = Peopler(self.sess, self.host)
        resp = req.peopler_profile_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_peopler_profiles_get(self):
        req = Peopler(self.sess, self.host)
        resp = req.peopler_profiles_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_peopler_users_get(self):
        req = Peopler(self.sess, self.host)
        resp = req.peopler_users_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_peopler_users_post(self):
        req = Peopler(self.sess, self.host)

        body = {
            "name": API_AUTO_TEST_ + get_str_random_num(),
            "role_id": officer_role_id,
            # "is_admin":     True,
            # "is_system":    True,
            # "is_tech":      True
        }
        resp = req.peopler_users_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        return resp     # исп: def _get_auto_user_id(self)

    def case_peopler_users_id_get(self):
        req = Peopler(self.sess, self.host)
        user_id = self.get_self_user_id()
        resp = req.peopler_users_id_get(user_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_peopler_users_id_put(self):
        req = Peopler(self.sess, self.host)
        user_id = self.get_test_user_id()
        body = {
                "id": user_id,
                "role_id":     officer_role_id,
                "is_admin":    False,
                "is_system":   False,
                "is_tech":     False
        }
        resp = req.peopler_users_id_put(user_id, body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_peopler_users_delete(self):
        req = Peopler(self.sess, self.host)
        user_id = self.get_test_user_id()
        resp = req.peopler_users_id_delete(user_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(f"Пользователь {user_id}, был удален")

    # __del__
    # Главное - не прострелить ногу # метод удаляет всех пользователей с приставкой users_prefix
    def all_users_with_prefix_delete(self, users_prefix):
        user_id_set = self._collect_auto_user_id(username_prefix=users_prefix)

        while len(user_id_set) > 0:
            Peopler(self.sess, self.host).peopler_users_id_delete(user_id_set.pop())
