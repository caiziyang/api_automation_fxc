# -*- coding: utf-8 -*-
# Script Name   : add_sku.py
# Author        : Caiziyang
# Time          : 2022/3/9 15:49
# Version       : 1.0.1
# Modifications :
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from query_sku_list import TestCaseQuerySkuList
from t_get_fxm_product_id import TestCaseGetFxmProductId


class TestCaseAddSkuList(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${ENV(T_FXM_URL)}")

    teststeps = [
        Step(
            RunTestCase("获取T版产品id与code")
            .call(TestCaseGetFxmProductId)
            .export(*["product_id", "product_code"])
        ),
        Step(
            RunTestCase("获取生成sku_list信息数据")
            .call(TestCaseQuerySkuList)
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
                {
                    "method": "quantity_add",
                    "params": {
                        "variables": {
                            "PR_USE_OUTCODE": "0",
                            "id": "",
                            "product_id": 5466,
                            "product_code": "CVFM8J",
                            "class": "dzm",
                            "sku_id": "222047",
                            "api_data": "103948",
                            "api_data_name": "銆愮數璇濋绾︺\ufffd戜經灞变笁姘村笇灏旈】娆㈡湅閰掑簵鑷姪鏅氶锛\ufffd218鎶㈣喘锛\ufffd",
                            "cost_price": "200",
                            "ori_price": "396",
                            "price": "218",
                            "is_support_axt": 0,
                            "axt_sprice": "",
                            "score": "218",
                            "rebate_force": "0",
                            "al_num": "10000",
                            "repertory": "9500",
                            "quantity": "10",
                            "min_kc_num": 0,
                            "max_kc_num": 0,
                            "inventory": "10",
                            "offset": 0,
                            "saled_num": "0",
                            "projectName": "璁㈠崟鑱旂郴浜\ufffd",
                            "hint": "",
                            "status": "0",
                            "switch_action": "1",
                            "begin_time": "2022-03-07 00:00:00",
                            "end_time": "2022-06-29 00:00:00",
                            "sku": "$鍚愰\ufffd楀枩鍓\ufffd:$鍗曚汉闂ㄧエ",
                            "axt_cprice": "10.90",
                            "rebate_total": "8.00",
                            "super_grand_rebate": "33.3333",
                            "senior_grand_rebate": "66.6667",
                            "special_rebate": "-66.6667",
                            "senior_special_rebate": "-100.0000",
                            "agency_price01": "166.6667",
                            "agency_price02": "300.0000",
                            "proportion_up": "62.5000",
                            "proportion_down": "37.5000",
                            "rebate_rule": "4.1",
                            "rebate_down": "3.00",
                            "rebate_up": "5.00",
                            "agency_rebate_down": "9.00",
                            "agency_rebate_up": "5.00",
                            "rebate_id": 1323,
                            "list_params": [
                                {
                                    "name": "璁㈠崟鑱旂郴浜\ufffd",
                                    "follow_change": "0",
                                    "is_main": "0",
                                    "is_idcard_tips": "0",
                                    "is_authentication_tips": "0"
                                },
                                {
                                    "name": "濮撳悕",
                                    "num": "1",
                                    "control": "1",
                                    "must": "1",
                                    "key_value": {}
                                },
                                {
                                    "name": "鎵嬫満",
                                    "num": "1",
                                    "control": "2",
                                    "must": "1",
                                    "key_value": {}
                                }
                            ],
                            "features": "null"
                        }
                    }
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        )
    ]


if __name__ == "__main__":
    TestCaseAddSkuList().test_start()