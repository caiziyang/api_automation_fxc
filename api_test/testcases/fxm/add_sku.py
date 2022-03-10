# -*- coding: utf-8 -*-
# Script Name   : add_sku.py
# Author        : Caiziyang
# Time          : 2022/3/9 15:49
# Version       : 1.0.1
# Modifications :
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from p_query_sku_test import TestCasePQuerySku
from t_get_fxm_product_id import TestCaseGetFxmProductId


class TestCaseAddSku(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${ENV(T_FXM_URL)}")

    teststeps = [
        Step(
            RunTestCase("获取T版产品id与code")
            .call(TestCaseGetFxmProductId)
            .export(*["product_id", "product_code"])
        ),
        Step(
            RunTestCase("获取生成sku信息数据")
            .call(TestCasePQuerySku)
            .export(*["sku_id", "sku_val_id", "sort_num"])
        ),
        Step(
            RunRequest("新增T版sku数据")
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
                {"method": "sku_add", "params": {
                    "variables": {"id": "null", "product_id": "$product_id", "product_code": "$product_code", "ordernum": "",
                                  "listnum": "", "allowmodify": "null", "sku_id": "$sku_id", "sku_val_id": "$sku_val_id",
                                  "sort_num": "$sort_num",
                                  },
                            },
                 }
            )
            .validate()
            .assert_equal("status_code", 200)
        )
    ]


if __name__ == "__main__":
    TestCaseAddSku().test_start()