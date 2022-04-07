import time
from datetime import datetime
import random
from httprunner import __version__


def get_httprunner_version():
    return __version__


def get_fxm_headers():
    headers = {"content-type": "application/json",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                             "(KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",}
    return headers


def sleep(n_secs):
    time.sleep(n_secs)


# 获取用户token
def get_token():
    token = "2ui0UkpGUF7nWkP025xG25_0257@"
    return token


# 订单号生成
def order_id():
    now = datetime.now()
    ret = ""
    date_time = now.strftime("%Y%m%d%H%M%S")
    for i in range(5):
        num = random.randint(0, 9)
        ret += "{}".format(num)
    order_id = "{}{}".format(date_time, ret)
    return order_id


# 下单时间生成
def order_time():
    now = datetime.now()
    order_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return order_time


# 取票码生成
def voucherCode():
    voucher_code = ""
    for i in range(11):
        num = random.randint(0, 9)
        voucher_code += "{}".format(num)
    return voucher_code


# 三方码生成
def third_party_code():
    ret = ""
    for i in range(5):
        num = random.randint(0, 9)
        a = random.randint(97, 122)
        b = chr(a)
        ret += "{}{}".format(num, b)
    order_id = "{}".format(ret)
    return order_id


if __name__ == "__main__":
    with open("1.txt", "w+", encoding="utf-8") as f:
        for i in range(1545, 11367):
            f.write(str(i) + "\n")