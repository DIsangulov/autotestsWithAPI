from req.Helpers.base_req import BaseReq


class Reporter(BaseReq):

    def reporter_mailing_get(self):
        """process GET req for getting all mailings from library"""
        # получение всех рассылок (*редактором которых является запросивший)
        return self.sess.get(f"{self.host}/back/dp.reporter/mailing")

    def reporter_mailing_put(self, data):
        """process PUT req for changing mailing"""
        return self.sess.put(f"{self.host}/back/dp.reporter/mailing", json=data)

    def reporter_mailing_post(self, data):
        """process POST req for adding new mailing"""
        # исп: создание рассылки из отчета
        # на фронте видны у того, кто является "автором" рассылки
        return self.sess.post(f"{self.host}/back/dp.reporter/mailing", json=data)

    def reporter_mailing_sample_post(self, data):
        """process POST req for getting mailing data sample from storage"""
        # исп: "Отправить тестовое письмо себе"
        return self.sess.post(f"{self.host}/back/dp.reporter/mailing/sample", json=data)

    def reporter_mailing_typed_type_get(self, _type):
        """process GET req for getting types mailings from library"""
        return self.sess.get(f"{self.host}/back/dp.reporter/mailing/typed/{_type}")

    def reporter_mailing_id_get(self, mailing_id):
        """process GET req for getting mailing by id"""
        return self.sess.get(f"{self.host}/back/dp.reporter/mailing/{mailing_id}")

    def reporter_mailing_id_delete(self, mailing_id):
        """process DELETE req for deleting mailing"""
        # исп: удалить рассылку
        return self.sess.delete(f"{self.host}/back/dp.reporter/mailing/{mailing_id}")

    def reporter_screener_fast_post(self, data):
        # https://tasks.ngrsoftlab.ru/browse/DAT-4983
        """process POST req for getting fast page screenshot"""
        return self.sess.post(f"{self.host}/back/dp.reporter/screener/fast", json=data)
