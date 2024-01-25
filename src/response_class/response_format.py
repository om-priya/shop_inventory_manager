class SuccessResponse:
    success = True

    def __init__(self, message, res_data):
        self.message = message
        self.json_data = res_data

    def get_json(self):
        res_dict = {
            "success": SuccessResponse.success,
            "message": self.message,
            "data": {"application/json": self.json_data},
        }
        return res_dict


class ErrorResponse:
    success = False

    def __init__(self, err_status_code, err_message, err_endpoint, guide_to_resolve):
        self.err_status_code = err_status_code
        self.err_message = err_message
        self.err_endpoint = err_endpoint
        self.guide_to_resolve = guide_to_resolve

    def get_json(self):
        res_dict = {
            "success": ErrorResponse.success,
            "err_info": {
                "message": self.err_message,
                "status_code": self.err_status_code,
                "err_endpoint": self.err_endpoint,
                "guide_to_resolve": self.guide_to_resolve,
            },
        }
