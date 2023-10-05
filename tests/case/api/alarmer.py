from req.Helpers.user_session import UserSession
from req.Api.req_alarmer import Alarmer
from resourses.constants import QA_SPAM_EMAIL, API_AUTO_TEST_
from tests.case.api.core import MAIL_USER, MAIL_PASS, MAIL_HOST, MAIL_PORT
from resourses.static_methods import get_datetime_now_z


class AlarmerCase(UserSession):

    def case_alarmer_alert_service_names_get(self):
        req = Alarmer(self.sess, self.host)
        resp = req.alarmer_alert_service_names_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_email_server_post(self):
        req = Alarmer(self.sess, self.host)

        data = {
            "email": "string",
            "id": 0,
            "last_date": get_datetime_now_z(),
            "message_id": "string"
        }
        resp = req.alarmer_email_server_post(data)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_email_server_get(self):
        req = Alarmer(self.sess, self.host)
        resp = req.alarmer_email_server_get()
        print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_email_server_id_get(self):
        req = Alarmer(self.sess, self.host)

        # ?receiver_id, получить можно из alarmer_email_server_get
        magic_id = 1

        resp = req.alarmer_email_server_id_get(magic_id)
        # print(resp.text)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

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

    def case_alarmer_notification_read_admin_get(self):
        req = Alarmer(self.sess, self.host)
        resp = req.alarmer_notification_read_admin_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_notification_read_type_admin_post(self):
        req = Alarmer(self.sess, self.host)

        _type = "admin"     # todo: admin|user
        body = {
            "id": 5590483   # FIXME: magic?
        }
        resp = req.alarmer_notification_read_type_post(_type, body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_notification_settings_admin_get(self):
        # front: >^.Настройки уведомлений
        req = Alarmer(self.sess, self.host)
        resp = req.alarmer_notification_settings_admin_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_notification_settings_common_get(self):
        req = Alarmer(self.sess, self.host)
        resp = req.alarmer_notification_settings_common_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_notification_settings_common_post(self):
        req = Alarmer(self.sess, self.host)
        body = {
            "get_sys_notify": True,
            "notify_duration": 1
        }
        resp = req.alarmer_notification_settings_common_post(body)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_notification_settings_user_get(self):
        req = Alarmer(self.sess, self.host)
        resp = req.alarmer_notification_settings_user_get()
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

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
        # изменение настроек уведомлений
        req = Alarmer(self.sess, self.host)

        _type = "user"
        body = {
            "data": None    # TODO: add any data # сначала гет дату, потом докидывать?
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

    def case_alarmer_notification_type_get(self, notification_type: str):
        req = Alarmer(self.sess, self.host)
        resp = req.alarmer_notification_type_get(notification_type)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_notification_type_read_post(self, read_type):
        # >^. Раскрыть ленту уведомлений
        # ../list/read - при прокрутке ленты, в data: попадают id уведомлений
        # ../all/read - клик "Прочитать все", в data: {"admin":[],"user":[]}
        req = Alarmer(self.sess, self.host)

        post_data = {"admin": [], "user": []}
        # todo: if read_type == "list" >> update data

        resp = req.alarmer_notification_type_read_post(read_type, post_data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"

    def case_alarmer_notifications_page_size_x_read_notify_type_page_x_get(self, notify_type: str):
        # front: раскрытие ленты уведомлений
        req = Alarmer(self.sess, self.host)

        page_size = 1
        page = 1    # page id

        resp = req.alarmer_notifications_page_size_x_read_notify_type_page_x_get(page_size, notify_type, page)
        # print(resp.text)
        assert resp.status_code == 200, \
            f"""Ошибка, 
            page_size: {page_size}
            notify_type: {notify_type}
            page: {page}
            status_code {resp.status_code}
            resp: {resp.text}
            """

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

        data = {
            "user": MAIL_USER,
            "send_user": "Владимир Даль",   # ??: Имя отправителя в полученном сообщении
            "psw": MAIL_PASS,
            "host": MAIL_HOST,
            "port": MAIL_PORT,
            "protocol": "smpt",
            "disable_tls": False,

            "to": QA_SPAM_EMAIL,
            "topic": API_AUTO_TEST_ + "alarmer_topic",
            "message": API_AUTO_TEST_ + "alarmer_message",
            "name": API_AUTO_TEST_ + "alarmer_name",
            "description": API_AUTO_TEST_ + "alarmer_description"
        }

        resp = req.alarmer_send_msg_post(data)
        assert resp.status_code == 200, f"Ошибка, post_data: {data}, status_code: {resp.status_code}, resp: {resp.text}"
