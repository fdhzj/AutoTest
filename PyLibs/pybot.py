import os
import sys

SCRIPTS_DIR = os.path.dirname(__file__)
MODULE_DIR = os.path.dirname(SCRIPTS_DIR)

try:
    sys.path.insert(0, SCRIPTS_DIR)
    sys.path.insert(0, MODULE_DIR)
except:
    pass

if __name__ == '__main__':
    from robot.api import TestSuiteBuilder
    suite = TestSuiteBuilder().build("/Users/fangdanhui/PycharmProjects/AutoTest/TEST/01_设备管理")
    suite.run()

