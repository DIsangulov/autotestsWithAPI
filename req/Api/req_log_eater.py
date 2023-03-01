from req.Helpers.base_req import BaseReq


class LogEater(BaseReq):

    def log_eater_audit_users_days_get(self, token):
        header = {'token': token}
        resp = self.sess.get(f"{self.host}/back/dp.log_eater/audit/users/1", headers=header, verify=False)
        return resp
