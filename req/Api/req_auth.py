import json

from req.Helpers.base_req import BaseReq

uid = None
sess_id = None


class AuthApi(BaseReq):
    def __init__(self, sess, host):
        super().__init__(sess, host)
        self.uid = None
        self.sess_id = None

    def _set_uid(self):
        pass

    def _set_sess_id(self):
        pass

    def ad_struct_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/ad_struct", headers=header, verify=False)
        return resp

    def ou_users_post(self):
        header = {'token': self.token}
        body = {
            "ou": "OU=Отдел внедрения и сервиса,OU=Центр профессиональных сервисов,OU=NGR,OU=Employees,DC=angaratech,DC=ru"}
        resp = self.sess.post(f"{self.host}/back/dp.auth/ou_users", headers=header, json=body, verify=False)
        return resp

    def sessions_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/sessions", headers=header, verify=False)
        dct = json.loads(resp.text)
        global uid
        uid = dct['res'][-1]['user_id']  # получили id пользователя
        # print(uid)
        return resp

    def sessions_uid_get(self):  # здесь можем взять sid
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/sessions/" + str(uid), headers=header, verify=False)
        dct = json.loads(resp.text)
        global sess_id
        sess_id = dct['res'][-1]['id']  # получили id сессии
        print(sess_id)
        return resp

    def sessions_one_sid_del(self):
        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.auth/sessions/one/" + str(sess_id), headers=header, verify=False)
        return resp

    def sessions_all_uid_del(self):

        # FIXME:06081704 Таким образом мы переопределим глобал uid, но было бы неплохо сделать отдельный метод для этого
        self.sessions_get()

        header = {'token': self.token}
        resp = self.sess.delete(f"{self.host}/back/dp.auth/sessions/all/" + str(uid), headers=header, verify=False)
        # print(f"Current uid {uid}") # FIXME: Убрать
        return resp

    def logout_get(self):
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/logout", headers=header, verify=False)
        return resp
