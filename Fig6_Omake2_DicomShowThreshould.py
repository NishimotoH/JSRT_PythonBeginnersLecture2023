# Fig4_DicomShow.py と Fig6_DicomShowThreshould.py の結果を
# すべて一つの Window で表示させるプログラム。
# 左上：Fig4
# 左下：Fig6
# 右上：ヒストグラム
# 右下：Fig4 に対して openCV の大津の2値化法を適用した結果

import pydicom
import numpy as np
import matplotlib.pyplot as plt
import cv2  # 事前に"pip install opencv-python"を実行して cv2 を使えるようにしてください

# DICOM データの読み込み
filename = pydicom.data.get_testdata_file("CT_small.dcm")
dc = pydicom.dcmread(filename)
print(dc)

# なんとなく指定した閾値による手動の画像2値化
threshould = 1400
imBone = np.zeros(dc.pixel_array.shape)
for x in range(0, dc.pixel_array.shape[0]):
    for y in range(0, dc.pixel_array.shape[1]):
        if dc.pixel_array[x, y] > threshould:
            imBone[x, y] = 1
        else:
            imBone[x, y] = 0

# 大津の手法による画像２値化
imUint16 = dc.pixel_array.astype(np.uint16)
thOtsu, imOtsu = cv2.threshold(imUint16, 0, 255, cv2.THRESH_OTSU)
print("Threshould: " + str(thOtsu))

# 1つの figure に 2x2 に分割した画像を提示するための準備
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

# 2x2 の各パネルに対して表示させる画像を指定する
ax1.imshow(dc.pixel_array, cmap=plt.cm.gray) # オリジナル画像
ax2.hist(np.ravel(dc.pixel_array), bins=100) # ヒストグラム
ax3.imshow(imBone, cmap=plt.cm.gray) # 手動の2値化
ax4.imshow(imOtsu, cmap=plt.cm.gray) # 大津の手法による2値化

# 画像を表示する
plt.show()
