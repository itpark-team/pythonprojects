# money = float(input("введите начальную сумму денег на счёте: "))
# percent = float(input("введите годовой процент по вкладу: "))
# years = int(input("введите количество лет на которые хотите сделать вклад: "))

# i = 0
# while i < years:
#     money = money + money * percent / 100
#     i = i + 1
#     print(f"год {i} - отстаток на счету {money:.2f}")

# print(f"денег на счёте после {years} лет = {money:.2f}")


money = float(input("введите начальную сумму денег на счёте: "))
percent = float(input("введите годовой процент по вкладу: "))
finish_money = float(input("введите конечную сумму денег на счёте: "))
# finish_money = money * 2
years = 0

while money < finish_money:
    money = money + money * percent / 100
    years = years + 1
    print(f"год {years} - отстаток на счету {money:.2f}")

print(f"денег на счёте после {years} лет = {money:.2f}")  

