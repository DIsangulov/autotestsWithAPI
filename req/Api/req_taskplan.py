from req.Helpers.base_req import BaseReq


class Taskplan(BaseReq):

    def taskplan_get_shedule_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {
            "sched_type": "script_exec",
            "timezone": "Europe/Moscow",
            "data": {
                "object_id": 1902
            }
        }

        # {"sched_type":"mailing","timezone":"Europe/Moscow","data":{"object_id":426}}

        resp = self.sess.post(f"{self.host}/back/dp.taskplan/get_schedule", headers=header, json=data, verify=False)
        return resp

    def taskplan_tasks_post(self):
        header = {'token': self.token, 'ui': str(2)}
        data = {"additionalProp1": {"sched_type": "alarm"}}
        resp = self.sess.post(f"{self.host}/back/dp.taskplan/tasks", headers=header, json=data, verify=False)
        return resp

    # add this >>
    # dp.taskplan/add_task      # создание рассылки из отчета
    # {"sched_type": "mailing", "object_id": 426, "schedule": {"sched_id": 0, "flag": 3, "timezone": "Europe/Moscow", "interval": {"val": "30", "str": "min"}, "day": {"val": "", "hhmm": "00:00"}, "week": {"days": null, "hhmm": "00:00"}, "month": {"var": 0, "day": "1", "val": "2", "val2": "", "wday": "", "wnum": "", "hhmm": "00:00"}}, "timezone": "Europe/Moscow"}

    # dp.taskplan/delete_task
