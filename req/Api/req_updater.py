from req.Helpers.base_req import BaseReq


class Updater(BaseReq):

    def updater_additions_get(self):
        """process GET req to get list of available additions"""
        return self.sess.get(f"{self.host}/back/dp.updater/additions")

    def updater_additions_addition_post(self, addition):
        """process POST req to install addition"""
        return self.sess.post(f"{self.host}/back/dp.updater/additions/{addition}")

    def updater_additions_addition_delete(self, addition):
        """process DELETE req to delete addition data (if user has access to addition database)"""
        return self.sess.delete(f"{self.host}/back/dp.updater/additions/{addition}")

    def updater_check_updates_get(self):
        """process GET req to get info 'product can be updated'"""
        return self.sess.get(f"{self.host}/back/dp.updater/check_updates")

    # TODO: def [POST] /back/dp.updater/update

    # TODO: def [POST] /back/dp.updater/update_from_archive

    # TODO new: /back/dp.updater/versions   # https://tasks.ngrsoftlab.ru/browse/DAT-5287
