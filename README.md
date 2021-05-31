# Discord bot 「 Lyla 」
「より自然な人間らしさ」を主体においたchatbot　定期的に機能追加

:

概要
* Windows+VSCodeで開発
* uidでユーザーの情報を収集し成長するチャットボット
* 占い機能や検索機能などの+αの機能有
* discord developersから

:

実装済み
* 挨拶に対するランダムな返答
* 天気予報
* 占い
* メンションと名前に対する返答
* １２桁のランダム整数作成
* sha256を使った秘密鍵作成
* グーグル検索
* ニュース検索
* 保存してある画像やテキストを出力
* ユーザーの情報を日時と共に保存
* デーモン化

実装予定
* 機械学習
* 音声認識
* 画像認識

windows10での起動　　

$ py -3 discordbot.py

Ubuntu + Rloginでの起動&デーモン化

起動：          $ sudo systemctl start discordbot_lyla.service 
再起動：        $ sudo systemctl restart discordbot_lyla.service 
停止：          $ sudo systemctl stop discordbot_lyla.service
ステータス確認： $ sudo systemctl status discordbot_lyla.service

エラーログも含め、ログは /var/log/syslog 

$ sudo tail -f  /var/log/syslog