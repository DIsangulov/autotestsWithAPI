import json

import requests

from req.Api.req_auth import AuthApi
from req.Api.req_storage_worker import StorageWorker
from resourses.credentials import TestUsers, TARGET_URL

_session_instance = {}


def _get_session_instance(username: str) -> requests.Session:
    if username not in _session_instance:
        _session_instance[username] = requests.Session()
    return _session_instance[username]


class UserSession:

    def __init__(self, *, auth_data: dict = TestUsers.DpQaa, with_auth: bool = True):

        self.host = TARGET_URL

        self.username = auth_data.get("username")
        self._password = auth_data.get("password")
        self._local = auth_data.get("local")

        self.sess = _get_session_instance(self.username)
        # self.sess.headers.update({'token': self.token})
        # print(f"tok: {self.sess.headers.get('token')}")
        self.sess.verify = False

        self.user_id = None

        if 'token' not in self.sess.headers:
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
        self.sess.headers.update({'token': dct['token']})

        return resp

    def get_self_user_id(self) -> int:
        """Возвращает 'user_id' текущего пользователя"""
        if self.user_id is None:
            resp = self.sess.get(f"{self.host}/back/dp.peopler/profile")
            assert resp.status_code == 200, f"Ошибка при получении профиля пользователя {resp.status_code}, {resp.text}"

            dct = json.loads(resp.text)
            self.user_id = int(dct['res']['user_id'])
        return self.user_id

    def get_self_role_id(self) -> int:
        """Возвращает 'role_id' текущего пользователя"""
        resp = self.sess.get(f"{self.host}/back/dp.peopler/profile")
        assert resp.status_code == 200, f"Ошибка при получении профиля пользователя {resp.status_code}, {resp.text}"

        dct = json.loads(resp.text)
        return int(dct['res']['role_id'])

    def _get_db_info_row_by_name(self, db_name: str) -> dict | None:
        """Получение всех БД, возвращает первое вхождение по 'name' в виде:
        {
          "id": int,
          "name": str,
          "tables_count": int,
          "description": str
        }
        """
        resp = StorageWorker(self.sess, self.host).storage_worker_storage_db_get()
        # resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/db")
        assert resp.status_code == 200, \
            f"""Ошибка при получении списка хранилищ
            debug:  {UserSession.__name__}::{self._get_db_info_row_by_name.__name__}
            status_code: {resp.status_code},
            resp:   {resp.text}
            """
        dct = json.loads(resp.text)
        db_info_rows = dct['res']
        return next((db_info for db_info in db_info_rows if db_info['name'] == db_name), None)

    def get_db_id_by_name(self, db_name: str) -> int:
        """Возвращает 'id' хранилища с указанным именем"""
        # resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/db")
        # assert resp.status_code == 200, f"Ошибка при получении списка хранилищ {resp.status_code}, {resp.text}"
        #
        # dct = json.loads(resp.text)
        # db_info_rows = dct['res']
        # db_info_row = next((db_info for db_info in db_info_rows if db_info['name'] == db_name), None)
        db_info_row = self._get_db_info_row_by_name(db_name)
        assert db_info_row is not None, f"Не удалось найти базу данных с именем {db_name}"
        return db_info_row['id']

    def check_db_is_exists(self, db_name: str) -> bool:
        """
        Проверка, что БД с именем 'db_name' уже существует
        :return: True - существует, False - не существует
        """
        ch_db = self._get_db_info_row_by_name(db_name)
        if ch_db is None:
            return False
        else:
            return True

    def asserts_check_db_and_table_is_exists(self, db_name: str, table_name: str) -> None:
        """
        Проверка наличия БД 'db_name'\n
        Проверка наличия таблицы 'table_name' в БД 'db_name'\n
        :raise AssertionError
        """

        assert self.check_db_is_exists(db_name), f"""Не удалось найти базу данных с именем {db_name}"""

        resp = StorageWorker(self.sess, self.host).storage_worker_show_base_db_name_get(db_name)
        assert resp.status_code == 200, \
            f"""Ошибка при получении структуры БД
            debug:  {UserSession.__name__}::{self.asserts_check_db_and_table_is_exists.__name__}
            status_code: {resp.status_code}
            resp:   {resp.text}
            """

        resp_json = json.loads(resp.text)
        tables_info_rows = resp_json["res"]["tables"]
        tab_info = next((tab_info for tab_info in tables_info_rows if tab_info['tab_name'] == table_name), None)
        assert tab_info is not None, \
            f"""Не удалось найти таблицу с именем {table_name}
            debug:  {UserSession.__name__}::{self.asserts_check_db_and_table_is_exists.__name__}
            db_name: {db_name}
            table_name: {table_name}
            """
