# 🛒 JavaWeb 电商平台测试项目

| 模块     | 工具             | 关键指标                          |
| -------- | ---------------- | --------------------------------- |
| 功能测试 | Excel + 思维导图 | 用例 10 条                        |
| 接口测试 | Postman + Pytest | 10 条脚本，断言通过率 100%        |
| 性能测试 | JMeter           | 下单接口 200 并发，平均 RT 235 ms |

## 🚀 一键运行

```bash
git clone ...
cd ecommerce-test
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
pytest
allure generate report/allure_raw -o report/allure_html --clean
allure open report/allure_html
```
