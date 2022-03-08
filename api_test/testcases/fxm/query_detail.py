# -*- coding: utf-8 -*-
# Script Name   : query_detail.py
# Author        : Caiziyang
# Time          : 2022/3/7 14:46
# Version       : 1.0.1
# Modifications : 
#
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


class TestCaseQueryDetail(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${ENV(P_FXM_URL)}")

    teststeps = [

        Step(
            RunRequest("获取产品详情页信息")
            .post("/services/local/fxm/product/product.japi")
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
            .with_data(
                {
                    '{"method":"querydetail","params":{"variables":{"product_id":338144}}}': ""
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseQueryDetail().test_start()