from PyLibs.common.send_request_get_response import SendRequestGetResponse
from PyLibs.data.userLogin import UserLogin


class UserLoginApi(object):

    def __init__(self):
        self.request = SendRequestGetResponse()

    def user_login(self, body, headers, response_data=None, return_key=None):
        request_data = UserLogin()
        if body:
            request_data.body.update(body)
        request_data.headers = headers
        return self.request.send_request_and_get_response(request_data, response_data, return_key)