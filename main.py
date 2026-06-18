from record import add_record, get_all_records
from statistics import show_all, month_stat
import json

# 删除指定序号账单
def delete_record(index):
    bill_list = get_all_records()
    if index < 1 or index > len(bill_list):
        print("序号不存在！")
        return
    del bill_list[index - 1]
    with open("bill.json", "w", encoding="utf-8") as f:
        json.dump(bill_list, f, ensure_ascii=False, indent=2)
    print("删除成功！")

# 主菜单页面
def main_menu():
    while True:
        print("\n=====简易记账本=====")
        print("1. 添加收支记录")
        print("2. 查看全部账单")
        print("3. 月度收支统计")
        print("4. 删除账单记录")
        print("0. 退出程序")
        choice = input("请输入功能序号：")
        if choice == "1":
            t = input("收入/支出（income/expense）：")
            m = float(input("金额："))
            c = input("分类（餐饮/交通/工资等）：")
            d = input("日期(例2026-06-17)：")
            des = input("备注：")
            add_record(t, m, c, d, des)
        elif choice == "2":
            show_all()
        elif choice == "3":
            mon = input("输入统计月份(例2026-06)：")
            month_stat(mon)
        elif choice == "4":
            show_all()
            num = int(input("输入要删除的账单序号："))
            delete_record(num)
        elif choice == "0":
            print("程序退出，账单已保存！")
            break
        else:
            print("输入错误，请重新选择！")

if __name__ == "__main__":
    main_menu()
