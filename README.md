# JSRT (日本放射線技術学会雑誌) 教育講座 「Python で遊ぼう！ (???)」 その1 プログラム

## 概要

日本放射線技術学会雑誌 Vol. ?? No. ?? (2023??) 教育講座で使用したプログラムのソースコードです。

## ファイル

* DicomShow.py
  * pydicom に含まれるサンプルの DICOM ファイルを読み出して、 tag を表示し、画像を表示するプログラムです。
* T1shim.py
  * T1 回復曲線をシミュレーションするためのプログラムです。
* threshouldedImage.py
  * pydicom に含まれるサンプル画像を閾値処理し、結果を表示するためのプログラムです。
* DicomShow-4panels.py
  * pydicom に含まれるサンプル画像のヒストグラム、手動閾値処理、大津らの手法による閾値処理の結果を示すプログラムです。

## 動作環境

Python 11.0
* pydicom
* numpy
* matplotlib
* opencv-python

## 使い方
IDLE のエディターにコピーじて実行してください。
