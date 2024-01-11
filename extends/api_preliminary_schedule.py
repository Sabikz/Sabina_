from extends.api import Api
import requests


class ApiPreliminarySchedule(Api):
    def preliminary_schedule(self):

        data = {
            "amount": 1,
            "commission": 1,
            "insurance": 1,
            "issueDate": "string",
            "payAmount": 1,
            "payMethod": 1,
            "paysPeryear": 1,
            "principalPayKind": 1,
            "principalPayNum": 1,
            "rate": 1,
            "term": 1
        }
        response = requests.post(f"{self.host}/api/pfact/datahandler/preliminarySchedule", headers=self.headers_type,
                                 verify=False, json=data)
        return response