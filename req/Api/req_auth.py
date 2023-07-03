import json
import random

import requests

from req.Helpers.base_req import BaseReq

API_AUTO_TEST_ = "API_AUTO_TEST_"

session_id = []     # 'id' сессий текущего пользователя


class AuthApiNew:

    def __init__(self, host, token):
        self.sess = requests.Session()
        self.host = host
        self.token = token

        self.sess.headers.update({'token': self.token})
        self.sess.verify = False

    def auth_ad_struct_get(self):
        """process GET req for getting domain AD struct"""

        return self.sess.get(f"{self.host}/back/dp.auth/ad_struct")



class AuthApi(BaseReq):

    def _get_session_id(self) -> int:
        self.auth_sessions_uid_get()                # получение всех session_id для текущего пользователя
        if len(session_id) == 0:
            # у self. пользователя не может быть число активных сессий == 0
            assert False, f"Число активных сессий у запрашивающего пользователя == 0"
        return session_id[-1]

    def auth_ad_struct_get(self):
        """process GET req for getting domain AD struct"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/ad_struct", headers=header, verify=False)
        return resp

    def auth_local_register_post(self):
        """process POST req with new local user info (credentials + info) for registration"""

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

        resp = self.sess.post(f"{self.host}/back/dp.auth/local/register", json=body, verify=False)
        return resp

    # TODO: /back/dp.auth/login
    # def login(self):
    #     pass

    def auth_logout_get(self):
        """Выход из системы ( текущая сессия )"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/logout", headers=header, verify=False)
        return resp

    def auth_ou_users_post(self):
        """process POST req with OU name for getting user list from ou"""
        header = {'token': self.token}
        body = {
            "ou": "OU=Отдел внедрения и сервиса,OU=Центр профессиональных сервисов,OU=NGR,OU=Employees,DC=angaratech,DC=ru"}
        resp = self.sess.post(f"{self.host}/back/dp.auth/ou_users", headers=header, json=body, verify=False)
        return resp

    def auth_sessions_get(self):
        """process GET req for getting all users sessions info"""
        # Получить список сессий >> Пользователей <-> число активных сессий
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/sessions", headers=header, verify=False)
        return resp

    def auth_sessions_all_uid_del(self, user_id=None):
        """process DELETE req for deleting all user sessions by user id"""
        # Удалить ВСЕ сессии пользователя **user_id**

        if user_id is None:
            user_id = self.get_self_user_id()

        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.auth/sessions/all/{user_id}", headers=header, verify=False)
        return resp

    def auth_sessions_one_sid_del(self, _session_id=None):
        """process DELETE req for deleting one user session by user id and session id"""
        # Удалить одну сессию

        if _session_id is None:
            # _session_id = AuthApi.get_sess_id(self)
            _session_id = self._get_session_id()

        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.auth/sessions/one/{_session_id}", headers=header, verify=False)
        return resp

    def auth_sessions_uid_get(self, user_id=None):
        """process GET req for getting all users sessions info"""
        # Получить список сессий пользователя **user_id**

        if user_id is None:
            user_id = self.get_self_user_id()

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/sessions/{user_id}", headers=header, verify=False)

        # FIXME: перенести логику в _get_session_id
        session_id_info_rows = json.loads(resp.text)['res']

        for _row in session_id_info_rows:
            session_id.append(int(_row['id']))
        # print(f"session_id[] is: {session_id}")

        return resp



    # Удаление пользователей возможно через Peopler.peopler_users_delete()
