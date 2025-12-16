salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital =0
counter = months
while counter > 0:
    money_capital += spend
    money_capital -= salary
    spend *= (1 + increase)
    counter -= 1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
