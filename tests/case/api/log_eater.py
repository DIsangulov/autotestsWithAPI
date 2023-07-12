from req.Helpers.user_session import UserSession
from req.Api.req_log_eater import LogEater


class LogEaterCase(UserSession):

    def case_log_eater_audit_users_days_get(self):
        req = LogEater(self.sess, self.host)

        days = "1"
        resp = req.log_eater_audit_users_days_get(days)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)
