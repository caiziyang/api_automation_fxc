# NOTE: Generated By HttpRunner v3.1.6
# FROM: har\p_fxm_product.har
"""
"""

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from get_fxm_product_id import TestCaseGetFxmProductId


class TestCasePFxmProduct(HttpRunner):

    config = Config("testcase description").verify(False).base_url("${ENV(PFXMURL)}")

    teststeps = [
        Step(
            RunTestCase("调用生产分销系统获取抢购产品id")
            .call(TestCaseGetFxmProductId)
            .export(*["product_id"])
        ),
        Step(
            RunRequest("获取生产分销系统抢购产品的基本信息，并提取响应的信息")
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
                {"method": "query", "params": {"variables": {"id": "$product_id"}}}
            )
            .extract().with_jmespath("body.result.rows[0].remark", "remark")
            .with_jmespath("body.result.rows[0].name", "product_name")
            .with_jmespath("body.result.rows[0].img_list", "img_list")
            .with_jmespath("body.result.rows[0].img_main", "img_main")
            .with_jmespath("body.result.rows[0].img_main_small", "img_main_small")
            .with_jmespath("body.result.rows[0].img_poster", "img_poster")
            .with_jmespath("body.result.rows[0].product_addr", "product_addr")
            .with_jmespath("body.result.rows[0].lat", "lat")
            .with_jmespath("body.result.rows[0].lon", "lon")
            .with_jmespath("body.result.rows[0].begin_time", "begin_time")
            .with_jmespath("body.result.rows[0].end_time", "end_time")
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCasePFxmProduct().test_start()
