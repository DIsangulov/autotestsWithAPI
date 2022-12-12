import json
import pytest
import requests
import urllib3
from self import self

from req.Api.req_auth import AuthApi
from req.Helpers.base_req import BaseReq
from req.Api.req_absorber import Absorber
from req.Api.req_alarmer import Alarmer

urllib3.disable_warnings()
# ________Constants________
sess = requests.Session()
host = "https://10.130.0.22"
# ________Constants________

# _________Globals_________
auth_token = None
uid = None


# _________Globals_________

@pytest.mark.skip
class TestAuth:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']

    def test_ad_struct(self):
        req = AuthApi(sess, host)
        resp = req.ad_struct(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_ou_users(self):
        req = AuthApi(sess, host)
        resp = req.ou_users(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions(self):
        req = AuthApi(sess, host)
        resp = req.sessions(auth_token)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions_uid(self):
        req = AuthApi(sess, host)
        resp = req.sessions_uid(auth_token)

        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions_one_sid_del(self):  # sid вкорячен в req_auth в метод sessions_one_sid_del
        req = AuthApi(sess, host)
        resp = req.sessions_one_sid_del(auth_token)
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_sessions_all_uid_del(self):
        self.test_get_token()
        req = AuthApi(sess, host)
        resp = req.sessions_all_uid_del(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # __________________________________LOGOUT_______________________________________

    def test_logout(self):
        self.test_get_token()
        req = AuthApi(sess, host)
        resp = req.sessions(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # __________________________________ABSORBER_______________________________________


@pytest.mark.skip
class TestAbsorber:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']
        print(auth_token)

    def test_library_columns(self):
        req = Absorber(sess, host)
        resp = req.library_columns(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_conn_type(self):
        req = Absorber(sess, host)
        resp = req.library_conn_type(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_conn_type_id(self):
        req = Absorber(sess, host)
        resp = req.library_conn_type_id(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_connector(self):  # получаем список всех коннекторов
        req = Absorber(sess, host)
        resp = req.library_connector(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_connector_post(self):
        req = Absorber(sess, host)
        resp = req.library_connector_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_connector_put(self):
        req = Absorber(sess, host)
        resp = req.library_connector_put(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_connector_get(self):
        req = Absorber(sess, host)
        resp = req.library_connector_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_connector_delete(self):
        req = Absorber(sess, host)
        resp = req.library_connector_delete(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_logo_get(self):
        req = Absorber(sess, host)
        resp = req.library_logo_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_logo_post(self):
        req = Absorber(sess, host)
        resp = req.library_logo_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_logo_put(self):
        req = Absorber(sess, host)
        resp = req.library_logo_put(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_library_logo_delete(self):
        req = Absorber(sess, host)
        resp = req.library_logo_delete(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_source_get(self):
        req = Absorber(sess, host)
        resp = req.source_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_source_post(self):  # тут какая-то задница
        req = Absorber(sess, host)
        resp = req.source_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"


class TestAlarmer:

    def test_get_token(self):
        req = BaseReq(sess, host)
        resp = req.auth()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        dct = json.loads(resp.text)
        global auth_token
        auth_token = dct['token']
        print(auth_token)

    def test_alarmer_notification_admin_all(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_admin_all(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_read_admin(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_admin_all(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_read_type_admin(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_read_type_user(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_admin(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_settings_admin(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_common_get(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_settings_common_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_common_post(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_settings_common_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_user_get(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_settings_user_get(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_userone_post(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_settings_userone_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_settings_type_post(self): # проблемный
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_settings_type_post(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_user_all(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_settings_user_all(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def test_alarmer_notification_user(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_notification_user(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_alarmer_send_invitation(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_send_invitation(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_alarmer_send_invitations(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_send_invitations(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    @pytest.mark.skip
    def test_alarmer_send_msg(self):
        req = Alarmer(sess, host)
        resp = req.alarmer_send_msg(auth_token)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"