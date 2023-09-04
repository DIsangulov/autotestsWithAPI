from req.Helpers.base_req import BaseReq


class Visualisation(BaseReq):

    def visualisation_query_get(self):
        """process GET req for getting query list"""
        # front: при создании визуализации > добавить серию > источник данных
        return self.sess.get(f"{self.host}/back/dp.visualisation/query")

    def visualisation_query_do_query_id_post(self, query_id, data):
        """process POST req with filters for executing query with id = query_id."""
        return self.sess.post(f"{self.host}/back/dp.visualisation/query/do/{query_id}", json=data)

    def visualisation_query_save_post(self, data):
        """process POST req for creating/editing query by id"""
        return self.sess.post(f"{self.host}/back/dp.visualisation/query/save", json=data)

    def visualisation_query_usage_id_get(self, query_id):
        """process GET req for getting query usage in visualisations by id"""
        return self.sess.get(f"{self.host}/back/dp.visualisation/query/usage/{query_id}")

    def visualisation_query_query_id_get(self, query_id):
        """process GET req for getting query by id"""
        return self.sess.get(f"{self.host}/back/dp.visualisation/query/{query_id}")

    def visualisation_query_id_delete(self, query_id):
        """process DELETE req for deleting query by id"""
        return self.sess.delete(f"{self.host}/back/dp.visualisation/query/{query_id}")

    def visualisation_reports_get(self):
        """process GET req for getting reports list"""
        return self.sess.get(f"{self.host}/back/dp.visualisation/reports")

    def visualisation_reports_post(self, data):
        """
        process POST req for creating/editing report by id
        updates if report id is present, creates new report otherwise
        """
        return self.sess.post(f"{self.host}/back/dp.visualisation/reports", json=data)

    def visualisation_reports_params_report_id_post(self, report_id, data):
        """process POST req for saving report params (for linked report)"""
        return self.sess.post(f"{self.host}/back/dp.visualisation/reports/params/{report_id}", json=data)

    def visualisation_reports_report_id_get(self, report_id):
        """process GET req for getting report by id"""
        return self.sess.get(f"{self.host}/back/dp.visualisation/reports/{report_id}")

    def visualisation_reports_report_id_delete(self, report_id):
        """process DELETE req for deleting report by id"""
        return self.sess.delete(f"{self.host}/back/dp.visualisation/reports/{report_id}")

    def visualisation_visualisation_get(self):
        """process GET req for getting visualisations list"""
        return self.sess.get(f"{self.host}/back/dp.visualisation/visualisation")

    def visualisation_visualisation_post(self, data):
        """process POST req for creating/editing visualisation by id"""
        return self.sess.post(f"{self.host}/back/dp.visualisation/visualisation", json=data)

    def visualisation_visualisation_dataseries_visualisation_id_post(self, visualisation_id, data):
        """
        process POST req for creating/editing dataseries in visualisation element
        updates if dataseries id is present, creates new dataseries otherwise
        """
        return self.sess.post(f"{self.host}/back/dp.visualisation/visualisation/dataseries/{visualisation_id}", json=data)

    def visualisation_visualisation_dataseries_visualisation_id_dataseries_id_delete(self, vis_id, dataseries_id, data):
        """process DELETE req for deleting dataseries (by id) from visualisation element"""
        return self.sess.delete(f"{self.host}/back/dp.visualisation/visualisation/dataseries/{vis_id}/{dataseries_id}", json=data)

    def visualisation_visualisation_types_get(self):
        """process GET req for getting visual elements type list"""
        # front: создание визуализации > добавить серию > тип элемента
        return self.sess.get(f"{self.host}/back/dp.visualisation/visualisation/types")

    def visualisation_visualisation_usage_visualisation_id_get(self, visualisation_id):
        """process GET req for getting visualisation usages in reports by id"""
        return self.sess.get(f"{self.host}/back/dp.visualisation/visualisation/usage/{visualisation_id}")

    def visualisation_visualisation_visualisation_id_get(self, visualisation_id):
        """process GET req for getting visualisation by id"""
        return self.sess.get(f"{self.host}/back/dp.visualisation/visualisation/{visualisation_id}")

    def visualisation_visualisation_visualisation_id_delete(self, visualisation_id):
        """process DELETE req for deleting visualisation by id"""
        return self.sess.delete(f"{self.host}/back/dp.visualisation/visualisation/{visualisation_id}")
