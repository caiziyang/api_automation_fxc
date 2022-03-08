# -*- coding: utf-8 -*-
# Script Name   : p_query_sku_test.py
# Author        : Caiziyang
# Time          : 2022/3/7 14:38
# Version       : 1.0.1
# Modifications : 
#
# Description   :
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from get_fxm_product_id import TestCaseGetFxmProductId


class TestCasePQuerySku(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${ENV(P_FXM_URL)}")

    teststeps = [
        Step(
            RunTestCase("获取分销系统抢购产品id")
                .call(TestCaseGetFxmProductId)
                .export(*["product_id"])
        ),
        Step(
            RunRequest("/fxm/services/local/fxm/product/product.japi")
            .post("/fxm/services/local/fxm/product/product.japi")
            .with_headers(
                **{
                    "content-type": "application/json",
                    "user-agent": "${ENV(USER_AGENT)}",
                }
            )
            .with_cookies(
                **{
                    "RSESSIONID": "${ENV(P_COOKIE)}",
                }
            )
            .with_json(
                {
                    "order": "asc",
                    "method": "query_sku",
                    "params": {"pagenumber": 1, "variables": {"product_id": "$product_id"}},
                }
            )
            .extract().with_jmespath("body.result.rows[0].sku_id", "sku_id")
            .with_jmespath("body.result.rows[0].sku_val_id", "sku_val_id")
            .with_jmespath("body.result.rows[0].sort_num", "sort_num")
            .validate()
            .assert_equal("status_code", 200)
        )
    ]


if __name__ == "__main__":
    TestCasePQuerySku().test_start()