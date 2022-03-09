# Description   :
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


class TestCaseQuerySkuList(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${ENV(P_FXM_URL)}")

    teststeps = [
        Step(
            RunTestCase("获取分销系统抢购产品id")
            .call(TestCaseGetFxmProductId)
            .export(*["product_id", "class"])
        ),
        Step(
            RunRequest("获取生产分销系统的sku_list信息")
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
                    "method": "query_sku_list",
                    "params": {
                        "pagenumber": 1,
                        "variables": {"product_id": "$product_id", "product_class": "$class"},
                    },
                }
            )
            .extract()
            .with_jmespath("body.result.rows[0].customizedGroup", "customizedGroup")
            .with_jmespath("body.result.rows[0].sku", "sku")
            .with_jmespath("body.result.rows[0].skuRebate", "skuRebate")
            .with_jmespath("body.result.rows[0].pc_name", "pc_name")
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseQuerySkuList().test_start()