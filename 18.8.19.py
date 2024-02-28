tickets = int(input('Какое количество билетов требуется:'))
price_ticket = 0
for age in range(tickets):
    age = int(input('Введите возраст посетителя:'))
    if age < 18:
        price_ticket += 0
    elif 18 <= age < 25:
        price_ticket += 990
    elif age >= 25:
        price_ticket += 1390
if tickets > 3:
    price_ticket -= price_ticket / 100 * 10

print('Сумма к оплате:', price_ticket )


