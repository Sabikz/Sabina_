from extends.api import Api
import requests


class ApiFindProduct(Api):
    def find_product(self):

        data = {
            "channelId": 1,
            "clientTypeId": 1,
            "creditPurposeId": 1,
            "creditSum": 1,
            "creditTerm": 1,
            "currencyId": 1,
            "firmId": 1,
            "insurId": 1,
            "lendKindId": 1,
            "lineId": 1,
            "lineProductId": 1,
            "lineSum": 1,
            "lineTerm": 1,
            "payMethodId": 1,
            "productSubTypeId": 1,
            "seasonMark": True,
            "trancheNumber": 1,
            "validSince": "string"
        }
        response = requests.post(f"{self.host}/api/pfact/datahandler/findProduct", headers=self.headers_type,
                                 verify=False, json=data)
        return response
