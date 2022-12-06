import json

import pytest

from req.Helpers.base_req import BaseReq

sess_id = None


class AuthApi(BaseReq):

    def ad_struct(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/ad_struct", headers=header, verify=False)
        return resp

    def ou_users(self, token):
        header = {'token': token}
        body = {"ou": "OU=Отдел внедрения и сервиса,OU=Центр профессиональных сервисов,OU=NGR,OU=Employees,DC=angaratech,DC=ru"}
        resp = self.sess.post(f"{self.host}/back/dp.auth/ou_users", headers=header, json=body, verify=False)
        return resp

    def sessions(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/sessions", headers=header, verify=False)
        return resp

    def sessions_uid(self, token):  # здесь можем взять sid
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/sessions/1238", headers=header, verify=False)
        dct = json.loads(resp.text)
        global sess_id
        sess_id = dct['res'][-1]['id']  # получили id сессии
        print(sess_id)
        return resp

    def sessions_one_sid_del(self, token):
        header = {'token': token}
        resp = self.sess.delete(f"{self.host}/back/dp.auth/sessions/one/" + str(sess_id), headers=header, verify=False)
        return resp

    def sessions_all_uid_del(self, token):
        header = {'token': token}
        resp = self.sess.delete(f"{self.host}/back/dp.auth/sessions/all/1238", headers=header, verify=False)
        return resp

    def logout(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.auth/logout", headers=header, verify=False)
        return resp
