import requests
import json
import keyboards as nav

usdt = 1
#находим курс криптовалюты по отношению к доллару
def get_coin_price(symb):
    base = 'https://fapi.binance.com'
    path = '/fapi/v1/premiumIndex'
    url = base + path
    pare = symb + 'usdt'
    param = {'symbol': pare , 'markPrice' : f'{symb}usdt'}
    r = requests.get(url, params=param)
    cena = r.json()
    return(cena['markPrice'])

def luna_stoimost():
    base = 'https://fapi.binance.com'
    path = '/fapi/v1/premiumIndex'
    url = base + path
    r = requests.get(url, params={'symbol': 'lunausdt', 'markPrice': 'lunausdt'})
    cena = r.json()
    return (print(cena['markPrice']))


