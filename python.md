# Python

# インストール
- numpy       : "python -m pip install numpy"
- matplotlib  : "python -m pip install matplotlib"
- Jupyter     : "python -m pip install jupyter"

# インストールのリスト
"python -m pip list"

# 作業フォルダ
[python folder](C:\MEDC\Python.git)

# Jupyter 起動
- jupyter notebook



----------------------------------------
# PythonからSlackに投稿する
[pythonからslackに投稿する](http://qiita.com/shtnkgm/items/4f0e4dcbb9eb52fdf316)

# slackweb をインストール
- "pip install skackweb"

# slack で　incoming webhookの設定
- "Add Incoming WebHooks Integration"

# post_slack.py
import slackweb

slack = slackweb.Slack(url="コピーしたwebhook URL")
slack.notify(text="hogehoge")

----------------------------------------
# GUI
- [PyQt](http://myenigma.hatenablog.com/entry/2016/01/24/113413)

----------------------------------------
# exeのビルド
- [PyInstller](http://retrofocus28.blogspot.jp/2013/10/pyinstallerexe.html)

