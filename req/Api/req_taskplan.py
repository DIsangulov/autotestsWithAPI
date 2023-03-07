from req.Helpers.base_req import BaseReq


class Taskplan(BaseReq):

    def taskplan_get_shedule_post(self, token):
        header = {'token': token, 'ui': str(2)}
        data = {
            "sched_type": "script_exec",
            "timezone": "Europe/Moscow",
            "data": {
                "object_id": 25
            }
        }
        resp = self.sess.post(f"{self.host}/back/dp.taskplan/get_schedule", headers=header, json=data, verify=False)
        return resp

    def taskplan_tasks_post(self, token):
        header = {'token': token, 'ui': str(2)}
        data = {"additionalProp1": {"sched_type": "alarm"}}
        resp = self.sess.post(f"{self.host}/back/dp.taskplan/tasks", headers=header, json=data, verify=False)
        return resp
