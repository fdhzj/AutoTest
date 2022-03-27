# coding=utf-8

import hashlib
import json
import time

from Crypto.Cipher import AES

from PyLibs.api.UserLoginApi import UserLoginApi
from variable import password, phone, companyid

BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]

ACCOUNTAESKEYSALT = "kdixkdqp54545^#*"
ACCOUNTAESIV = "eaaaaa3abb5862a21918b5771d1615aa"
ACCOUNTFRONTKEY1 = '4969fj#k23#'
ACCOUNTKEY1 = "iejf$873#kfj%&kd"
ACCOUNTKEY2 = "xgx3d*fe3478$ukx"
ACCOUNTFRONTFALG = 1


def GetAes(timestamp, data):
    m = hashlib.md5()
    m.update(timestamp.encode("utf8"))
    m.update(ACCOUNTAESKEYSALT.encode("utf8"))
    key = m.digest()
    ciper = AES.new(key, AES.MODE_CBC, bytes.fromhex(ACCOUNTAESIV))
    aesdata = ciper.encrypt(pad(data))
    return aesdata


def getPassword(passwd):
    s = hashlib.sha1()
    s.update(passwd.encode("utf8"))
    if ACCOUNTFRONTFALG:
        s.update(ACCOUNTFRONTKEY1.encode("utf8"))
    else:
        s.update(ACCOUNTKEY1.encode("utf8"))
    return s.hexdigest()


def GetTokenHex(data):
    m = hashlib.md5()
    m.update(data.encode("utf8"))
    m.update(ACCOUNTKEY2.encode("utf8"))
    return m.hexdigest()


def login():
    user_login = UserLoginApi()
    passwd = getPassword(password)
    data = {
        "phone": phone,
        "password": passwd,
        "companyid": companyid
    }
    timestamp = str(time.time())[:10]
    data = json.dumps(data)
    body = GetAes(timestamp, data)
    token = GetTokenHex(data)
    headers = {
        "timastamp": timestamp,
        "token": token
    }
    return user_login.user_login(body, headers, return_key="loginSession")



