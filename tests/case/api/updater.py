import json

from req.Helpers.user_session import UserSession
from req.Api.req_updater import Updater


componentsNames = [
    "registry-dp",
    "dp_xba_py",
    "dp_xba_cook",
    "dp_visualisation",
    "dp_updater",
    "dp_taskplan",
    "dp_storage_worker",
    "dp_scripter",
    "dp_rm_ml",
    "dp_rm_cook",
    "dp_reporter",
    "dp_postgres_single",
    "dp_permitter",
    "dp_peopler",
    "dp_monitor",
    "dp_log_eater",
    "dp_licenser",
    "dp_frontend",
    "dp_elements_eater",
    "dp_datapie_baker",
    "dp_core",
    "dp_auth",
    "dp_absorber",
    # "dp_picker-0",
    # "dp_storage_single-0",
    # "dp_postgres_single-0",
    # "dp_ml-0",
]


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
        # DAT-5287  # DAT-5933
        req = Updater(self.sess, self.host)
        resp = req.updater_versions_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        _full_assertion_message = []
        result_list = json.loads(resp.text)['res']

        info_box_num = 0
        for info_box in result_list:
            # В каждом результате 'res': есть приведенные в списке поля:
            check_fields = ["name", "version", "state", "build_id"]
            for _field in check_fields:
                if _field not in info_box:
                    _full_assertion_message.append(f"\n'res'[{info_box_num}]: {info_box} doesn't have field '{_field}'")
            info_box_num += 1

        for cn in componentsNames:
            # Все перечисленные компоненты есть в ответе
            check = next((info_box for info_box in result_list if info_box['name'] == cn), None)
            if check is None:
                _full_assertion_message.append(f"\nThere is no component info for: '{cn}'")

        assert len(_full_assertion_message) == 0, "".join(_full_assertion_message) + \
                                                  f"\ncode: {resp.status_code}" + \
                                                  f"\nresp: {resp.text}"
