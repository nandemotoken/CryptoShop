#!/user/bin/env python
# -*- coding: utf-8 -*-
from bottle import route , run , static_file , request
import pycoin
import pycoin.key.BIP32Node
import re


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
def index():
  html = """
<h1>ブロックチェーンエンジニア集中講座 第4週</h1>
</br>[TestnetBTC Shop]
</br>　<a href="/1">商品1</a>
</br>　<a href="/2">商品2</a>
</br>　<a href="/3">商品3</a>
</br>
</br>[DOGE shop]
</br>　<a href="/11">商品11</a>
</br>　<a href="/12">商品12</a>
</br>　<a href="/13">商品13</a>
</br>
</br>[DASH shop]
</br>　<a href="/101">商品101</a>
</br>　<a href="/102">商品102</a>
</br>　<a href="/103">商品103</a>
</br>
</br>
<h3>言語：Python
BIP32ライブラリ：pycoin
フレームワーク：bottle</br>
作者：大塚大輔(nandemotoken@gmail.com)</h3>
"""
  return html

@route('/coin')
def page2():
  return pycoin.version


#@route('/0')
#def sampleitem():
#  item = [] 
#  with open('data/0.item') as f:
#    for line in f:
#      item.append(line)
#  address = pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubxtn.strip()).subkey(int(item[5])).address()
#
#  html = """
#<h1>{0}</h1>
#<h2>{1}</h2>
#<form name="buy" method="POST" action={5}>
#<input type="text" placeholder="slackユーザ名を入力" name="user_name" required />
#<input type="submit" value="購入" />
#</form>
#支払いアドレス：{6}
#</br>
#{3}</br>
#<img src="{2}">
#</br><a href="/">TOPに戻る</a>
#""".format(item[0],item[1],item[2],item[3],item[4],item[5],address)
#  print(item[2])
#  print(pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubbtc.strip()).subkey(0))
#  print(pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubbtc.strip()).subkey(int(item[5])).address())
#  return html

#@route('/0', method="POST")
#def order():
#  user_name = request.forms.get("user_name")
#  print(user_name)

#  with open('data/0.item') as f1:
#    data = f1.read()
#  data = data.replace("在庫あり","入金確認中")
#  data = data.replace("注文者：大塚大輔", "注文者：" + user_name )

#  with open('data/0.item', 'w') as f2:
#    f2.write(data)

#  item = []
#  with open('data/0.item') as f3:
#    for line in f3:
#      item.append(line)
#  address = pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubbtc.strip()).subkey(int(item[5])).address()

#  html = """
#<h1>{0}を注文しました</h1>
#slackにてお渡し方法をご確認させてください。</br>
#　・HashHub対面受け渡し など</br></br>
#
#支払いアドレス：{6}
#</br>
#{4}
#</br>
#<img src="{2}">
#<form name="buy" method="POST" action=cancel{5}>
#<input type="submit" value="注文キャンセル" />
#</form>
#</br><a href="/">TOPに戻る</a>
#""".format(item[0],item[1],item[2],item[3],item[4],item[5],address)
#  return html

#@route('/cancel0' , method="POST")
#def cancel():
#  with open('data/0.item') as f1:
#    data = f1.read()
#  data = data.replace("入金確認中","在庫あり")
#  data = re.sub('注文者：.*' , '注文者：大塚大輔' , data)
#
#  with open('data/0.item', 'w') as f2:
#    f2.write(data)
#
#
#  item = []
#  with open('data/0.item') as f:
#    for line in f:
#      item.append(line)
#
#  html = """キャンセルしました。</br><a href="/">TOPに戻る</a>"""
#  return html


@route('/data/<filename:re:.*\.jpg>')
def send_image(filename):
  return static_file(filename , root='/root/CriptoShop/data' , mimetype='image/jpg')


#@route('/1')
#def item1():
#  item = """<h1>StrongHands Chocolate1</h1>
#<h2>price:0.00001BTC</h2>
#</br>
#<img src="data/1.jpg">
#"""
#  return item



