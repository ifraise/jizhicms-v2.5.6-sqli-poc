# JizhiCMS v2.5.6 DDL SQL Injection

🌍 Language | 语言选择
- [English (English)](./README.md)
- [中文 (Chinese)](./README_CN.md)

## Vulnerability Info
- Type: DDL SQL Injection
- Affected Version: JizhiCMS v2.5.6
- Vulnerable Path: `/index.php/admins/Fields/addFields.html`
- Vulnerable Parameter: `field`
- Permission: Admin account required

## Manual Reproduction
1. Log in to backend: `http://127.0.0.1/index.php/admins/Login/index.html`
2. Access vulnerable page: `http://127.0.0.1/index.php/admins/Fields/addFields.html?molds=article`
3. Capture request, replace `field` with payload and send.
4. Check database to confirm the result.

## Install dependency
- pip install requests
## Run POC
- python jizhicms-v2.5.6-dll-sqli-poc.py
