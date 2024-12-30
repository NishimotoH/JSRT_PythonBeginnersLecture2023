# Fig6_DicomShowThreshould.py の処理時間を比較するプログラム
# 最初にオリジナル、else 削除、if 文と for 文の削除、の3つの方法で比較する。
# 作者環境では1.08秒、1.02秒、0.00秒であった。
# 次に 5000x5000 の行列で同様の処理を行う。
# 作者環境では16.00秒、10.50秒、0.03秒であった。

import pydicom
import numpy as np
import time

# DICOM データの読み込み
filename = pydicom.data.get_testdata_file("CT_small.dcm")
dc = pydicom.dcmread(filename)

# 画像2値化の閾値設定
threshold1 = 1400

print("====================")

# オリジナルの手法
time_sta = time.time()
imBone1 = np.zeros(dc.pixel_array.shape)
for x in range(0, dc.pixel_array.shape[0]):
    for y in range(0, dc.pixel_array.shape[1]):
        if dc.pixel_array[x, y] >= threshold1:
            imBone1[x, y] = 1
        else:
            imBone1[x, y] = 0
time_end = time.time()
tim = time_end - time_sta
print("DICOM original: " + str(format(tim, ".2f")))

# 1秒間プログラムの実行を停止する
time.sleep(1.0)

# "else"を削除した手法
time_sta = time.time()
imBone2 = np.zeros(dc.pixel_array.shape)
for x in range(0, dc.pixel_array.shape[0]):
    for y in range(0, dc.pixel_array.shape[1]):
        if dc.pixel_array[x, y] >= threshold1:
            imBone2[x, y] = 1
time_end = time.time()
tim = time_end - time_sta
print('DICOM No "else": ' + str(format(tim, ".2f")))

time.sleep(1.0)

# "if"と"for"を削除した手法
time_sta = time.time()
imBone3 = dc.pixel_array > threshold1
time_end = time.time()
tim = time_end - time_sta
print('DICOM No "if" and "for": ' + str(format(tim, ".2f")))

time.sleep(1.0)

# 5,000 x 5,000 の行列で同じことを試す。行列の各要素の値は random 。
bsl = np.random.randint(0, 100, (5000, 5000))
threshold2 = 50
print("====================")
print("Big size list. Mat: " + str(bsl.shape[0]) + " x " + str(bsl.shape[1]))

# オリジナルの手法
time_sta = time.time()
bsl1 = np.zeros(bsl.shape)
for x in range(0, bsl.shape[0]):
    for y in range(0, bsl.shape[1]):
        if bsl[x, y] >= threshold2:
            bsl1[x, y] = 1
        else:
            bsl1[x, y] = 0
time_end = time.time()
tim = time_end - time_sta
print("Original: " + str(format(tim, ".2f")))

time.sleep(1.0)

# "else"を削除した手法
time_sta = time.time()
bsl2 = np.zeros(bsl.shape)
for x in range(0, bsl.shape[0]):
    for y in range(0, bsl.shape[1]):
        if bsl[x, y] >= threshold2:
            bsl2[x, y] = 1
time_end = time.time()
tim = time_end - time_sta
print('No "else": ' + str(format(tim, ".2f")))

time.sleep(1.0)

# "if"と"for"を削除した手法
time_sta = time.time()
bsl3 = bsl > threshold2
time_end = time.time()
tim = time_end - time_sta
print('No "if" and "for": ' + str(format(tim, ".2f")))

print("====================")

# プログラム終了後にコマンドウインドウが閉じないようにするために、
# 任意のキーを押せばプログラムが終了するようにする。
print("Please press any key if you want to finish this program.")
input()
