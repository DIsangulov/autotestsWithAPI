from req.Helpers.base_req import BaseReq


class Taskplan(BaseReq):

    # TODO: [POST] /back/dp.taskplan/add_task   # front: создание рассылки из отчета

    # TODO: [DELETE] /back/dp.taskplan/delete_task

    def taskplan_get_shedule_post(self, data):
        """process POST req to get schedule info for object"""
        return self.sess.post(f"{self.host}/back/dp.taskplan/get_schedule", json=data)
