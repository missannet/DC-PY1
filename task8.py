money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# Первый способ -> 5
while True:
    money_capital -= spend - salary
    spend = spend + spend * increase
    if money_capital < 0:
        break
    month += 1

print(month)


