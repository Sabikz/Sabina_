from locust import HttpUser, task, between, events
import config
import os
from dotenv import load_dotenv

load_dotenv()


class UserProduct(HttpUser):
    wait_time = between(0.00001, 0.1)
    host = "https://dev-svc.kmf.kz"

    def on_start(self):
        self.authorization()

    def authorization(self):
        login_auth = {"domainLogin": os.environ.get("DOMAIN_LOGIN"),
                      "domainPswd": os.environ.get("DOMAIN_PASSWORD")}

        login_response = self.client.post("/api/pfact/admin/auth", json=login_auth)

        if login_response.status_code == 200:
            try:
                response_json = login_response.json()

                if "Token" in response_json:
                    self.token = response_json["Token"]
                elif "data" in response_json and "accessToken" in response_json["data"]:
                    self.token = response_json["data"]["accessToken"]
                else:
                    print("Ответ не содержит поле 'Token', 'data' или 'accessToken'")
                    events.request_failure.fire(request_type="authorization", name="/api/pfact/admin/auth",
                                                response_time=0, response_length=0, exception=None, response=None)
                    self.stop()

            except (AttributeError, ValueError) as e:
                print(f"Ошибка при обработке JSON: {e}")
                print(f"Содержимое ответа: {login_response.content}")
                events.request_failure.fire(request_type="authorization", name="/api/pfact/admin/auth",
                                            response_time=0, response_length=0, exception=None, response=None)
                self.stop()

        else:
            print(f"Ошибка авторизации. Код состояния: {login_response.status_code}")
            print(f"Содержимое ответа: {login_response.content}")
            events.request_failure.fire(request_type="authorization", name="/api/pfact/admin/auth",
                                        response_time=0, response_length=0, exception=None, response=None)
            self.stop()

    @task(100)
    def create_product(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        req_body = {
            "product": {
                "arh": False,
                "asbukaId": "test",
                "colvirId": "test_produc",
                "name": "прод3",
                "nameEn": "продукт",
                "nameKaz": "продукт",
                "productTypeId": 1
            },
            "selectedParams": [
                {
                    "paramId": 1,
                    "refsId": [1]
                }
            ]
        }

        create_prod = self.client.post("/api/pfact/admin/createProduct", headers=headers,
                                       json=req_body)
        if create_prod.status_code != 200:
            print(f"Failed to create product. Status code: {create_prod.status_code}")
            print(f"Response content: {create_prod.content}")
            events.request_failure.fire(request_type="create_product", name="/api/pfact/admin/createProduct", response_time=0,
                                        response_length=0, exception=None, response=None)
