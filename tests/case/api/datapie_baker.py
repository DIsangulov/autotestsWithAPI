from req.Helpers.user_session import UserSession
from req.Api.req_datapie_baker import DatapieBaker


class DatapieBakerCase(UserSession):

    def case_datapie_baker_model_get(self):
        req = DatapieBaker(self.sess, self.host)
        resp = req.datapie_baker_model_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_datapie_baker_model_post(self):
        req = DatapieBaker(self.sess, self.host)

        post_data = {}
        resp = req.datapie_baker_model_post(post_data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_datapie_baker_model_case_get(self):
        req = DatapieBaker(self.sess, self.host)
        resp = req.datapie_baker_model_case_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_datapie_baker_model_case_post(self):
        req = DatapieBaker(self.sess, self.host)
        post_data = {}
        resp = req.datapie_baker_model_case_post(post_data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_datapie_baker_model_case_play_post(self):
        req = DatapieBaker(self.sess, self.host)
        post_data = {}
        resp = req.datapie_baker_model_case_play_post(post_data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_datapie_baker_model_case_usage_id_delete(self):
        req = DatapieBaker(self.sess, self.host)
        id_for_delete = None
        resp = req.datapie_baker_model_case_usage_id_delete(id_for_delete)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_datapie_baker_model_case_id_delete(self):
        req = DatapieBaker(self.sess, self.host)
        id_for_delete = None
        resp = req.datapie_baker_model_case_id_delete(id_for_delete)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_datapie_baker_model_case_id_settings_get(self):
        req = DatapieBaker(self.sess, self.host)
        case_id = None
        resp = req.datapie_baker_model_case_id_settings_get(case_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_datapie_baker_model_case_id_usage_get(self):
        req = DatapieBaker(self.sess, self.host)
        case_id = None
        resp = req.datapie_baker_model_case_id_usage_get(case_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_datapie_baker_model_case_id_auto_post(self):
        req = DatapieBaker(self.sess, self.host)
        case_id = None
        auto_flag = "off"   # on / off
        post_data = {}
        resp = req.datapie_baker_model_case_id_auto_post(case_id, auto_flag, post_data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_datapie_baker_model_id_get(self):
        req = DatapieBaker(self.sess, self.host)
        model_id = None
        resp = req.datapie_baker_model_id_get(model_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_datapie_baker_model_id_delete(self):
        req = DatapieBaker(self.sess, self.host)
        model_id = None
        resp = req.datapie_baker_model_id_delete(model_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_datapie_baker_model_id_case_id_match_get(self):
        req = DatapieBaker(self.sess, self.host)
        model_id = None
        case_id = None
        resp = req.datapie_baker_model_id_case_id_match_get(model_id, case_id)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
