import base64
import json

import requests

from PyLibs.common.baseAssert import BaseAssert
from PyLibs.common.request_data import get_return_key_value


class SendRequestGetResponse(object):

    def __init__(self):
        self.res = None

    def send_request_and_get_response(self, request_data, response_data=None, return_key=None):

        if request_data.method == "GET":
            self.res = requests.get(url=request_data.url, headers=request_data.headers)
        elif request_data.method == "POST":
            self.res = requests.post(url=request_data.url, data=request_data.body, headers=request_data.headers)
        elif request_data.method == "PUT":
            self.res = requests.put(url=request_data.url, data=request_data.body, headers=request_data.headers)
        elif request_data.method == "DELETE":
            self.res = requests.delete(url=request_data.url)
        else:
            raise Exception("请求方法暂时不支持")

        if self.res.status_code != 200 and response_data is not None:
            BaseAssert(self.res.content["code"] == response_data.code, "预期返回错误code为{0},实际返回错误code{1}".format(res.status_code, response_data.code))
            BaseAssert(self.res.content["message"] == response_data.meaasge, "预期返回错误code{0},实际返回错误code{1}".format(res.content["message"], response_data.message))

        self.res = base64.b64decode(json.loads(self.res)["event"]["payload"]["data"])[16:]

        if return_key is not None:
            return get_return_key_value(return_key, self.res)

        return self.res.content



