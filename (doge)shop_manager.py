import requests
from pycoin.serialize import h2b
import pycoin.key.BIP32Node
import json
from pycoin.tx.Tx import Tx
from pycoin.tx.tx_utils import sign_tx
from pycoin.tx.tx_utils import create_tx

#　　※管理用PCで『管理用の拡張秘密鍵を作成(★)』で決めた文字列↓
d = pycoin.key.BIP32Node.BIP32Node.from_master_secret(h2b("aaaaaaaa"), netcode='DOGE')
#　　※自身のコインアドレス↓
send_to_address = "DNBLH28hqsWTrVuEQHRSUqCyinnU1tQscM"

#　　　　　　　　　　　　　　　↓商品番号
doge_shop_address13 = d.subkey(13).address()
resp6 = requests.get('https://chain.so/api/v2/get_tx_unspent/DOGE/'+doge_shop_address13)
resp6_tx = requests.get('https://chain.so/api/v2/tx/DOGE/' + json.loads(resp6.text)["data"]["txs"][0]["txid"] )
def check_my_tx(resp_tx):
    for i ,  o in enumerate(json.loads(resp_tx.text)["data"]["outputs"]):
        if o["address"] == doge_shop_address13:
            return i
tx6 = Tx.from_hex(json.loads(resp6_tx.text)["data"]["tx_hex"])
spendable6 = tx6.tx_outs_as_spendable()[check_my_tx(resp6_tx)]
tx6 = create_tx([spendable6] , [send_to_address] )
sign_tx(tx6 , wifs=[d.subkey(13).wif()],netcode="DOGE")
pos6 = requests.post("https://chain.so/api/v2/send_tx/DOGE", { 'tx_hex':tx6.as_hex() } )

