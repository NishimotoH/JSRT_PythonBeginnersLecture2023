# 日本放射線技術学会雑誌 (JSRT) 教育講座 「Python で遊ぼう！ (???)」 その1 プログラム

## 概要

日本放射線技術学会雑誌 Vol. ?? No. ?? (2023??) 教育講座で使用したプログラムのソースコード (1~3) と、それを少し発展させたもの (4,5) です。

## ファイル

* 1_DicomShow.py
  * pydicom に含まれるサンプルの DICOM ファイルを読み出して、 tag を表示し、画像を表示するプログラムです。
  * 雑誌掲載プログラム
* 2_T1shim.py
  * T1 回復曲線をシミュレーションするためのプログラムです。
  * 雑誌掲載プログラム
* 3_threshouldedImage.py
  * pydicom に含まれるサンプル画像を閾値処理し、結果を表示するためのプログラムです。
  * 雑誌掲載プログラム
* 4_DicomShow-4panels.py
  * pydicom に含まれるサンプル画像のヒストグラム、手動閾値処理、大津らの手法による閾値処理の結果を示すプログラムです。
* 5_timeEval.py
  * for 文中にある if 文中の省略可能な else 文の有無と、そもそも for 文を使わない場合の処理速度の比較。

## 動作環境

Python 11.1
* pydicom
* numpy
* matplotlib
* opencv-python

## 使い方
IDLE のエディターにコピーじて実行してください。
