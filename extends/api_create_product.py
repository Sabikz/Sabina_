from extends.api import Api
import requests


class ApiCreateProduct(Api):
    def create_product(self, product_name):
        data = {
            "arh": False,
            "asbukaId": "test",
            "colvirId": "test",
            "name": product_name,
            "nameEn": "test",
            "nameKz": "testkz",
            "productTypeId": 1,
            "selectedParams": [
                {
                    "paramId": 1,
                    "refsId": [1]
                }
            ]
        }
        response = requests.post(f"{self.host}/api/pfact/admin/createProduct", headers=self.headers_type, verify=False,
                                 json=data)
        return response



