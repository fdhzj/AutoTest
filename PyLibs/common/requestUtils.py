import base64
import binascii
import json
import time

from variable import MAC, PID, AESKEY


def lencal(data):
    len1 = len(data)
    len1 = hex(len1)
    if len(len1) == 3:
        datalen = int(len1[2:3], 16)
    elif len(len1) == 4:
        datalen = int(len1[2:4], 16)
    elif len(len1) == 5:
        datalen = int(len1[2:3], 16) + int(len1[3:5], 16)
    else:
        datalen = int(len1[2:4], 16) + int(len1[4:6], 16)
    return datalen


def asciitostring(data):
    e = 0
    for i in data:
        d = ord(i)
        e = e + d
    return e


def bytetoString(data):
    hexString = ""
    for i in range(0, len(data)):
        if len(hex(data[i])) == 4:
            hexString += hex(data[i])[2:4]
        else:
            hexString += "0" + hex(data[i])[2:3]
    return hexString


def calsumdata(data, command_type):
    len1 = len(data)
    len2 = lencal(data)
    if len1 < 16:
        len1 = "0" + str(hex(len1))[2:] + "00"
    elif 16 <= len1 < 256:
        len1 = str(hex(len1))[2:] + "00"
    elif 256 <= len1 < 4096:
        len1 = str(hex(len1))[3:] + "0" + str(hex(len1))[2:3]
    else:
        len1 = str(hex(len1))[4:6] + str(hex(len1))[2:4]
    e = asciitostring(data)
    calsum = 165 + 165 + 90 + 90 + int(command_type[0:2], 16) + int(command_type[2:4], 16) + len2 + e + 48815
    if calsum > 65535:
        calsum -= 65536
    calsum = str(hex(calsum))
    if len(calsum) == 6:
        calsum = calsum[4:6] + calsum[2:4]
    else:
        calsum = calsum[3:5] + "0" + calsum[2:3]
    returndata = "a5a55a5a" + calsum + command_type + len1 + "0000"
    print(returndata)
    return binascii.a2b_hex(returndata)


def commandconstitute(mac, pid, key, data, pad):
    timestamp = str(time.time())
    did = "00000000000000000000" + mac
    device_mac = mac[0:2] + ":" + mac[2:4] + ":" + mac[4:6] + ":" + mac[6:8] + ":" + mac[8:10] + ":" + mac[10:12]
    cookie = {
        "device":
            {
                "id": 1,
                "key": key,
                "aeskey": key,
                "did": did,
                "pid": pid,
                "mac": device_mac
            }
    }

    cookie_base64 = base64.b64encode(json.loads(cookie).encode("utf-8"))
    return {
        "directive": {
            "header": {
                "namespace": "DNA.TransmissionControl",
                "name": "commonControl",
                "interfaceVersion": "2",
                "messageId": did + '-' + timestamp
            },
            "endpoint": {
                "devicePairedInfo": {
                    "did": did,
                    "pid": pid,
                    "mac": device_mac,
                    "cookie": cookie_base64.decode()
                },
                "endpointId": did,
                "cookie": {}
            },
            "payload": data.decode(),
            "notpadding": pad
        }
    }


def blcontrol_data(querydata, control_type, pad):
    querydata = json.loads(querydata)
    header_data = calsumdata(querydata, control_type)
    body = base64.b64encode(header_data) + base64.b64encode(querydata)
    return commandconstitute(MAC, PID, AESKEY, body, pad)

