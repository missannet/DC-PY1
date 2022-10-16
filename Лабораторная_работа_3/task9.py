salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for i in list(range(0, months)):
    w = (increase + 1) ** i * spend
    need_money += w

need_money -= salary * months
print(round(need_money))
