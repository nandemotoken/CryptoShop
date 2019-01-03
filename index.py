#!/user/bin/env python
# -*- coding: utf-8 -*-
from bottle import route , run , static_file , request
import pycoin
import pycoin.key.BIP32Node
import re



@route('/')
def index():
  html = """
<h1>ブロックチェーンエンジニア集中講座 第4週</h1>
</br>[TestnetBTC Shop]
</br>　<a href="/data/XTN/1">商品1</a>
</br>　<a href="/data/XTN/2">商品2</a>
</br>　<a href="/data/XTN/3">商品3</a>
</br>
</br>[DOGE shop]
</br>　<a href="/data/DOGE/11">商品11</a>
</br>　<a href="/data/DOGE/12">商品12</a>
</br>　<a href="/data/DOGE/13">商品13</a>
</br>
</br>[DASH shop]
</br>　<a href="/data/DASH/101">商品101</a>
</br>　<a href="/data/DASH/102">商品102</a>
</br>　<a href="/data/DASH/103">商品103</a>
</br>
</br>
<h3>言語：Python
BIP32ライブラリ：pycoin
フレームワーク：bottle</br>
作者：大塚大輔(nandemotoken@gmail.com)</h3>
"""
  return html



@route('/data/<currency:re:.*>/<filename:re:.*\.jpg>')
def send_image(currency , filename):
    return static_file(filename , root=('/root/CriptoShop/data/'+ currency) , mimetype='image/jpg')


@route('/data/<currency:re:.*>/<filename:re:..?.?>')
def item(currency , filename):
    item = []
#    return filename
    with open('data/'+currency+'/'+filename+'.item') as f:
        for line in f:
            item.append(line)
    pubkey = ""
    with open('data/'+currency+'/pubkey') as k:
        pubkey = k.readlines()[0]
    
    address = pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubkey.strip()).subkey(int(item[5])).address()
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
    return html


@route('/data/<currency:re:.*>/<filename:re:..?.?>', method="POST")
def order(currency , filename):
    user_name = request.forms.get("user_name")
    with open('data/'+ currency + "/" +  filename + '.item') as f1:
        data = f1.read()
    data = data.replace("在庫あり","入金確認中")
    data = data.replace("注文者：大塚大輔", "注文者：" + user_name )

    with open('data/'+ currency + "/" +  filename + '.item' , "w" ) as f2:
        f2.write(data)

    pubkey = ""
    with open('data/'+currency+'/pubkey') as k:
        pubkey = k.readlines()[0]

    item = []
    with open('data/'+ currency + "/" +  filename + '.item') as f3:
        for line in f3:
            item.append(line)
        address = pycoin.key.BIP32Node.BIP32Node.from_wallet_key(pubkey.strip()).subkey(int(item[5])).address()

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


@route('/data/<currency:re:.*>/cancel<filename:re:..?.?>', method="POST")
def cancel(currency , filename):
    with open('data/'+ currency + "/" + filename + '.item') as f1:
        data = f1.read()
    data = data.replace("入金確認中","在庫あり")
    data = re.sub('注文者：.*' , '注文者：大塚大輔' , data)

    with open('data/'+ currency + "/" +  filename + '.item' , "w" ) as f2:
        f2.write(data)

    html = """キャンセルしました。</br><a href="/">TOPに戻る</a>"""
    return html


run(host='150.95.149.179' , port=8080 , debug=True)



