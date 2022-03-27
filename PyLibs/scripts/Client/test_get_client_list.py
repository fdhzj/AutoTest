from PyLibs.api.CommonControlApi import CommonControlApi
from PyLibs.common.baseAssert import BaseAssert
from PyLibs.common.requestUtils import blcontrol_data
from PyLibs.enum1.controlType import ControlType
'''
前提条件是1个master有20个子设备
'''


class TestGetClientList(object):

    def __init__(self):
        self.common_control = None
        self.query_body = None

    def setup_get_client_list(self):
        self.common_control = CommonControlApi()

    def test_获取子设备列表_index不传(self):
        body1 = {
            "count": 5
        }
        body1 = blcontrol_data(body1, ControlType.getClientList, 1)
        results1 = self.common_control.common_control(body=body1)
        body2 = {
            "count": 5,
            "index": 0
        }
        body2 = blcontrol_data(body2, ControlType.getClientList, 1)
        results2 = self.common_control.common_control(body=body2)
        BaseAssert(results1 == results2, "预期index不传与传0时返回值一致，实际返回不一致")

    def test_获取子设备列表_index为空(self):
        body1 = {
            "count": 5
        }
        body1 = blcontrol_data(body1, ControlType.getClientList, 1)
        results1 = self.common_control.common_control(body=body1)
        body2 = {
            "count": 5,
            "index": ""
        }
        body2 = blcontrol_data(body2, ControlType.getClientList, 1)
        results2 = self.common_control.common_control(body=body2)
        BaseAssert(results1 == results2, "预期index为空与传0时返回值一致，实际返回不一致")

    def test_获取子设备列表_count不传(self):
        body1 = {
            "index": 0
        }
        body1 = blcontrol_data(body1, ControlType.getClientList, 1)
        results1 = self.common_control.common_control(body=body1)
        body2 = {
            "count": 5,
            "index": 0
        }
        body2 = blcontrol_data(body2, ControlType.getClientList, 1)
        results2 = self.common_control.common_control(body=body2)
        BaseAssert(results1 == results2, "预期count不传与传0时返回值一致，实际返回不一致")
        BaseAssert(len(results1) == 5, "预期不传count返回5条记录，实际返回{0}条".format(len(results1)))

    def test_获取子设备列表_count为空(self):
        body1 = {
            "index": 0,
            "count": ""
        }
        body1 = blcontrol_data(body1, ControlType.getClientList, 1)
        results1 = self.common_control.common_control(body=body1)
        body2 = {
            "count": 5,
            "index": 0
        }
        body2 = blcontrol_data(body2, ControlType.getClientList, 1)
        results2 = self.common_control.common_control(body=body2)
        BaseAssert(results1 == results2, "预期count不传与传0时返回值一致，实际返回不一致")
        BaseAssert(len(results1) == 5, "预期不传count返回5条记录，实际返回{0}条".format(len(results1)))

    def test_获取子设备列表_index为负1(self):
        body = {
            "index": -1,
            "count": 5
        }
        body = blcontrol_data(body, ControlType.getClientList, 1)
        results = self.common_control.common_control(body=body)
        BaseAssert(len(results) == 0, "预计返回0条数据，实际返回{0}条".format(len(results)))

    def test_获取子设备列表_index为21(self):
        body = {
            "index": 21,
            "count": 5
        }
        body = blcontrol_data(body, ControlType.getClientList, 1)
        results = self.common_control.common_control(body=body)
        BaseAssert(len(results) == 0, "预计返回0条数据，实际返回{0}条".format(len(results)))

    def test_获取子设备列表_index为16(self):
        body = {
            "index": 16,
            "count": 5
        }
        body = blcontrol_data(body, ControlType.getClientList, 1)
        results = self.common_control.common_control(body=body)
        BaseAssert(len(results) == 4, "预计返回4条数据，实际返回{0}条".format(len(results)))

    def test_获取子设备列表_count为1(self):
        body = {
            "index": 0,
            "count": 1
        }
        body = blcontrol_data(body, ControlType.getClientList, 1)
        results = self.common_control.common_control(body=body)
        BaseAssert(len(results) == 1, "预计返回4条数据，实际返回{0}条".format(len(results)))

    def test_获取子设备列表_count为负1(self):
        body = {
            "index": 0,
            "count": -1
        }
        body = blcontrol_data(body, ControlType.getClientList, 1)
        results = self.common_control.common_control(body=body)
        BaseAssert(len(results) == 0, "预计返回4条数据，实际返回{0}条".format(len(results)))

    def test_获取子设备列表_count为6(self):
        body = {
            "index": 0,
            "count": 6
        }
        body = blcontrol_data(body, ControlType.getClientList, 1)
        results = self.common_control.common_control(body=body)
        BaseAssert(len(results) == 5, "预计返回4条数据，实际返回{0}条".format(len(results)))




