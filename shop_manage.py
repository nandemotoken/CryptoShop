#!/user/bin/env python
# -*- coding: utf-8 -*-

import requests
from pycoin.serialize import h2b
import pycoin.key.BIP32Node
import json
from pycoin.tx.Tx import Tx
from pycoin.tx.tx_utils import sign_tx
from pycoin.tx.tx_utils import create_tx


#--------------利用前設定---------------
#利用する暗号通貨。XTN(BTCTestNet) ,DOGE ,DASH
my_netcode = "DOGE"

#『管理用の拡張秘密鍵を作成』で決めた文字列
private_key_string = ""

#送信先アドレス
send_to_address = ""

#商品番号(支払いアドレスと対応する)
item_number = 1


#--------------プログラム---------------


private_key_master = pycoin.key.BIP32Node.BIP32Node.from_master_secret(h2b(private_key_string), netcode=my_netcode)

item_address = private_key_master.subkey(item_number).address()

print("Item address:" + item_address + "\nsend_to: " +send_to_address )

is_ok = raw_input("続けますか?(y)")

if is_ok != "y":
    print("終了")
    exit()


chain_so_get_tex_unspent_dic = {
        "XTN":"https://chain.so/api/v2/get_tx_unspent/BTCTEST/" , 
        "DOGE":"https://chain.so/api/v2/get_tx_unspent/DOGE/" , 
        "DASH":"https://chain.so/api/v2/get_tx_unspent/DASH/"
        }

chain_so_get_tex_unspent = chain_so_get_tex_unspent_dic[my_netcode]

chain_so_tx_dic = {
        "XTN":"https://chain.so/api/v2/tx/BTCTEST/" ,
        "DOGE":"https://chain.so/api/v2/tx/DOGE/" ,
        "DASH":"https://chain.so/api/v2/tx/DASH/"
        }

chain_so_tx = chain_so_tx_dic[my_netcode]

chain_so_send_tx_dic = {
        "XTN":"https://chain.so/api/v2/send_tx/BTCTEST/" ,
        "DOGE":"https://chain.so/api/v2/send_tx/DOGE/" ,
        "DASH":"https://chain.so/api/v2/send_tx/DASH/"
        }

chain_so_send_tx = chain_so_send_tx_dic[my_netcode]


def check_my_tx(resp_tx):
        for i ,  o in enumerate(json.loads(resp_tx.text)["data"]["outputs"]):
                    if o["address"] == item_address:
                                    return i


resp = requests.get( chain_so_get_tex_unspent + item_address )

resp_tx = requests.get( chain_so_tx + json.loads(resp.text)["data"]["txs"][0]["txid"] )

tx = Tx.from_hex(json.loads(resp_tx.text)["data"]["tx_hex"])

spendable = tx.tx_outs_as_spendable()[check_my_tx(resp_tx)]

tx = create_tx([spendable] , [send_to_address] )

sign_tx(tx , wifs=[private_key_master.subkey(item_number).wif()] , netcode=my_netcode)

pos = requests.post(chain_so_send_tx , { 'tx_hex':tx.as_hex() } )




