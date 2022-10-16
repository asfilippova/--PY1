salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
for month in range (0, 10): # рассчитываем сумму на 10 месяцев
    need_money += abs(salary - spend) # сумма на проживание = сумма разницы от зарплаты и расходов
    spend = spend * (1 + increase)

print(round(need_money))
