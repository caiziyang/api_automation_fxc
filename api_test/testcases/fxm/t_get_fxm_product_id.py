# -*- coding: utf-8 -*-
# Script Name   : t_get_fxm_product_id.py
# Author        : Caiziyang
# Time          : 2022/3/8 18:25
# Version       : 1.0.1
# Modifications :
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseGetFxmProductId(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${ENV(T_FXM_URL)}")

    teststeps = [
        Step(
            RunRequest("获取分销系统抢购产品id")
            .post("/fxm/services/local/fxm/product/product.japi")
            .with_headers(
                **{
                    "content-type": "application/json",
                    "user-agent": "${ENV(USER_AGENT)}",
                }
            )
            .with_cookies(
                **{
                    "RSESSIONID": "${ENV(T_COOKIE)}",
                }
            )
            .with_json(
                {	"order": "asc",
                    "limit": 30,
                    "method": "query",
                    "params": {
                        "variables": {
                            "product_code": "",
                            "product_class": "dzm",
                        },
                    },
                }
            )
            .extract()
            .with_jmespath("body.result.rows[0].id", "product_id")
            .with_jmespath("body.result.rows[0].product_code", "product_code")
            .validate()
            .assert_equal("status_code", 200)
        ),
        ]


if __name__ == "__main__":
    TestCaseGetFxmProductId().test_start()