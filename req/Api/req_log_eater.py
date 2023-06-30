from req.Helpers.base_req import BaseReq


class LogEater(BaseReq):

    def log_eater_audit_users_days_get(self):
        """process GET req http handler for getting path to file with user audit logs for "days" days count"""
        days = "1"
        header = {'token': self.token}
        resp = self.sess.get(f"{self.host}/back/dp.log_eater/audit/users/{days}", headers=header, verify=False)
        return resp
