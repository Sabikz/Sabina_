from enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response):
        self.response = response
        try:
            self.response_json = response.json()
        except (AttributeError, ValueError):
            self.response_json = None
        self.response_status = getattr(response, 'status_code', None)
        self.response_content = getattr(response, 'content', None)

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
            else:
                schema.parse_obj(self.response_json)
            return self

    class Response:
        def __init__(self, response_data):
            self.response_data = response_data
            self.response_status = response_data.get('status',
                                                     None)  # Здесь 'status' - это ключ для статуса в вашем ответе

        def assert_status_code(self, status_code):
            print("Actual response status", self.response_status)
            print("Expected response status", status_code)
            if isinstance(status_code, list):
                assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
            else:
                assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
