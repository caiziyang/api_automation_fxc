# -*- coding: utf-8 -*-
# Script Name   : add_product_base_test.py
# Author        : Caiziyang
# Time          : 2022/3/7 15:42
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
from p_fxm_product_test import TestCasePFxmProduct



class TestCaseAddProductBase(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${ENV(T_FXM_URL)}")

    teststeps = [
        Step(
            RunTestCase("获取生产产品信息数据")
            .call(TestCasePFxmProduct)
            .export(*["remark", "product_name", "img_list", "img_main",
                      "img_main_small", "img_poster", "product_addr", "lat", "lon", "begin_time", "end_time"])
        ),
        Step(
            RunRequest("新增T版产品数据")
            .post("/services/local/fxm/product/product.japi")
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
                {"method": "add_product_base", "params": {
                    "variables": {"status": "0", "business": "", "sourcing_id": "",
                                  "name": "$product_name",
                                  "min_limit_count": "1", "limit_count": "9999", "order_min_limit_count": "",
                                  "order_max_limit_count": "", "country": "0", "province": "", "city": "",
                                  "product_addr": "$product_addr", "send_type": "1", "send_time": "",
                                  "delay_day": "", "delay_hour": "", "delay_minute": "", "delay_rebate_day": "7",
                                  "refund_period": "7", "pay_ways": "3.2.2", "img_main": "$img_main", "img_main_small": "$img_main_small",
                                  "img_main_banner": "", "img_poster": "$img_poster", "img_poster_title": "", "img_list": "$img_list",
                                  "performance_tag": "8", "begin_time": "$begin_time",
                                  "end_time": "$end_time", "off_shelf_time": "2022-03-27 06:00:00",
                                  "browse": "", "is_show_countdown": 1, "buy_sms": "", "peers_buy_sms": "",
                                  "send_sms": "",
                                  "remark": "$remark",
                                  "countdown_value": "72", "img_poster_type": 0, "is_sub_wechat": 0, "lat": "$lat",
                                  "lon": "$lon", "rebate_strategy": "1", "product_class": "dzm", "label_ids": "",
                                  "is_display_pageviews": 0, "offset_pageviews": 0}}}
            )
            .validate()
            .assert_equal("status_code", 200)
        )
    ]


if __name__ == "__main__":
    TestCaseAddProductBase().test_start()