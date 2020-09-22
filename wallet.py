from constants import *
import subprocess
import json
import os
from web3 import Web3
from dotenv import load_dotenv
from bit import PrivateKeyTestnet
load_dotenv()

# generate mnemonic
#12_word = "point guess object game pet torch tired three hen breeze unit venture"
words = os.getenv('12_word ')
# The php command that will get our derived addresses
# --coin ETH will derive ethereum addresses
# --format=json changes the terminal output to json format
def derive_wallets(words,coin,numderive):
    command = f' php hd-wallet-derive/hd-wallet-derive.php  -g --mnemonic="{words}" 
    --cols=path,address,privkey,pubkey --format=json --coin = {coin} --numderive = {numderive}' 
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    keys = json.loads(output)
    # print all the addresses
    print(keys)

    # print out the first address
    print(keys[0]['address'])
coins = #need to derive ETH and BTCTEST 
#
def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        account= Account.privateKeyToAccount(priv_key)
    else coin = BTCTEST:
        account=PrivateKeyTestnet(priv_key)    

def create_tx(coin, account, to ,amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
    return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
        "chainID":#?
    }
    if coin = BTCTEST:
        return {'privateKeyTestnet.prepare_transaction(account.address,[(to, amount, BTC)]}



def sent_tx(coin, account, to, amount):
    raw_tx=create_tx(coin, account, to, amount)
    signed_tx=account.sign_transaction(raw_tx)
    
    #after signing send to network for ETH
    if coin = ETH:
        result = w3.eth.sendRawTransaction(signed.rawTransaction)
    #after signing send to network for BTCTEST
    else:
        result= NetworkAPI.broadcast_tx_testnet(signed)

#Local PoA Eth transaction
geth -- datadir nodeX init networkname.json
from web3.middleware import geth_poa_middleware
w3.middleware_onion.inject(geth_poa_middleware, layer = 0)
    