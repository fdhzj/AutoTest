from variable import user_login_address


class UserLogin(object):

    def __init__(self):
        super(UserLogin, self).__init__()
        self.method = "POST"
        self.url = user_login_address + '/account/login'
        self.body = {}
        self.headers = {}