#!/user/bin/env python
# -*- coding: utf-8 -*-
from bottle import route , run , static_file
import pycoin
import pycoin.key.BIP32Node

#bitcoin mainnet pubkey
with open('data/pubBTC') as f:
  lines = []
  for line in f:
    lines.append(line)
pubbtc=lines[0]

#bitcoin testnet pubkey
with open('data/pubXTN') as f:
  lines = []
  for line in f:
    lines.append(line)
pubxtn=lines[0]

#doge mainnet pubkey
with open('data/pubDOGE') as f:
  lines = []
  for line in f:
    lines.append(line)
pubdoge=lines[0]

#dash mainnet pubkey
with open('data/pubDASH') as f:
  lines = []
  for line in f:
    lines.append(line)
pubdash=lines[0]

#print(pubbtc)
#print(pubxtn)
#print(pubdoge)
#print(pubdash)


@route('/')
def page1():
  return "Bottle Working"

@route('/coin')
def page2():
  return pycoin.version


@route('/0')
def page3():
  item = [] 
  with open('data/0.item') as f:
    for line in f:
      item.append(line)
  html = """
<h1>{0}</h1>
<h2>{1}</h2>
<form name="buy" method="POST" action={5}>
<input type="text" placeholder="slackユーザ名を入力" name="user_name" required />
<input type="submit" value="購入" />
</form>
支払いアドレス：{6}
</br>
<img src="{2}">
</br><a href="/">TOPに戻る</a>
""".format(item[0],item[1],item[2],item[3],item[4],item[5],pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubbtc.strip()).subkey(int(item[5])).address())
#  print(item[2])
#  print(pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubbtc.strip()).subkey(0))
#  print(pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubbtc.strip()).subkey(int(item[5])).address())
  return html

@route('/0', method="POST")
def order():
  item = []
  with open('data/0.item') as f:
    for line in f:
      item.append(line)

  html = """
<h1>{0}を注文しました</h1>
slackにてお渡し方法をご確認させてください。</br>
　・HashHub対面受け渡し など</br></br>

支払いアドレス：{6}
</br>
<img src="{2}">
<form name="buy" method="POST" action=cancel{5}>
<input type="submit" value="注文キャンセル" />
</form>
</br><a href="/">TOPに戻る</a>
""".format(item[0],item[1],item[2],item[3],item[4],item[5],pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubbtc.strip()).subkey(int(item[5])).address())
  return html

@route('/cancel0' , method="POST")
def cancel():
  item = []
  with open('data/0.item') as f:
    for line in f:
      item.append(line)

  html = """キャンセルしました。</br><a href="/">TOPに戻る</a>"""
  return html


@route('/data/<filename:re:.*\.jpg>')
def send_image(filename):
  return static_file(filename , root='/root/CriptoShop/data' , mimetype='image/jpg')


@route('/1')
def item1():
  item = """<h1>StrongHands Chocolate1</h1>
<h2>price:0.00001BTC</h2>
</br>
<img src="http://150.95.177.213:8080/data/1.jpg">
"""
  return item



@route('/2')
def item2():
  item = """<h1>StrongHands Chocolate2</h1>
<h2>price:0.00001BTC</h2>
</br>
<img src="http://150.95.177.213:8080/data/2.jpg">
"""
  return item


run(host='150.95.177.213' , port=8080 , debug=True)






