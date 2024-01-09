from extends.api import Api
import requests


class ApiCreateProduct(Api):
    def create_product(self, product_name, r_cl_type, r_channel, r_lpur, r_sm_loan, r_mn_loan, r_currency, r_firm,
                       r_lend_kind):

        data = {
            "product": {
                "arh": False,
                "asbukaId": "test",
                "colvirId": "test",
                "name": product_name,
                "nameEn": "test",
                "nameKz": "test",
                "productTypeId": 1,
            },
            "selectedParams": [
                {
                    "paramId": 1,
                    "refsId": [r_cl_type]
                },
                {
                    "paramId": 27,
                    "refsId": [r_channel]
                },
                {
                    "paramId": 5,
                    "refsId": [r_lpur]
                },
                {
                    "paramId": 4,
                    "refsId": [r_sm_loan]
                },
                {
                    "paramId": 11,
                    "refsId": [r_mn_loan]
                },
                {
                    "paramId": 6,
                    "refsId": [r_currency]
                },
                {
                    "paramId": 7,
                    "refsId": [r_firm]
                },
                {
                    "paramId": 9,
                    "refsId": [r_lend_kind]
                }
            ]
        }
        response = requests.post(f"{self.host}/api/pfact/admin/createProduct", headers=self.headers_type, verify=False,
                                 json=data)
        return response




