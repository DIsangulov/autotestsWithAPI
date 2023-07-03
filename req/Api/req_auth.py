import requests

from req.Helpers.base_req_raw import BaseReqRaw


class AuthApi(BaseReqRaw):

    def auth_ad_struct_get(self) -> requests.Response:
        """process GET req for getting domain AD struct"""
        return self.sess.get(f"{self.host}/back/dp.auth/ad_struct")

    def auth_local_register_post(self, body) -> requests.Response:
        """process POST req with new local user info (credentials + info) for registration"""
        return self.sess.post(f"{self.host}/back/dp.auth/local/register", json=body)

    # TODO: /back/dp.auth/login
    # def login(self):
    #     pass

    def auth_logout_get(self) -> requests.Response:
        """Выход из системы ( текущая сессия )"""
        return self.sess.get(f"{self.host}/back/dp.auth/logout")

    def auth_ou_users_post(self, body) -> requests.Response:
        """process POST req with OU name for getting user list from ou"""
        return self.sess.post(f"{self.host}/back/dp.auth/ou_users", json=body)

    def auth_sessions_get(self) -> requests.Response:
        """process GET req for getting all users sessions info"""
        # Получить список сессий >> Пользователей <-> число активных сессий
        return self.sess.get(f"{self.host}/back/dp.auth/sessions")

    def auth_sessions_all_uid_del(self, user_id) -> requests.Response:
        """process DELETE req for deleting all user sessions by user id"""
        # Удалить ВСЕ сессии пользователя **user_id**
        return self.sess.delete(f"{self.host}/back/dp.auth/sessions/all/{user_id}")

    def auth_sessions_one_sid_del(self, _session_id) -> requests.Response:
        """process DELETE req for deleting one user session by user id and session id"""
        # Удалить одну сессию
        return self.sess.delete(f"{self.host}/back/dp.auth/sessions/one/{_session_id}")

    def auth_sessions_uid_get(self, user_id) -> requests.Response:
        """process GET req for getting all users sessions info"""
        # Получить список сессий пользователя **user_id**
        return self.sess.get(f"{self.host}/back/dp.auth/sessions/{user_id}")
