from req.Helpers.base_req import BaseReq


class DatapieBaker(BaseReq):

    def datapie_baker_model_get(self):
        """process GET req for getting all models"""
        return self.sess.get(f"{self.host}/back/dp.datapie_baker/model")

    def datapie_baker_model_post(self, post_data):
        """process POST req for creating model"""
        return self.sess.post(f"{self.host}/back/dp.datapie_baker/model", json=post_data)

    def datapie_baker_model_case_get(self):
        """process GET req for getting model-case list sorted by model_id, case name, case app"""
        return self.sess.get(f"{self.host}/back/dp.datapie_baker/model/case")

    def datapie_baker_model_case_post(self, post_data):
        """process POST req for creating model case"""
        return self.sess.post(f"{self.host}/back/dp.datapie_baker/model/case", json=post_data)

    def datapie_baker_model_case_play_post(self, post_data):
        """process GET req for playing model case (manual execution)"""
        return self.sess.post(f"{self.host}/back/dp.datapie_baker/model/case/play", json=post_data)

    def datapie_baker_model_case_usage_id_delete(self, id_):
        """process DELETE req for deleting model case usage by id"""
        return self.sess.delete(f"{self.host}/back/dp.datapie_baker/model/case/usage/{id_}")

    def datapie_baker_model_case_id_delete(self, id_):
        """process DELETE req for deleting model case by id"""
        return self.sess.delete(f"{self.host}/back/dp.datapie_baker/model/case/{id_}")

    def datapie_baker_model_case_id_settings_get(self, id_):
        """process GET req for getting model-case settings list by case id"""
        return self.sess.get(f"{self.host}/back/dp.datapie_baker/model/case/{id_}/settings")

    def datapie_baker_model_case_id_usage_get(self, id_):
        """process GET req for getting list of case usages on tables by case id"""
        return self.sess.get(f"{self.host}/back/dp.datapie_baker/model/case/{id_}/usage")

    def datapie_baker_model_case_id_auto_post(self, id_, auto, post_data):
        """process POST req for setting model case auto-use flag"""
        return self.sess.post(f"{self.host}/back/dp.datapie_baker/model/case/{id_}/{auto}", json=post_data)

    def datapie_baker_model_id_get(self, id_):
        """process GET req for getting model info by model id"""
        return self.sess.get(f"{self.host}/back/dp.datapie_baker/model/{id_}")

    def datapie_baker_model_id_delete(self, id_):
        """process DELETE req for deleting model by id"""
        return self.sess.delete(f"{self.host}/back/dp.datapie_baker/model/{id_}")

    def datapie_baker_model_id_case_id_match_get(self, model_id, case_id):
        """process GET req for getting list of case-table matches (not used) by model id and case id"""
        return self.sess.get(f"{self.host}/back/dp.datapie_baker/model/{model_id}/case/{case_id}/match")
