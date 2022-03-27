from PyLibs.api.CommonControlApi import CommonControlApi
from PyLibs.common.baseAssert import BaseAssert
from PyLibs.common.compare_dict import cmp_ad_dict
from PyLibs.common.requestUtils import blcontrol_data
from PyLibs.enum1.Enable import PwrStatus
from PyLibs.enum1.controlType import ControlType


class TestCommonControl(object):

    def __init__(self):
        self.common_control = None
        self.query_body = None

    def setup_common_control(self):
        self.common_control = CommonControlApi()
        self.query_body = blcontrol_data('{}', ControlType.queryStatus, 1)

    def test_common_control(self, pwr, status):
        result1 = self.common_control.common_control(self.query_body)
        control_body = blcontrol_data('{"{0}": %d}'.format(pwr, status), ControlType.controlStatus, 1)
        self.common_control.common_control(body=control_body)
        result2 = self.common_control.common_control(self.query_body)
        BaseAssert(result2[pwr] == status, "预期开关状态为{0}， 实际开关状态为{1}".format(status, result2["pwr"]))
        cmp_ad_dict(result1.pop(pwr), result2.pop(pwr))

    def test_测试1加1等于0(self):
        pass

    def test_通用电工控制_设置pwr为0(self):
        self.test_common_control("pwr", PwrStatus.off)

    def test_通用电工控制_设置pwr为1(self):
        self.test_common_control("pwr", PwrStatus.on)

    def test_通用电工控制_设置pwr1为0(self):
        self.test_common_control("pwr1", PwrStatus.off)

    def test_通用电工控制_设置pwr1为1(self):
        self.test_common_control("pwr1", PwrStatus.on)

    def test_通用电工控制_设置pwr2为0(self):
        self.test_common_control("pwr2", PwrStatus.off)

    def test_通用电工控制_设置pwr2为1(self):
        self.test_common_control("pwr2", PwrStatus.on)

    def test_通用电工控制_设置pwr3为0(self):
        self.test_common_control("pwr3", PwrStatus.off)

    def test_通用电工控制_设置pwr3为1(self):
        self.test_common_control("pwr3", PwrStatus.on)

    def test_通用电工控制_设置pwr4为0(self):
        self.test_common_control("pwr4", PwrStatus.off)

    def test_通用电工控制_设置pwr4为1(self):
        self.test_common_control("pwr4", PwrStatus.on)


