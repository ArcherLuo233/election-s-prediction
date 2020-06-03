from model.user import User


def login(username, password):
    users = User.search(username=username)['data']
    if not users:
        return False, '用户不存在'
    user = users[0]
    if user.check_password(password) is False:
        return False, '用户名或密码错误'
    return True, user
