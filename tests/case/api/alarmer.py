from req.Helpers.user_session import UserSession
from req.Api.req_alarmer import Alarmer
from resourses.constants import QA_SPAM_EMAIL, API_AUTO_TEST_


class AlarmerCase(UserSession):

    def case_alarmer_alert_service_names_get(self):
        req = Alarmer(self.sess, self.host)
        resp = req.alarmer_alert_service_names_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # todo: front:? use data
    def case_alarmer_email_server_post(self):
        req = Alarmer(self.sess, self.host)

        data = {
            "email": "string",
            "id": 0,
            "last_date": "string",
            "message_id": "string"
        }
        resp = req.alarmer_email_server_post(data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_email_server_get(self):
        req = Alarmer(self.sess, self.host)
        resp = req.alarmer_email_server_get()
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_email_server_id_get(self):
        req = Alarmer(self.sess, self.host)

        # ?receiver_id, получить можно из alarmer_email_server_get
        magic_id = 1

        resp = req.alarmer_email_server_id_get(magic_id)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    # look: возвращает 200 при любом _id, это не ок
    def case_alarmer_email_server_id_delete(self):
        req = Alarmer(self.sess, self.host)

        # ?receiver_id, получить можно из alarmer_email_server_get
        magic_id = 1

        resp = req.alarmer_email_server_id_delete(magic_id)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_notification_admin_all_get(self):
        req = Alarmer(self.sess, self.host)

        resp = req.alarmer_notification_admin_all_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_read_admin_get(self):
        req = Alarmer(self.sess, self.host)

        resp = req.alarmer_notification_read_admin_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_read_type_admin_post(self):
        req = Alarmer(self.sess, self.host)

        _type = "admin"     # todo: admin|user
        body = {
            "id": 5590483   # FIXME: magic?
        }
        resp = req.alarmer_notification_read_type_post(_type, body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_settings_admin_get(self):
        req = Alarmer(self.sess, self.host)

        resp = req.alarmer_notification_settings_admin_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_settings_common_get(self):
        req = Alarmer(self.sess, self.host)

        resp = req.alarmer_notification_settings_common_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_settings_common_post(self):
        req = Alarmer(self.sess, self.host)

        body = {
            "get_sys_notify": True,
            "notify_duration": 1
        }
        resp = req.alarmer_notification_settings_common_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_settings_user_get(self):
        req = Alarmer(self.sess, self.host)

        resp = req.alarmer_notification_settings_user_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_settings_userone_post(self):
        req = Alarmer(self.sess, self.host)

        body = {
            "object_id": 1,
            "type": 1,
            "user_id": 1
        }
        resp = req.alarmer_notification_settings_userone_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_settings_type_post(self):
        req = Alarmer(self.sess, self.host)

        _type = "user"
        body = {
            "data": None    # TODO: add any data
        }
        resp = req.alarmer_notification_settings_type_post(_type, body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_settings_user_all_get(self):
        req = Alarmer(self.sess, self.host)

        resp = req.alarmer_notification_settings_user_all_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_user_get(self):
        req = Alarmer(self.sess, self.host)

        _type = "user"      # TODO: user|admin
        resp = req.alarmer_notification_type_get(_type)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp

    def case_alarmer_notification_type_read_post(self):
        req = Alarmer(self.sess, self.host)

        _type = "list"      # TODO: list|all

        data = {
            "admin": [
                0
            ],
            "user": [
                0
            ]
        }
        resp = req.alarmer_notification_type_read_post(_type, data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_notifications_page_size_x_read_notify_type_page_x_get(self):
        req = Alarmer(self.sess, self.host)

        page_size = 1
        notify_type = "all"  # todo: all|warning|error|announcement
        page = 1    # page id

        resp = req.alarmer_notifications_page_size_x_read_notify_type_page_x_get(page_size, notify_type, page)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_send_invitation_post(self):
        # "user_id" > DAT-5291
        req = Alarmer(self.sess, self.host)

        body = {
            "to": QA_SPAM_EMAIL,
        }
        resp = req.alarmer_send_invitation_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_send_invitations_post(self):
        # DAT-5291
        req = Alarmer(self.sess, self.host)

        body = {
            "to": [
                QA_SPAM_EMAIL
            ],
            # "user_id": 4870
        }
        resp = req.alarmer_send_invitations_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_send_msg_post(self):
        req = Alarmer(self.sess, self.host)

        body = {
            "topic": API_AUTO_TEST_ + "topic",
            "message": API_AUTO_TEST_ + "message",
            "name": API_AUTO_TEST_ + "name",
            "description": API_AUTO_TEST_ + "alarmer_desc",
            "disable_tls": False,
            "host": "NGR-Exchange01.ngrsoftlab.ru",
            "port": 587,
            "protocol": "smpt",
            "to": QA_SPAM_EMAIL,
            # "send_user": DpQaa.USER,
            "send_user": "Владимир Даль",   # ??: Имя отправителя в полученном сообщении
            "psw": self._password,          # пароль для аунтефикации
            "user": self.username           # имя для аунтефикации
        }
        resp = req.alarmer_send_msg_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

        # print(resp.text)
        return resp
