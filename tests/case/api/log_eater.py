from req.Helpers.base_req import BaseReq
from req.Api.req_log_eater import LogEater


class LogEaterCase(BaseReq):

    def case_log_eater_audit_users_days_get(self):
        req = LogEater(self.sess, self.host)

        days = "1"
        resp = req.log_eater_audit_users_days_get(days)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)
