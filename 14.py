import requests


def get_values():
    exchange_list = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5").json()
    return exchange_list


def user_interface():
    buy_sell = str(input('input buy, sale or else to exit application'))
    if buy_sell == 'buy':
        summ = float(input('input summ to buy '))
        currency = str(input(('input currency to exchange ')))
        return process(currency, summ, buy_sell)
    elif buy_sell == 'sale':
        currency = str(input(('input currency to exchange ')))
        summ = float(input('input summ to exchange from '))
        return process(currency, summ, buy_sell)
    else:
        exit(0)

def process(currency, summ, buy_sell):
    course = get_values()
    for i in range(len(course)):
        if course[i].get('ccy') == str(currency):
            buy_exchange = course[i].get('buy')
            sale_exchange = course[i].get('sale')
            if buy_sell == 'buy':
                return float(float(sale_exchange) * summ)
            else:
                return float(summ * float(buy_exchange))
        elif str(currency) == 'UAH':
            return summ

while True:
    print(user_interface())
