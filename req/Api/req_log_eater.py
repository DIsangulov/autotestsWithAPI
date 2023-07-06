import requests

from req.Helpers.base_req_raw import BaseReqRaw


class LogEater(BaseReqRaw):

    def log_eater_audit_users_days_get(self, days) -> requests.Response:
        """process GET req http handler for getting path to file with user audit logs for "days" days count"""
        return self.sess.get(f"{self.host}/back/dp.log_eater/audit/users/{days}")
