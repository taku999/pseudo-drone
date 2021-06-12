# pseudo-drone
test program for showing map
# 端末位置を地図表示するjavascriptのテスト環境  

## 機能

- jsonの端末情報をwebsocketで送信して、leaflet+openstreermapで地図に表示する。  
<br>

## 環境構築  

- Windows(業務用PCを除く)  
- javascriptはCDNを使用するので、モジュールインストール不要  
- pythonは下記のモジュールをインストールしておくこと。  
  - tornado  
<br>

## 構成  

- 下記のファイルを同一ディレクトリに置く。  
  - genJson.py:jsonファイル生成
  - server.py:サーバ
  - leaflet_echo_ws.html: leaflet+openstreetmapを使用したクライアント  

<br>

## 動作確認方法  

1. server.pyを起動する。  
2. leaflet_echo_ws.htmlを開く。  
3. genjson.pyを起動する。  
<br>

## 追加・修正履歴  

- 2020.12.5

  試験：環境をubuntuから実行してテスト  
  結果：OK  

- 2020.12.7

  - グラフをマルチ化  
  - genjson.py：5台分の情報に変更  
  - server.py：５台分の情報を転送  
  - displayMulti.html：４グラフを表示  

- 2020.12.8

  - 地図表示を追加(leaflet,BSD-2-Clause)  
  - スタイルはbootstrapを使用（MIT License）

- 2020.12.9  
  - bootstrapを追加  
    - component>buttons  
    - layout>Containers  
    - utilities>flex>Justify content  
    - utilities?Spacing  
  
- 2020.12.10  
  - TIPS:ubuntu起動後、下記を実行でgenjson.py実行  
        ```$ source cdwrok.sh```  

- 2020.12.11  
  - 追加：leafletを使ったリアルタイム表示のサンプルを追加  
    - leaflet.html  
    - leaflet_echo.html  
    - leaflet_echo_ws.html(上記+websocket)  

- 2020.12.16
  - 修正：jqueryのCDNが間違っていたので修正した。
  - 追加：connection.onmessageに表示処理を追加した。

- 2020.12.18
  - 修正：genjsonで生成する位置情報を少しずつ動かすようにした  
  - 追加：javascriptが受信したJSONを文字列として表示した。  

```javascript:JSONデータ表示
  　　　print_first(JSON.stringify(e.data));  
```

- 2020.12.24  
  - 記録：onmessageの中でマーカーを発生できない。(エラーは出ない)  
            onmessageの外でマーカーを発生させ、onmessageの中でsetLatLngすると、
            マーカーは残るが、地図が消える。  

- 2021.01.03  
  - 修正：latLngの設定時にlatとlngが逆になっていた  
  - 修正：genjsonのlatとlngの加算数が小さすぎて位置の変化がわからなかったので大きくした  

- 2021.01.04  
  - 修正：マーカーが追加されていくので、一度削除してからマーカーを置くように修正  

## 参考資料

- [ドローン操作システムを作ろう](https://qiita.com/hsgucci/items/86eedb5555b4234ee0e7)  
- [leafletを使ってみた](http://dotnsf.blog.jp/archives/1068371516.html)  
- [leafletドキュメント](https://leafletjs.com/)  
