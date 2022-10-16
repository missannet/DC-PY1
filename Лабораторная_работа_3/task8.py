money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while (money_capital + salary * month) > (increase + 1) ** month * spend * month:
    month += 1

print(month)
