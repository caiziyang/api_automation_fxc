# -*- coding: utf-8 -*-
# Script Name   : get_fxm_product_id.py
# Author        : Caiziyang
# Time          : 2022/3/7 16:32
# Version       : 1.0.1
# Modifications : 
#
# Description   :
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseGetFxmProductId(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${ENV(PFXMURL)}")

    teststeps = [
        Step(
            RunRequest("获取分销系统抢购产品id")
            .post("/fxm/services/local/fxm/product/product.japi")
            .with_headers(
                **{
                    "content-type": "application/json",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                                  " (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                }
            )
            .with_cookies(
                **{
                    "JSESSIONID": "E4145889AC0203AED54C62384C365D8C",
                    "RSESSIONID": "YWJL0EQC33BMFYJEP09PHCFRZJGV94J0",
                }
            )
            .with_json(
                {
                    "method": "queryFromEs",
                    "params": {
                        "pagenumber": 1,
                        "pagesize": 30,
                        "variables": {
                            "product_code": "5YNAR5",
                            "product_class": "dzm",
                        },
                    },
                }
            )
            .extract()
            .with_jmespath("body.result.rows[0].id", "product_id")
            .with_jmespath("body.result.rows[0].class", "class")
            .validate()
            .assert_equal("status_code", 200)
        ),
        ]


if __name__ == "__main__":
    TestCaseGetFxmProductId().test_start()