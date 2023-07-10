import requests

from req.Helpers.base_req_raw import BaseReqRaw


class Absorber(BaseReqRaw):

    def absorber_library_columns_get(self) -> requests.Response:
        """process GET req for getting all columns dict elements from library"""
        return self.sess.get(f"{self.host}/back/dp.absorber/library/columns")

    def absorber_library_conn_type_get(self) -> requests.Response:
        """process GET req for getting all conn types from library"""
        return self.sess.get(f"{self.host}/back/dp.absorber/library/conn_type")

    def absorber_library_conn_type_id_get(self, conn_type_id) -> requests.Response:
        """process GET req for getting conn types from library by id"""
        return self.sess.get(f"{self.host}/back/dp.absorber/library/conn_type/{conn_type_id}")

    def absorber_library_connector_get(self) -> requests.Response:
        """process GET req for getting all сonnectors from library"""
        # front: перейти в библиотеку шаблонов (/library/connectors)
        return self.sess.get(f"{self.host}/back/dp.absorber/library/connector")

    def absorber_library_connector_put(self, data) -> requests.Response:
        """process PUT req for changing сonnector"""
        return self.sess.put(f"{self.host}/back/dp.absorber/library/connector", json=data)

    def absorber_library_connector_post(self, data) -> requests.Response:
        """process POST req for adding new сonnector"""
        return self.sess.post(f"{self.host}/back/dp.absorber/library/connector", json=data)

    def absorber_library_connector_id_get(self, con_id) -> requests.Response:
        """process GET req for getting сonnector by id"""
        return self.sess.get(f"{self.host}/back/dp.absorber/library/connector/{con_id}")

    def absorber_library_connector_id_delete(self, con_id) -> requests.Response:
        """process DELETE req for deleting сonnector"""
        return self.sess.delete(f"{self.host}/back/dp.absorber/library/connector/{con_id}")

    def absorber_library_external_type_post(self, _type, file):
        """process POST req for importing external file with driver or parsing patterns"""
        return self.sess.post(f"{self.host}/back/dp.absorber/library/external/{_type}", files=file)

    def absorber_library_logo_get(self) -> requests.Response:
        """process GET req for getting all logos from library"""
        return self.sess.get(f"{self.host}/back/dp.absorber/library/logo")

    def absorber_library_logo_put(self, data) -> requests.Response:
        """process PUT req for changing logo"""
        return self.sess.put(f"{self.host}/back/dp.absorber/library/logo", json=data)

    def absorber_library_logo_post(self, data) -> requests.Response:
        """process POST req for new logo addition"""
        return self.sess.post(f"{self.host}/back/dp.absorber/library/logo", json=data)

    def absorber_library_logo_id_get(self, logo_id):
        """process GET req for getting logo by id"""
        return self.sess.get(f"{self.host}/back/dp.absorber/library/logo/{logo_id}")

    def absorber_library_logo_delete(self, _logo_id) -> requests.Response:
        """process DELETE req for deleting logo"""
        return self.sess.delete(f"{self.host}/back/dp.absorber/library/logo/{_logo_id}")

    def absorber_source_get(self) -> requests.Response:
        """process GET req for getting all sources from library"""
        return self.sess.get(f"{self.host}/back/dp.absorber/source")

    def absorber_source_put(self, data) -> requests.Response:
        """process PUT req for changing source"""
        return self.sess.put(f"{self.host}/back/dp.absorber/source", json=data)

    def absorber_source_post(self, data) -> requests.Response:
        """process POST req for adding new source"""
        return self.sess.post(f"{self.host}/back/dp.absorber/source", json=data)

    def absorber_source_id_get(self, _source_id) -> requests.Response:
        """process GET req for getting source by id"""
        return self.sess.get(f"{self.host}/back/dp.absorber/source/{_source_id}")

    def absorber_source_id_delete(self, _source_id) -> requests.Response:
        """process DELETE req for deleting source"""
        return self.sess.delete(f"{self.host}/back/dp.absorber/source/{_source_id}")

    def absorber_source_id_debug_get(self, _source_id) -> requests.Response:
        """process GET req for getting source debug info (last action.RowLimitFromDebugFile/N(later) strings from debug file) by id"""
        return self.sess.get(f"{self.host}/back/dp.absorber/source/{_source_id}/debug")
