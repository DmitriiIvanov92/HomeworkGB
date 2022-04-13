from utils.convert_money_utils import currency_rates
# from utils.convert_money_utils import users  # убрать users если хотим вывести str = 'usd', 'eur'

print(f'USD: {currency_rates("usd")}')  # срабатывает,если в convert_money отключаем input() и print
print(f'EUR: {currency_rates("eur")}')

# print(f'{users.upper()}: {currency_rates(users)}')