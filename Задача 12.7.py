money = int(input("Введите сумму вклада:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

ТКБ = int(money / 100 * per_cent['ТКБ'])
СКБ = int(money / 100 * per_cent['СКБ'])
ВТБ = int(money / 100 * per_cent['ВТБ'])
СБЕР = int(money / 100 * per_cent['СБЕР'])

deposit = [ТКБ, СКБ, ВТБ, СБЕР]

print(deposit)

print("Максимальная сумма, которую вы можете заработать — ", max(deposit))
# Мой код выглядит неочень, но он работает)))