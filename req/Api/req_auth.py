import json

from req.Helpers.base_req import BaseReq


class AuthApi(BaseReq):

    def get_user_id(self):
        """Возвращает 'user_id' текущего пользователя"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.peopler/profile", headers=header, verify=False)
        dct = json.loads(resp.text)
        return dct['res']['user_id']

    def get_sess_id(self):
        """Возвращает 'id' текущей **сессии**"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/sessions/" + str(self.get_user_id()), headers=header, verify=False)
        dct = json.loads(resp.text)

        # FIXME: получили id последней сессии?
        # сессии в ответе не сортированы
        # сейчас просто возвращает айдишник, который лежит ниже всего в ответе
        return dct['res'][-1]['id']

    def ad_struct_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/ad_struct", headers=header, verify=False)
        return resp

    #
    # def register(self):
    #     pass

    # Логин проводится в BaseReq
    # def login(self):
    #     pass

    def ou_users_post(self):
        header = {'token': self.token}
        body = {
            "ou": "OU=Отдел внедрения и сервиса,OU=Центр профессиональных сервисов,OU=NGR,OU=Employees,DC=angaratech,DC=ru"}; resp = self.sess.post(f"{self.host}/back/dp.auth/ou_users", headers=header, json=body, verify=False)
        return resp

    def sessions_get(self):
        """Получить список сессий >> Пользователей <-> число активных сессий"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/sessions", headers=header, verify=False)
        return resp

    def sessions_all_uid_del(self, user_id):
        """Удалить ВСЕ сессии пользователя **user_id**"""
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.auth/sessions/all/" + str(user_id), headers=header, verify=False)
        return resp

    def sessions_one_sid_del(self, session_id):
        """Удалить одну сессию"""
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.auth/sessions/one/" + str(session_id), headers=header, verify=False)
        return resp

    def sessions_uid_get(self, user_id):
        """Получить список сессий пользователя **user_id**"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/sessions/" + str(user_id), headers=header, verify=False)
        return resp

    def logout_get(self):
        """Выход из системы ( текущая сессия )"""
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/logout", headers=header, verify=False)
        return resp
