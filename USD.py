import sys
import logging
import math
import urllib
import schedule
import time

from FTX.client import Client
from FTX.config import *
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


def lending(client):

    balance = client.get_private_wallet_single_balance("USD")['total']
    # client.set_private_margin_lending_offer('USD', usd_available, 2.283e-05)
    rate = client.get_private_margin_lending_rates()
    for i in range(len(rate)):
        if rate[i]['coin'] == "USD":
            USD_rate = rate[i]['estimate']
            print(rate[i]['estimate'])
    client.set_private_margin_lending_offer("USD", balance, USD_rate)


schedule.every().minute.at(":50").do(lending, client)
# schedule.every(0.1).minutes.do(lending, client)
while True:
    schedule.run_pending()
    time.sleep(1)
