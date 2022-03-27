# coding=utf-8
import base64
import time
import json

from PyLibs.enum1 import Enable
from PyLibs.enum1.TimeControl import TimeControl
from PyLibs.enum1.TimeType import TimeType


def timeset(timeline, week):
    timeline = timeline[0:4]+"-"+timeline[5:7]+"-"+timeline[8:10]+"_"+timeline[11:13]+":"+timeline[14:16]+":"+timeline[17:19]
    stamp_array = time.strptime(timeline, '%Y-%m-%d_%H:%M:%S')
    stamp = int(time.mktime(stamp_array))
    date = time.localtime(stamp)
    timeyear = time.strftime('%Y', date)
    timemonth = time.strftime('%m', date)
    timeday = time.strftime('%d', date)
    timehour = time.strftime('%H', date)
    timeminute = time.strftime('%M', date)
    timesecond = time.strftime('%S', date)
    if week is None:
        timelist = timesecond + "_" + timeminute + "_" + timehour + "_" + timeday + "_" + timemonth + "_*_" + timeyear
    else:
        timelist = timesecond + "_" + timeminute + "_" + timehour + "_" + timeday + "_" + timemonth + '_' + week + '_' + timeyear
    return timelist


def timestamp_set(timestamp, week):
    date = time.localtime(timestamp)
    timeyear = time.strftime('%Y', date)
    timemonth = time.strftime('%m', date)
    timeday = time.strftime('%d', date)
    timehour = time.strftime('%H', date)
    timeminute = time.strftime('%M', date)
    timesecond = time.strftime('%S', date)
    if week is None:
        timelist = timesecond + "_" + timeminute + "_" + timehour + "_" + timeday + "_" + timemonth + "_*_" + timeyear
    else:
        timelist = timesecond + "_" + timeminute + "_" + timehour + "_" + timeday + "_" + timemonth + '_' + week + '_' + timeyear
    return timelist


def timerMake(mac, timeControl, timeType, enable, settime, cmd):
    return {
        "did": "00000000000000000000" + mac,
        "act": timeControl,
        "timerlist": [{
            "type": timeType,
            "id": 0,
            "en": enable,
            "name": "comm",
            "time": settime,
            "cmd": cmd
        }]
    }


def cycle_or_rand_timerMake(mac, timeControl, timeType, enable, startTime, cmd1, cmd2, time1, time2,endTime):
    return {
        "did": "00000000000000000000" + mac,
        "act": timeControl,
        "timerlist": [{
            "type": timeType,
            "id": 0,
            "en": enable,
            "name": "comm",
            "sime": startTime,
            "etime": endTime,
            "cmd1": cmd1,
            "cmd2": cmd2,
            "time1": time1,
            "time2": time2
        }]
    }