# 极致CMS v2.5.6 DDL SQL注入漏洞

🌍 Language | 语言选择
- [English (English)](./README.md)
- [中文 (Chinese)](./README_CN.md)

##漏洞信息 

- 漏洞类型：DDL SQL注入 
- 影响版本：极致CMS v2.5.6 
- 漏洞路径：`/index.php/admins/Fields/addFields.html` 
- 漏洞参数：`field` 
- 权限要求：后台管理员账号

##复现步骤 

1. 后台登录地址：`http://127.0.0.1/index.php/admins/Login/index.html` 
2. 访问漏洞页面：`http://127.0.0.1/index.php/admins/Fields/addFields.html?molds=article` 
3. 抓包后修改 `field` 参数为攻击载荷，发送请求。 
4. 查看数据库验证漏洞。

## 安装依赖
- pip install requests
## 运行poc
- python jizhicms-v2.5.6-dll-sqli-poc.py

