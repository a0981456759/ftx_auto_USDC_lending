import sys
import logging
import math
import urllib
import schedule
import time

from FTX.client import Client

logging.basicConfig(
    handlers=[logging.StreamHandler(
        sys.stdout), logging.FileHandler('log.txt')],
    level=logging.INFO,
    format='[%(asctime)s %(levelname)-8s] %(message)s',
    datefmt='%Y%m%d %H:%M:%S',
)
INPUT_YOUR_API_KEY1 = input('INPUT_YOUR_MAIN_ACCOUNT_API_KEY: ')
INPUT_YOUR_API_SECRET1 = input('INPUT_YOUR_MAIN_ACCOUNT_API_SECRET: ')
INPUT_YOUR_SUBACCOUNT_NAME1 = input('INPUT_YOUR_SUB_ACCOUNT_NAME: ')
client = Client(INPUT_YOUR_API_KEY1, INPUT_YOUR_API_SECRET1,
                INPUT_YOUR_SUBACCOUNT_NAME1)
coin = input('INPUT_YOUR_LENDING_COIN: ')


def lending(client, coin):

    balance = client.get_private_wallet_single_balance(coin)['total']
    # client.set_private_margin_lending_offer('USD', usd_available, 2.283e-05)
    rate = client.get_private_margin_lending_rates()
    for i in range(len(rate)):
        if rate[i]['coin'] == coin:
            USD_rate = rate[i]['estimate']
            print(rate[i]['estimate'])
    client.set_private_margin_lending_offer(coin, balance, USD_rate)


schedule.every().hour.at(":50").do(lending, client, coin)
# schedule.every(0.1).minutes.do(lending, client)
while True:
    schedule.run_pending()
    time.sleep(1)
