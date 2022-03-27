import time

from PyLibs.api.CommonControlApi import CommonControlApi
from PyLibs.common.baseAssert import BaseAssert
from PyLibs.common.requestUtils import blcontrol_data
from PyLibs.common.timer import timestamp_set, timerMake
from PyLibs.enum1 import Enable
from PyLibs.enum1.TimeControl import TimeControl
from PyLibs.enum1.TimeType import TimeType
from PyLibs.enum1.controlType import ControlType
from variable import MAC


class TestAddCommonTimer(object):

    def __init__(self):
        self.timestamp = None
        self.common_control = None
        self.query_body = None
        # self.query_body = blcontrol_data("{}", ControlType.queryStatus, 1)
        self.pwr_status = None

    def setup_add_common_timer(self):
        self.common_control = CommonControlApi()
        self.timestamp = int(time.time()) + 120
        self.pwr_status = self.common_control.common_control(self.query_body, return_key="pwr")

    def test_common_timer_add(self, index):
        function_timer = timestamp_set(self.timestamp + (index-1)*60, None)
        self.pwr_status = 1 - self.pwr_status
        common_timer_body = timerMake(MAC, TimeControl.add, TimeType.common, Enable.Enanle, function_timer,
                                      {"pwr": self.pwr_status})
        results = self.common_control.common_control(blcontrol_data(common_timer_body, ControlType.timerSet, 1),
                                                     return_key="index")
        BaseAssert(results["index"] == (index-1), "预期添加第一个定时任务返回索引为0，实际返回{0}".format(results["index"]))

    def test_添加第1个普通定时(self):
        self.test_common_timer_add(index=1)

    def test_添加第2个普通定时(self):
        self.test_common_timer_add(index=2)

    def test_添加第3个普通定时(self):
        self.test_common_timer_add(index=3)

    def test_添加第4个普通定时(self):
        self.test_common_timer_add(index=4)

    def test_添加第5个普通定时(self):
        self.test_common_timer_add(index=5)

    def test_添加第6个普通定时(self):
        self.test_common_timer_add(index=6)

    def test_添加第7个普通定时(self):
        self.test_common_timer_add(index=7)

    def test_添加第8个普通定时(self):
        self.test_common_timer_add(index=8)

    def test_添加第9个普通定时(self):
        self.test_common_timer_add(index=9)

    def test_添加第10个普通定时(self):
        self.test_common_timer_add(index=10)

    def test_添加第11个普通定时(self):
        self.test_common_timer_add(index=11)

    def test_添加第12个普通定时(self):
        self.test_common_timer_add(index=12)

    def test_添加第13个普通定时(self):
        self.test_common_timer_add(index=13)

    def test_添加第14个普通定时(self):
        self.test_common_timer_add(index=14)

    def test_添加第15个普通定时(self):
        self.test_common_timer_add(index=15)

    def test_添加第16个普通定时(self):
        self.test_common_timer_add(index=16)

    def test_添加第17个普通定时(self):
        self.test_common_timer_add(index=17)

    def test_添加第18个普通定时(self):
        self.test_common_timer_add(index=18)

    def test_添加第19个普通定时(self):
        self.test_common_timer_add(index=19)

    def test_添加第20个普通定时(self):
        self.test_common_timer_add(index=20)

    def test_添加第21个普通定时(self):
        self.test_common_timer_add(index=21)

    def test_添加第22个普通定时(self):
        self.test_common_timer_add(index=22)

    def test_添加第23个普通定时(self):
        self.test_common_timer_add(index=24)

    def test_添加第24个普通定时(self):
        self.test_common_timer_add(index=24)

    def test_添加第25个普通定时(self):
        self.test_common_timer_add(index=25)

    def test_添加第26个普通定时(self):
        self.test_common_timer_add(index=26)

    def test_添加第27个普通定时(self):
        self.test_common_timer_add(index=27)

    def test_添加第28个普通定时(self):
        self.test_common_timer_add(index=28)

    def test_添加第29个普通定时(self):
        self.test_common_timer_add(index=29)

    def test_添加第30个普通定时(self):
        self.test_common_timer_add(index=30)

    def test_添加第31个普通定时(self):
        self.test_common_timer_add(index=31)

    def test_添加第32个普通定时(self):
        self.test_common_timer_add(index=32)

    def test_添加第33个普通定时(self):
        self.test_common_timer_add(index=33)

    def test_添加第34个普通定时(self):
        self.test_common_timer_add(index=34)

    def test_添加第35个普通定时(self):
        self.test_common_timer_add(index=35)

    def test_添加第36个普通定时(self):
        self.test_common_timer_add(index=36)

    def test_添加第37个普通定时(self):
        self.test_common_timer_add(index=37)

    def test_添加第38个普通定时(self):
        self.test_common_timer_add(index=38)

    def test_添加第39个普通定时(self):
        self.test_common_timer_add(index=39)

    def test_添加第40个普通定时(self):
        self.test_common_timer_add(index=40)

    def test_添加第41个普通定时(self):
        self.test_common_timer_add(index=41)

    def test_添加第42个普通定时(self):
        self.test_common_timer_add(index=42)

    def test_添加第43个普通定时(self):
        self.test_common_timer_add(index=43)

    def test_添加第44个普通定时(self):
        self.test_common_timer_add(index=44)

    def test_添加第45个普通定时(self):
        self.test_common_timer_add(index=45)

    def test_添加第46个普通定时(self):
        self.test_common_timer_add(index=9)

    def test_添加第47个普通定时(self):
        self.test_common_timer_add(index=47)

    def test_添加第48个普通定时(self):
        self.test_common_timer_add(index=48)