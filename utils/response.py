from flask import jsonify


class BaseResponse:
    """
    BaseResponse supporting only
    the status code and data references

    ::param status_code int
    ::param **data      dict
    """

    def __init__(self, status_code: int, data: dict) -> "BaseResponse":
        self.status_code = status_code
        self.data = data


class ErrorRes(BaseResponse):
    """
    Implements BaseResponse and sets
    status code 400 and status "ERROR"
    by default

    ::param status_code int
    ::param **data      dict
    """

    def __init__(self, *, status_code: int = 400, data: dict = {}) -> "ErrorRes":
        BaseResponse.__init__(self, status_code, data)
        self.data["status"] = "ERROR"
        self.json = jsonify(self.data)
        self.json.status_code = self.status_code


class SuccessRes(BaseResponse):
    """
    Implements BaseResponse and sets
    status code 200 and status "SUCCESS"
    by default

    ::param status_code int
    ::param **data      dict
    """

    def __init__(self, *, status_code: int = 200, data: dict = {}) -> "SuccessRes":
        BaseResponse.__init__(self, status_code, data)
        data["status"] = "SUCCESS"
        self.json = jsonify(self.data)
        self.json.status_code = self.status_code
