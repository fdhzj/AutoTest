from PyLibs.common.request_data import get_headers
from variable import device_control_address


class CommonControl(object):

    def __init__(self):
        super(CommonControl, self).__init__()
        self.method = "POST"
        self.url = device_control_address + '/device/control/v2/sdkcontrol'
        self.body = {}
        self.headers = get_headers()


