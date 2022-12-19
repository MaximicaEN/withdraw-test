import time
import ccxt
from termcolor import cprint
from web3 import Web3
import random

def check_balance(address, number, web3):
    try:
        balance = web3.eth.get_balance(web3.toChecksumAddress(address))
        humanReadable = web3.fromWei(balance,'ether')
        cprint(f'{number}. {address} : {humanReadable}', 'white')

    except Exception as error:
        cprint(f'{number}. {address} = {error}', 'red')

def binance_withdraw(address, amount_to_withdrawal, symbolWithdraw, network, API_KEY, API_SECRET):

    account_binance = ccxt.binance({
        'apiKey': API_KEY,
        'secret': API_SECRET,
        'enableRateLimit': True,
        'options': {
            'defaultType': 'spot'
        }
    })

  

    # RPC = 'https://mainnet.optimism.io'
    # RPC = 'https://arb1.arbitrum.io/rpc'
    # RPC = 'https://polygon-rpc.com'
    # RPC = 'https://bsc-dataseed.binance.org'
    # RPC = 'https://arb1.arbitrum.io/rpc'
    RPC = 'https://rpc.flashbots.net' #ETH

    web3 = Web3(Web3.HTTPProvider(RPC))

    # api_keys of binance
    API_KEY = "KEY"
    API_SECRET = "KEY"

   

