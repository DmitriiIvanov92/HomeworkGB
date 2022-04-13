from datetime import datetime
import requests

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
idx = response.text.find('Date')
date_url = response.text[idx + 6:idx + 16]
date = datetime.date(datetime.strptime(date_url, "%d.%m.%Y"))
currencies = []
for el in response.text.split('<CharCode>')[1:]:
    currencies.append(el.split('</CharCode>')[0])
value = []
for val in response.text.split('<Value>')[1:]:
    value.append(float(val.split('</Value>')[0].replace(',', '.')))
current_rates_dict = dict(zip(currencies, value))

def currency_rates(currency):
    if current_rates_dict.get(currency.upper()):
        return f'{current_rates_dict.get((currency.upper())):.02f} руб., {date}' \
            if currency.lower() else f'{current_rates_dict.get(currency.lower()):.02f}'


# users = input('Введите желаемую валюту для обмена: ')
# print(f'{users.upper()}: {currency_rates(users)}')
