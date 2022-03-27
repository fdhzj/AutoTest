import os
import sys

from robot.conf import RobotSettings
from robotide import main
from robotide.preferences import RideSettings

TEST_DIR = "/TEST"


if __name__ == '__main__':
    robotSettings = RideSettings()
    robotSettings.set("auto_import", os.path.abspath('.'))
    robotSettings.set("pythonpath", os.path.abspath('.'))
    main(os.path.abspath('.') + TEST_DIR)

