# -*- coding: utf-8 -*-
# Script Name   : query_sku_list.py
# Author        : Caiziyang
# Time          : 2022/3/7 14:49
# Version       : 1.0.1
# Modifications : 
#
# Description   :
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
from get_product_class import get_product_class
from get_fxm_product_id import TestCaseGetFxmProductId


class TestCaseQuerySkuList(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${ENV(PFXMURL)}")

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
                    "order": "asc",
                    "method": "query_sku_list",
                    "params": {
                        "pagenumber": 1,
                        "variables": {"product_id": "$product_id", "product_class": "$class"},
                    },
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseQuerySkuList().test_start()