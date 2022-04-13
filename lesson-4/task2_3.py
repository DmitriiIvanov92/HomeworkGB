from datetime import datetime
import requests

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
# print(response)
# pprint.pprint(response.text)
idx = response.text.find('Date')
date_url = response.text[idx + 6:idx + 16]
date = datetime.date(datetime.strptime(date_url, "%d.%m.%Y"))

# 1 вариант срабатывает только с USD,EUR,GBP:
# usd_rub = response.text[1720:1728]
# eur_rub = response.text[1855:1863]
# gbp_rub = response.text[551:559]
# convert_usd_rub = round(float(usd_rub.replace(',', '.')), 2)
# convert_eur_rub = round(float(eur_rub.replace(',', '.')), 2)
# convert_gbp_rub = round(float(gbp_rub.replace(',', '.')), 2)

# current_rates_dict = {
#     'USD': convert_usd_rub,
#     'EUR': convert_eur_rub,
#     'GBP': convert_gbp_rub
# }

# def currency_rates(currency):
#     if current_rates_dict.get(currency.upper()):
#         return f'{current_rates_dict.get((currency.upper())):.02f} рублей, {date}' \
#             if users.lower() else f'{current_rates_dict.get(currency.lower()):.02f}'
#
#
# users = input('Введите желаемую валюту для обмена: ')
# print(currency_rates(users))

# -------------------------------------------------------------------------------------  2 вариант:
currencies = []
for el in response.text.split('<CharCode>')[1:]:
    currencies.append(el.split('</CharCode>')[0])
# currencies = ['AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL', 'HUF', 'HKD', 'DKK', 'USD', 'EUR', 'INR',
# 'KZT', 'CAD', 'KGS', 'CNY', 'MDL', 'NOK', 'PLN', 'RON', 'XDR', 'SGD', 'TJS', 'TRY', 'TMT',
# 'UZS', 'UAH', 'CZK', 'SEK', 'CHF', 'ZAR', 'KRW', 'JPY']
value = []
for val in response.text.split('<Value>')[1:]:
    value.append(float(val.split('</Value>')[0].replace(',', '.')))
current_rates_dict = dict(zip(currencies, value))


def currency_rates(currency):
    if current_rates_dict.get(currency.upper()):
        return f'{users.upper()}: {current_rates_dict.get((currency.upper())):.02f} рублей, {date}' \
            if currency.lower() else f'{current_rates_dict.get(currency.lower()):.02f}'


users = input('Введите желаемую валюту для обмена: ')
print(currency_rates(users))

if __name__ == '__main__':
    aud = f'AUD: {currency_rates("aud")}'
    kzt = f'KZT: {currency_rates("kzt")}'
    print(aud)
    print(kzt)
