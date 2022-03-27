def BaseAssert(params, message):
    if params is False:
        raise Exception(message)