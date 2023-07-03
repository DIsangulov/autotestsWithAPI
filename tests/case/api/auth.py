import json
import random

from req.Helpers.base_req import BaseReq
from req.Api.req_auth import AuthApi

API_AUTO_TEST_ = "API_AUTO_TEST_"

session_id = []     # 'id' сессий текущего пользователя


class AuthApiCase(BaseReq):

    def _get_session_id(self) -> int:
        self.case_auth_sessions_uid_get()                # получение всех session_id для текущего пользователя
        if len(session_id) == 0:
            # у self. пользователя не может быть число активных сессий == 0
            assert False, f"Число активных сессий у запрашивающего пользователя == 0"
        return session_id[-1]

    def case_auth_ad_struct_get(self):
        req = AuthApi(self.sess, self.host)
        resp = req.auth_ad_struct_get()

        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_auth_local_register_post(self):
        req = AuthApi(self.sess, self.host)

        str_random_num = str(random.randint(100, 999))
        body = {
            "rusname":      "Авто Мобиль",
            "username":     API_AUTO_TEST_ + str_random_num,
            "password":     "12345678",
            "email":        "auto_mail@mail.ru",
            "mobile":       "+7 999 999 99 99",
            "department":   "Отдел",
            "title":        "Должность",
            "local":        True
        }
        resp = req.auth_local_register_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_auth_logout_get(self):
        req = AuthApi(self.sess, self.host)

        resp = req.auth_logout_get()
        assert resp.status_code == 401, f"Ошибка, код {resp.status_code}, {resp.text}"
        assert resp.text == '{"res":"ok"}\n', f"Ошибка, текст ответа: {resp.text}"

        # print(resp.text)
        return resp

    def case_auth_ou_users_post(self):
        req = AuthApi(self.sess, self.host)

        body = {
            "ou": "OU=Отдел внедрения и сервиса,OU=Центр профессиональных сервисов,OU=NGR,OU=Employees,DC=angaratech,DC=ru"
        }
        resp = req.auth_ou_users_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_auth_sessions_get(self):
        req = AuthApi(self.sess, self.host)
        resp = req.auth_sessions_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_auth_sessions_all_uid_del(self):
        req = AuthApi(self.sess, self.host)

        user_id = self.get_self_user_id()
        resp = req.auth_sessions_all_uid_del(user_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_auth_sessions_one_sid_del(self):
        req = AuthApi(self.sess, self.host)

        _session_id = self._get_session_id()
        resp = req.auth_sessions_one_sid_del(_session_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_auth_sessions_uid_get(self):
        req = AuthApi(self.sess, self.host)

        user_id = self.get_self_user_id()
        resp = req.auth_sessions_uid_get(user_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # FIXME: перенести логику в _get_session_id
        session_id_info_rows = json.loads(resp.text)['res']

        for _row in session_id_info_rows:
            session_id.append(int(_row['id']))
        # print(f"session_id[] is: {session_id}")

        # print(resp.text)
        return resp

    # Удаление пользователей возможно через .peopler_users_delete()
