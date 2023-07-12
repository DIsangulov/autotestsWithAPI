from req.Helpers.user_session import UserSession
from req.Api.req_updater import Updater


class UpdaterCase(UserSession):

    def case_updater_additions_get(self):
        req = Updater(self.sess, self.host)
        resp = req.updater_additions_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    # TODO: check 200 or 400
    def case_updater_additions_addition_post(self):
        req = Updater(self.sess, self.host)
        addition = "geo_ip"     # FIXME: какие ещё есть? << updater_additions_get
        resp = req.updater_additions_addition_post(addition)
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    # TODO: check 200 or 400
    # fixme: {"error":{"code":403,"description":"no access to geo_ip database","msg":"Запрещено"}}
    def case_updater_additions_addition_delete(self):
        req = Updater(self.sess, self.host)
        addition = "geo_ip"
        resp = req.updater_additions_addition_delete(addition)
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)

    # TODO: check 200 or 400
    def case_updater_check_updates_get(self):
        req = Updater(self.sess, self.host)
        resp = req.updater_check_updates_get()
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)


