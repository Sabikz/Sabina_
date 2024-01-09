from extends.api import Api
import requests


class ApiPreliminarySchedule(Api):
    def preliminary_schedule(self):

        data = {
            "amount": 0,
            "commission": 0,
            "insurance": 0,
            "issueDate": "string",
            "payAmount": 0,
            "payMethod": 0,
            "paysPeryear": 0,
            "principalPayKind": 0,
            "principalPayNum": 0,
            "rate": 0,
            "term": 0
        }
        response = requests.post(f"{self.host}/api/pfact/datahandler/preliminarySchedule", headers=self.headers_type,
                                 verify=False, json=data)
