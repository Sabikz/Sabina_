from extends.api import Api
import requests


class ApiProductRate(Api):
    def product_rate(self):

        data = {
            "clientPromotion": 12,
            "commisionMark": 1,
            "creditIssueDate": "string",
            "creditPromotion": 12,
            "creditSum": 5000000.5,
            "creditTerm": 12,
            "firmId": 1,
            "insurance": 250000,
            "lineRate": 30.5,
            "lineSum": 5000000.5,
            "lineTerm": 12,
            "productId": 12
        }
        response = requests.post(f"{self.host}/api/pfact/datahandler/productRate", headers=self.headers_type,
                                 verify=False, json=data)
        return response

