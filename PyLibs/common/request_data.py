from variable import lid, licenseId, userId, loginSession


def get_headers():
    return {
        "lid": lid,
        "licenseId": licenseId,
        "userId": userId,
        "loginSession": loginSession
    }


def get_return_key_value(key, response_data):
    for k in response_data:
        if k == key:
            return response_data[key]
    else:
        raise Exception("返回字段没有{0}字段".format(key))
