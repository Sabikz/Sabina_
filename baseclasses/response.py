from enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code
        self.response_content = response.content

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
            else:
                schema.parse_obj(self.response_json)
            return self

    def assert_status_code(self, status_code):
        print("Actual response status", self.response_status)
        print("Expected response status", status_code)
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        print("Response content:", self.response_content)
        return self
