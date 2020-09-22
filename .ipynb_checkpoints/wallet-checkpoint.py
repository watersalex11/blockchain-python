from constants import *
import subprocess
import json
import os
from dotenv import load_dotenv
load_dotenv()

# generate mnemonic
#12_word = "point guess object game pet torch tired three hen breeze unit venture"
mnemonic = os.getenv('MNEMONIC', '12_word ')
# The php command that will get our derived addresses
# --coin ETH will derive ethereum addresses
# --format=json changes the terminal output to json format
def derive_wallets():
    command = 'php derive -g --mnemonic="12_word" --cols=path,address,privkey,pubkey --format=json --coin = ETH --numderive = 3' 
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    keys = json.loads(output)
    # print all the addresses
    print(keys)

    # print out the first address
    print(keys[0]['address'])