#@route('/2')
#def item2():
#  item = """<h1>StrongHands Chocolate2</h1>
#<h2>price:0.00001BTC</h2>
#</br>
#<img src="data/1.jpg">
#"""
#  return item

@route('/<filename:re:.>')
def item(filename):
  item = []
  with open('data/'+ filename + '.item') as f:
    for line in f:
      item.append(line)
  address = pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubxtn.strip()).subkey(int(item[5])).address()

  html = """
<h1>{0}</h1>
<h2>{1}</h2>
<form name="buy" method="POST" action={5}>
<input type="text" placeholder="slackユーザ名を入力" name="user_name" required />
<input type="submit" value="購入" />
</form>
支払いアドレス：{6}
</br>
{3}</br>
<img src="{2}">
</br><a href="/">TOPに戻る</a>
""".format(item[0],item[1],item[2],item[3],item[4],item[5],address)
#  print(item[2])
#  print(pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubbtc.strip()).subkey(0))
#  print(pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubbtc.strip()).subkey(int(item[5])).address())
  print item[5]
  return html

@route('/<filename:re:.>', method="POST")
def order(filename):
  user_name = request.forms.get("user_name")
  with open('data/'+ filename + '.item') as f1:
    data = f1.read()
  data = data.replace("在庫あり","入金確認中")
  data = data.replace("注文者：大塚大輔", "注文者：" + user_name )

  with open('data/'+ filename + '.item', 'w') as f2:
    f2.write(data)

  item = []
  with open('data/'+ filename + '.item') as f3:
    for line in f3:
      item.append(line)
  address = pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubxtn.strip()).subkey(int(item[5])).address()

  html = """
<h1>{0}を注文しました</h1>
slackにてお渡し方法をご確認させてください。</br>
　・HashHub対面受け渡し など</br></br>

支払いアドレス：{6}
</br>
{4}　
{3}</br>
<img src="{2}">
<form name="buy" method="POST" action=cancel{5}>
<input type="submit" value="注文キャンセル" />
</form>
</br><a href="/">TOPに戻る</a>
""".format(item[0],item[1],item[2],item[3],item[4],item[5],address)
  return html

@route('/cancel<filename:re:.>' , method="POST")
def cancel(filename):
  with open('data/'+ filename + '.item') as f1:
    data = f1.read()
  data = data.replace("入金確認中","在庫あり")
  data = re.sub('注文者：.*' , '注文者：大塚大輔' , data)

  with open('data/'+ filename + '.item', 'w') as f2:
    f2.write(data)


  item = []
  with open('data/'+ filename + '.item') as f:
    for line in f:
      item.append(line)

  html = """キャンセルしました。</br><a href="/">TOPに戻る</a>"""
  return html

@route('/<filename:re:..>')
def item(filename):
  item = []
  with open('data/'+ filename + '.item') as f:
    for line in f:
      item.append(line)
  address = pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubdoge.strip()).subkey(int(item[5])).address()

  html = """
<h1>{0}</h1>
<h2>{1}</h2>
<form name="buy" method="POST" action={5}>
<input type="text" placeholder="slackユーザ名を入力" name="user_name" required />
<input type="submit" value="購入" />
</form>
支払いアドレス：{6}
</br>
{3}</br>
<img src="{2}">
</br><a href="/">TOPに戻る</a>
""".format(item[0],item[1],item[2],item[3],item[4],item[5],address)
#  print(item[2])
#  print(pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubbtc.strip()).subkey(0))
#  print(pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubbtc.strip()).subkey(int(item[5])).address())
  return html

