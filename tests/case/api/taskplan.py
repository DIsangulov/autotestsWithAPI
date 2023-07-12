from req.Helpers.user_session import UserSession
from req.Api.req_taskplan import Taskplan


class TaskplanCase(UserSession):

    # [post] /add_task
    # {"sched_type": "mailing", "object_id": 426, "schedule": {"sched_id": 0, "flag": 3, "timezone": "Europe/Moscow", "interval": {"val": "30", "str": "hour"}, "day": {"val": "", "hhmm": "00:00"}, "week": {"days": null, "hhmm": "00:00"}, "month": {"var": 0, "day": "1", "val": "2", "val2": "", "wday": "", "wnum": "", "hhmm": "00:00"}}, "timezone": "Europe/Moscow"}

    def case_taskplan_get_shedule_post(self):
        req = Taskplan(self.sess, self.host)
        req.sess.headers.update({'ui': "2"})
        # data = {
        #     "sched_type": "script_exec",
        #     "timezone": "Europe/Moscow",
        #     "data": {
        #         "object_id": 1902
        #     }
        # }
        data = {
            "sched_type": "mailing",
            "timezone": "Europe/Moscow",
            # FIXME: нужна существующая рассылка с установленным расписанием
            # add_task <<<<
            "data": {"object_id":    483}
        }

        resp = req.taskplan_get_shedule_post(data)
        assert resp.status_code == 200, f"Ошибка, код {resp.status_code}, {resp.text}"
        # print(resp.text)
