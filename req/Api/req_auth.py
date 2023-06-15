import json
import random

from req.Helpers.base_req import BaseReq
from req.Api.req_peopler import Peopler


class AuthApi(BaseReq):

    @staticmethod
    def get_sess_id(req: BaseReq):
        """Возвращает 'id' СЛУЧАЙНОЙ активной **сессии**"""
        header = {'token': req.token}
        resp = req.sess.get(f"{req.host}/back/dp.auth/sessions/" + str(Peopler.get_user_id(req)), headers=header, verify=False)
        dct = json.loads(resp.text)

        # сессии в ответе не сортированы, сейчас просто возвращает айдишник, который лежит ниже всего в ответе
        return dct['res'][-1]['id']

    def auth_ad_struct_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/ad_struct", headers=header, verify=False)
        return resp

    def auth_local_register_post(self):

        random_num = random.randint(0, 9999)
        body = {
            "rusname":      "Авто Мобиль",
            "username":     f"auto_dp_{random_num}",
            "password":     "12345678",
            "email":        "auto_mail@mail.ru",
            "mobile":       "+7 999 999 99 99",
            "department":   "Отдел",
            "title":        "Должность",
            "local":        True
        }

        resp = self.sess.post(f"{self.host}/back/dp.auth/local/register", json=body, verify=False)
        return resp

    # Логин проводится в BaseReq
    # def login(self):
    #     pass

    def auth_ou_users_post(self):
        header = {'token': self.token}
        body = {
            "ou": "OU=Отдел внедрения и сервиса,OU=Центр профессиональных сервисов,OU=NGR,OU=Employees,DC=angaratech,DC=ru"}
        resp = self.sess.post(f"{self.host}/back/dp.auth/ou_users", headers=header, json=body, verify=False)
        return resp

    def auth_sessions_get(self):
        """Получить список сессий >> Пользователей <-> число активных сессий"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/sessions", headers=header, verify=False)
        return resp

    def auth_sessions_all_uid_del(self, user_id=None):
        """Удалить ВСЕ сессии пользователя **user_id**"""

        if user_id is None:
            user_id = Peopler.get_user_id(self)

        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.auth/sessions/all/" + str(user_id), headers=header, verify=False)
        return resp

    def auth_sessions_one_sid_del(self, session_id=None):
        """Удалить одну сессию"""

        if session_id is None:
            session_id = AuthApi.get_sess_id(self)

        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.auth/sessions/one/" + str(session_id), headers=header, verify=False)
        return resp

    def auth_sessions_uid_get(self, user_id=None):
        """Получить список сессий пользователя **user_id**"""

        if user_id is None:
            user_id = Peopler.get_user_id(self)

        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/sessions/" + str(user_id), headers=header, verify=False)
        return resp

    def auth_logout_get(self):
        """Выход из системы ( текущая сессия )"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/logout", headers=header, verify=False)
        return resp
