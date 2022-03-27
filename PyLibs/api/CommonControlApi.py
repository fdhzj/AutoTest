from PyLibs.common.send_request_get_response import SendRequestGetResponse
from PyLibs.data.commonControl import CommonControl


class CommonControlApi(object):

    def __init__(self):
        self.request = SendRequestGetResponse()

    def common_control(self, body=None, response_data=None, return_key=None):
        request_data = CommonControl()
        if body:
            request_data.body.update(body)
        return self.request.send_request_and_get_response(request_data, response_data, return_key)
