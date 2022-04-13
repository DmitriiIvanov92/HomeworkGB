import sys
sys.path.append('../../..')

from utils.convert_money_utils import currency_rates

currency = sys.argv[1]
print(f'{currency.upper()}: {currency_rates(currency)}')