from database import *


def token_set_token(uid, token=None):
    if token is None:
        # 生成随机的token
        token = token_get_new_token()
    c = conn_dri.cursor()
    c.execute('update drivers set token = ? where id = ?', (token, uid))
    c.close()
    conn_dri.commit()


def token_get_token(did):
    c = conn_dri.cursor()
    c.execute('select token from drivers where id = ?', (did, ))
    data = c.fetchall()[0][0]
    c.close()
    return data


def token_check(did, token):
    token_ = token_get_token(did)
    # print('Check(): {} and {}'.format(token_, token))
    if token == token_:
        return True
    else:
        return False


if __name__ == '__main__':
    print(token_check(1, '46c7f01c9548c7da'))
