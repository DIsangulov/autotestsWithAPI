import json
import os

import requests

from resourses.credentials import DpQaa, DpQaaLocal


# TODO: rename > UserSession ?
class BaseReq:

    def __init__(self, sess, host, authdata: dict = None, withauth: bool = True):
        # self.sess = sess
        self.sess = requests.Session()
        self.host = host
        self.token = None

        # self.sess.headers.update({'token': self.token})
        self.sess.verify = False

        self.username   = None
        self._password  = None
        self._local     = False

        if authdata is None:
            if self._local:
                self.username = os.environ.get('TARGET_API_USER', DpQaaLocal.USER)
                self._password = os.environ.get('TARGET_API_PASSWORD', DpQaaLocal.PASS)
            else:
                self.username = os.environ.get('TARGET_API_USER', DpQaa.USER)       # "dataplan_qaa@ngrsoftlab.ru"
                self._password = os.environ.get('TARGET_API_PASSWORD', DpQaa.PASS)  # "fHNHQBc7jEKfaO0kywZz!!"
        else:
            # self.username = os.environ.get('TARGET_API_USER', authdata['username'])
            # self._password = os.environ.get('TARGET_API_PASSWORD', authdata['password'])
            # self._local = authdata['local']
            assert False, f"Авторизация по пользовательской 'authdata' не реализован"
            pass

        if withauth:
            self.auth()

    def auth(self):
        data = {
            "username": self.username,
            "password": self._password,
            "local":    self._local
        }
        # resp = self.sess.post(f"{self.host}/back/dp.auth/login", json=data, verify=False)
        resp = self.sess.post(f"{self.host}/back/dp.auth/login", json=data)

        assert resp.status_code == 200, f"Ошибка авторизации, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        self.token = dct['token']
        self.sess.headers.update({'token': self.token})

        return resp

    # FIXME: определить self.user_id для уменьшения кол-ва обращений
    def get_self_user_id(self) -> int:
        """Возвращает 'user_id' текущего пользователя"""
        header = {'token': self.token}
        # resp = self.sess.get(f"{self.host}/back/dp.peopler/profile", headers=header, verify=False)
        resp = self.sess.get(f"{self.host}/back/dp.peopler/profile", headers=header)
        dct = json.loads(resp.text)
        return dct['res']['user_id']

    def get_db_id_by_name(self, db_name: str) -> int:
        """Возвращает 'id' хранилища с указанным именем"""
        header = {'token': self.token}
        # resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/db", headers=header, verify=False)
        resp = self.sess.get(f"{self.host}/back/dp.storage_worker/storage/db", headers=header)
        dct = json.loads(resp.text)
        db_info_rows = dct['res']
        db_info_row = next((db_info for db_info in db_info_rows if db_info['name'] == db_name), None)
        assert db_info_row is not None, f"Не удалось найти базу данных с именем {db_name}"

        db_id = db_info_row['id']

        return db_id
