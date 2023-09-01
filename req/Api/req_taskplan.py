from req.Helpers.base_req import BaseReq


class Taskplan(BaseReq):

    def taskplan_add_task_post(self, data):
        """process POST req to add new task"""
        return self.sess.post(f"{self.host}/back/dp.taskplan/add_task", json=data)

    def taskplan_delete_task(self, data):
        """process DELETE req to delete task"""
        return self.sess.post(f"{self.host}/back/dp.taskplan/delete_task", json=data)

    def taskplan_get_shedule_post(self, data):
        """process POST req to get schedule info for object"""
        return self.sess.post(f"{self.host}/back/dp.taskplan/get_schedule", json=data)
