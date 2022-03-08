# -*- coding: utf-8 -*-
# Script Name   : run.py
# Author        : Caiziyang
# Time          : 2021/12/21 15:18
# Version       : 1.0.1
import os
import logging
import time


def main():
    path = os.path.abspath(os.path.dirname(__file__))
    text_path = os.path.join(path, "testcases")
    logging.info("测试文件的路径{}".format(text_path))
    print(text_path)
    report_path = os.path.join(path, "reports\\report_{}.html".format(time.strftime('%Y-%m-%d')))
    logging.info("报告输出的路径{}".format(report_path))
    # logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
    #                    level=logging.DEBUG)
    os.system("hrun {} --html={}".format(text_path, report_path))
    os.system("start {}".format(report_path))
    # os.system("hrun {} --alluredir={}".format(text_path, report_path))
    # os.system("allure serve {}".format(report_path))


if __name__ == "__main__":
    main()