# Python で OpenCV
- 参考URL:<http://opencv.blog.jp/python/使い方>

----------------------------------------
# セットアップ (Python通常版を使う方法)
- Python へ NumPy をインストールする
  - 参考URL:<http://programming.blogo.jp/python/numpy>
  - NumPy をダウンロード -> 解凍 -> コマンドプロンプトにて "python setup.py install"
  - pipインストール済みなら、
    "pip install numpy"が楽

- OpenCV のインストール
  - 参考URL:<http://opencv.blog.jp/python/ver3_install>
  - OpenCV をダウンロード -> 解凍

- Python用 OpenCVモジュールを入手
  - cv.pyd
  - <C:\Program Files (x86)\OpenCV2.2\Python2.7\Lib\site-packages>

- OpenCVをPythonへインストール
  - cv.pyd を 下記へコピー
  - <C:\Python27\Lib\site-packages>


----------------------------------------
# 画像読み込み

import numpy as np
import cv

img = cv.imread('hoge.png', 0)
