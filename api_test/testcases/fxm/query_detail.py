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

    config = Config("testcase description").verify(False)

    teststeps = [

        Step(
            RunRequest("/fxm/services/local/fxm/product/product.japi")
            .post("https://m.lhs11.com/fxm/services/local/fxm/product/product.japi")
            .with_headers(
                **{
                    "content-length": "69",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "x-requested-with": "XMLHttpRequest",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
                    "sec-ch-ua-platform": '"Windows"',
                    "origin": "https://m.lhs11.com",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://m.lhs11.com/fxm/page/fxm/product/dzm/addorupdate.jsp?action=update&product_id=338144&page=1",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,zh-TW;q=0.6",
                }
            )
            .with_cookies(
                **{
                    "nginx-sticky": "1646617599.75.875.846701",
                    "JSESSIONID": "E4145889AC0203AED54C62384C365D8C",
                    "RSESSIONID": "YWJL0EQC33BMFYJEP09PHCFRZJGV94J0",
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