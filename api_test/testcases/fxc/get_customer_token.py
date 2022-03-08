# -*- coding: utf-8 -*-
# Script Name   : get_customer_token.py
# Author        : Caiziyang
# Time          : 2022/1/5 11:21
# Version       : 1.0.1
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseGetCustomerToken(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${ENV(BASEURL)}").export("USERTOKEN")

    teststeps = [
        Step(
            RunRequest("/fxc/781962339.jsp")
            .get("/fxc/781962339.jsp")
            .with_params(**{"userid": "12018601"})
            .with_headers(
                **{
                    "user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) "
                                  "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.70"
                                  " Mobile Safari/537.36 MMWEBID/77 MicroMessenger/7.0.22.1820(0x27001636) "
                                  "Process/tools WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32",
                    "content-type": "application/json",
                }
            )
            .extract().with_jmespath("cookies.usertoken", "USERTOKEN")
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseGetCustomerToken().test_start()