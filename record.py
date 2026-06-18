import json
import os

# 账单文件路径
BILL_FILE = "bill.json"

# 初始化账单文件，不存在则创建空列表
def init_file():
    if not os.path.exists(BILL_FILE):
        with open(BILL_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

# 添加收支记录
def add_record(types, money, category, date, desc):
    """
    types: income / expense 收入/支出
    money: 金额 float
    category: 分类 餐饮/交通/工资等
    date: 日期 2026-06-17
    desc: 备注
    """
    init_file()
    # 读取原有数据
    with open(BILL_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    # 新增单条账单
    new_bill = {
        "type": types,
        "money": money,
        "category": category,
        "date": date,
        "desc": desc
    }
    data.append(new_bill)
    # 写回文件
    with open(BILL_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("账单添加成功！")

# 获取全部账单（给统计模块调用）
def get_all_records():
    init_file()
    with open(BILL_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
