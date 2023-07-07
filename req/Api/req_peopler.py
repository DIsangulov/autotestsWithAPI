import requests

from req.Helpers.base_req_raw import BaseReqRaw


class Peopler(BaseReqRaw):

    def peopler_mainpage_get(self) -> requests.Response:
        """process GET req to get pinned main page for user"""
        return self.sess.get(f"{self.host}/back/dp.peopler/mainpage")

    def peopler_many_users_put(self, body) -> requests.Response:
        """process PUT req for editing many users (edit roles)"""
        return self.sess.put(f"{self.host}/back/dp.peopler/many_users", json=body)

    def peopler_many_users_post(self, body) -> requests.Response:
        """process POST req for creating many users"""
        return self.sess.post(f"{self.host}/back/dp.peopler/many_users", json=body)

    # TODO: [POST] /back/dp.peopler/pin_page/current_user

    # TODO: [DELETE] /back/dp.peopler/pin_page/current_user

    # TODO: [POST] /back/dp.peopler/pin_page/list/{type_subject}

    # TODO: [POST] /back/dp.peopler/pin_page/{type_subject}

    # TODO: [DELETE] /back/dp.peopler/pin_page/{type_subject}/{id}

    # TODO: [POST] /back/dp.peopler/pinned_page_status

    def peopler_profile_get(self) -> requests.Response:
        """process GET req for getting user profile by token"""
        return self.sess.get(f"{self.host}/back/dp.peopler/profile")

    def peopler_profiles_get(self) -> requests.Response:
        """process GET req for getting user profiles"""
        return self.sess.get(f"{self.host}/back/dp.peopler/profiles")

    def peopler_users_get(self) -> requests.Response:
        """Получить список пользователей"""
        return self.sess.get(f"{self.host}/back/dp.peopler/users")

    def peopler_users_post(self, body) -> requests.Response:
        """Создание нового '@доменного' пользователя"""
        return self.sess.post(f"{self.host}/back/dp.peopler/users", json=body)

    def peopler_users_id_get(self, user_id) -> requests.Response:
        """Получить информацию пользователя по **ID**"""
        return self.sess.get(f"{self.host}/back/dp.peopler/users/{user_id}")

    def peopler_users_id_put(self, user_id: int, body: dict) -> requests.Response:
        """process PUT req for editing user by id"""
        return self.sess.put(f"{self.host}/back/dp.peopler/users/{user_id}", json=body)

    def peopler_users_id_delete(self, user_id) -> requests.Response:
        """Удалить пользователя по **ID**"""
        return self.sess.delete(f"{self.host}/back/dp.peopler/users/{user_id}")
