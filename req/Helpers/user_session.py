import json
import os

import requests

from req.Api.req_auth import AuthApi
from resourses.credentials import TestUsers


class UserSession:

    def __init__(self, *, auth_data: dict = TestUsers.DpQaa, with_auth: bool = True):
        self.sess = requests.Session()
        # self.sess.headers.update({'token': self.token})
        self.sess.verify = False

        self.host = os.environ.get('TARGET_URL', "https://10.130.0.22")
        self.token = None
        self.user_id = None

        self.username = os.environ.get('TARGET_API_USER', auth_data.get("username"))
        self._password = os.environ.get('TARGET_API_PASSWORD', auth_data.get("password"))
        self._local = os.environ.get('TARGET_API_USER_IS_LOCAL', auth_data.get("local"))

        if with_auth:
            self.auth()

    def auth(self):
        data = {
            "username": self.username,
            "password": self._password,
            "local":    self._local
        }
        # resp = self.sess.post(f"{self.host}/back/dp.auth/login", json=data)
        resp = AuthApi(self.sess, self.host).auth_login_post(data)

        assert resp.status_code == 200, f"Ошибка авторизации, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        self.token = dct['token']
        self.sess.headers.update({'token': self.token})

        return resp

    def get_self_user_id(self) -> int:
        """Возвращает 'user_id' текущего пользователя"""
        if self.user_id is None:
            header = {'token': self.token}
            resp = self.sess.get(f"{self.host}/back/dp.peopler/profile", headers=header)
            dct = json.loads(resp.text)
            self.user_id = int(dct['res']['user_id'])
        return self.user_id

    def get_db_id_by_name(self, db_name: str) -> int:
        """Возвращает 'id' хранилища с указанным именем"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/db", headers=header)
        dct = json.loads(resp.text)
        db_info_rows = dct['res']
        db_info_row = next((db_info for db_info in db_info_rows if db_info['name'] == db_name), None)
        assert db_info_row is not None, f"Не удалось найти базу данных с именем {db_name}"

        db_id = db_info_row['id']

        return db_id
