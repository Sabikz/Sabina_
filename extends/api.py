import requests as requests
import config
import os
from dotenv import load_dotenv

load_dotenv()


class Api:
    host = None
    data_user = None

    def __init__(self):
        self.host = "https://dev-svc.kmf.kz"
        self.data_user = self.authorize()
        self.token = f"Bearer {self.data_user}"
        self.headers_type = {"Content-Type": "application/json",
                             "Authorization": self.token}

    def login(self):
        data = {"domainLogin": os.environ.get("DOMAIN_LOGIN"),
                "domainPswd": os.environ.get("DOMAIN_PASSWORD")}
        headers_type = {"Content-Type": "application/json"}
        response = requests.post("https://dev-svc.kmf.kz/api/pfact/admin/auth", headers=headers_type, json=data,
                                 verify=False)
        return response

    def authorize(self):
        response = self.login()
        if response.status_code != 200:
            raise Exception("Error authorize using given credential")

        try:
            result = response.json()
            print("Full response:", result)
            access_token = result["data"]["accessToken"]
            return access_token
        except KeyError:
            raise Exception("No 'accessToken' found in the response")