@route('/<filename:re:..>', method="POST")
def order(filename):
  user_name = request.forms.get("user_name")
  with open('data/'+ filename + '.item') as f1:
    data = f1.read()
  data = data.replace("在庫あり","入金確認中")
  data = data.replace("注文者：大塚大輔", "注文者：" + user_name )

  with open('data/'+ filename + '.item', 'w') as f2:
    f2.write(data)

  item = []
  with open('data/'+ filename + '.item') as f3:
    for line in f3:
      item.append(line)
  address = pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubdoge.strip()).subkey(int(item[5])).address()

  html = """
<h1>{0}を注文しました</h1>
slackにてお渡し方法をご確認させてください。</br>
　・HashHub対面受け渡し など</br></br>

支払いアドレス：{6}
</br>
{4}　
{3}</br>
<img src="{2}">
<form name="buy" method="POST" action=cancel{5}>
<input type="submit" value="注文キャンセル" />
</form>
</br><a href="/">TOPに戻る</a>
""".format(item[0],item[1],item[2],item[3],item[4],item[5],address)
  return html

@route('/cancel<filename:re:..>' , method="POST")
def cancel(filename):
  with open('data/'+ filename + '.item') as f1:
    data = f1.read()
  data = data.replace("入金確認中","在庫あり")
  data = re.sub('注文者：.*' , '注文者：大塚大輔' , data)

  with open('data/'+ filename + '.item', 'w') as f2:
    f2.write(data)


  item = []
  with open('data/'+ filename + '.item') as f:
    for line in f:
      item.append(line)

  html = """キャンセルしました。</br><a href="/">TOPに戻る</a>"""
  return html



@route('/<filename:re:...>')
def item(filename):
  item = []
  with open('data/'+ filename + '.item') as f:
    for line in f:
      item.append(line)
  address = pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubdash.strip()).subkey(int(item[5])).address()

  html = """
<h1>{0}</h1>
<h2>{1}</h2>
<form name="buy" method="POST" action={5}>
<input type="text" placeholder="slackユーザ名を入力" name="user_name" required />
<input type="submit" value="購入" />
</form>
支払いアドレス：{6}
</br>
{3}</br>
<img src="{2}">
</br><a href="/">TOPに戻る</a>
""".format(item[0],item[1],item[2],item[3],item[4],item[5],address)
#  print(item[2])
#  print(pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubbtc.strip()).subkey(0))
#  print(pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubbtc.strip()).subkey(int(item[5])).address())
  return html

@route('/<filename:re:...>', method="POST")
def order(filename):
  user_name = request.forms.get("user_name")
  with open('data/'+ filename + '.item') as f1:
    data = f1.read()
  data = data.replace("在庫あり","入金確認中")
  data = data.replace("注文者：大塚大輔", "注文者：" + user_name )

  with open('data/'+ filename + '.item', 'w') as f2:
    f2.write(data)

  item = []
  with open('data/'+ filename + '.item') as f3:
    for line in f3:
      item.append(line)
  address = pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubdash.strip()).subkey(int(item[5])).address()

  html = """
<h1>{0}を注文しました</h1>
slackにてお渡し方法をご確認させてください。</br>
　・HashHub対面受け渡し など</br></br>

支払いアドレス：{6}
</br>
{4}　
{3}</br>
<img src="{2}">
<form name="buy" method="POST" action=cancel{5}>
<input type="submit" value="注文キャンセル" />
</form>
</br><a href="/">TOPに戻る</a>
""".format(item[0],item[1],item[2],item[3],item[4],item[5],address)
  return html

@route('/cancel<filename:re:...>' , method="POST")
def cancel(filename):
  with open('data/'+ filename + '.item') as f1:
    data = f1.read()
  data = data.replace("入金確認中","在庫あり")
  data = re.sub('注文者：.*' , '注文者：大塚大輔' , data)

  with open('data/'+ filename + '.item', 'w') as f2:
    f2.write(data)


  item = []
  with open('data/'+ filename + '.item') as f:
    for line in f:
      item.append(line)

  html = """キャンセルしました。</br><a href="/">TOPに戻る</a>"""
  return html





run(host='150.95.177.213' , port=8080 , debug=True)




