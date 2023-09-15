import json

from req.Helpers.user_session import UserSession
from req.Api.req_updater import Updater


class UpdaterCase(UserSession):

    def case_updater_additions_get(self):
        req = Updater(self.sess, self.host)
        resp = req.updater_additions_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # TODO: check 200 or 400
    def case_updater_additions_addition_post(self):
        req = Updater(self.sess, self.host)
        addition = "geo_ip"     # geo_ip|rm_demo|xba_demo
        resp = req.updater_additions_addition_post(addition)
        # print(resp.text)
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"

    # TODO: check 200 or 400
    def case_updater_additions_addition_delete(self):
        req = Updater(self.sess, self.host)
        addition = "geo_ip"     # geo_ip|rm_demo|xba_demo
        resp = req.updater_additions_addition_delete(addition)
        # print(resp.text)
        assert resp.status_code == 200 or 400, f"Ошибка, код {resp.status_code}, {resp.text}"
        # # 400: {"error":{"code":403,"description":"no access to geo_ip database","msg":"Запрещено"}}

    def case_updater_check_updates_get(self):
        req = Updater(self.sess, self.host)
        resp = req.updater_check_updates_get()
        # print(resp.text)
        assert resp.status_code == 200, f"2.Ошибка, код {resp.status_code}, {resp.text}"
        # 200: {"res":[{"current_version":"1.9.0","new_version":"1.9.1"}]}

        resp_data: dict = json.loads(resp.text)['res'][0]
        resp_data_keys = resp_data.keys()

        key_to_check = "current_version"
        assert key_to_check in resp_data_keys, f"1.Ошибка, отсутствует ключ '{key_to_check}' в ответе: {resp.text}"

        key_to_check = "new_version"
        assert key_to_check in resp_data_keys, f"0.Ошибка, отсутствует ключ '{key_to_check}' в ответе: {resp.text}"

    def case_updater_update_post(self):
        req = Updater(self.sess, self.host)
        data = {}
        resp = req.updater_update_post(data)
        assert False

    def case_updater_update_from_archive_post(self):
        req = Updater(self.sess, self.host)
        data = {}
        resp = req.updater_update_from_archive_post(data)
        assert False

    def case_updater_versions_get(self):
        # DAT-5287
        req = Updater(self.sess, self.host)
        resp = req.updater_versions_get()
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
