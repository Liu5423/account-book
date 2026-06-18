from record import get_all_records
from collections import defaultdict

# 查看全部账单
def show_all():
    bill_list = get_all_records()
    if len(bill_list) == 0:
        print("暂无账单记录！")
        return
    print("=====全部账单=====")
    for idx, bill in enumerate(bill_list, 1):
        print(f"{idx}. {bill['date']} | {bill['type']} | {bill['category']} | {bill['money']}元 | 备注：{bill['desc']}")

# 按月统计收支
def month_stat(target_month):
    """target_month格式：2026-06"""
    bill_list = get_all_records()
    total_in = 0.0
    total_out = 0.0
    cate_count = defaultdict(float)

    for bill in bill_list:
        if bill["date"].startswith(target_month):
            if bill["type"] == "income":
                total_in += bill["money"]
            else:
                total_out += bill["money"]
                cate_count[bill["category"]] += bill["money"]
    print(f"====={target_month}月度统计=====")
    print(f"总收入：{total_in:.2f} 元")
    print(f"总支出：{total_out:.2f} 元")
    print(f"当月结余：{total_in - total_out:.2f} 元")
    print("支出分类明细：")
    for k, v in cate_count.items():
        print(f"  {k}: {v:.2f}元")
