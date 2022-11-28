import pydicom
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Read DICOM data
filename = pydicom.data.get_testdata_file("CT_small.dcm")
dc = pydicom.dcmread(filename)
print(dc)

# Thresholding to extract bone
threshould = 1400
imBone = np.zeros(dc.pixel_array.shape)
for x in range(0, dc.pixel_array.shape[0]):
    for y in range(0, dc.pixel_array.shape[1]):
        if dc.pixel_array[x, y] > threshould:
            imBone[x, y] = 1
        else:
            imBone[x, y] = 0

# Thresholding by Otsu's method
imUint16 = dc.pixel_array.astype(np.uint16)
thOtsu, imOtsu = cv2.threshold(imUint16, 0, 255, cv2.THRESH_OTSU)
print("Threshould: " + str(thOtsu))

# Prepare a figure with 2x2 panels
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

# Set images for each panels
ax1.imshow(dc.pixel_array, cmap=plt.cm.gray)
ax2.hist(np.ravel(dc.pixel_array), bins=100)
ax3.imshow(imBone, cmap=plt.cm.gray)
ax4.imshow(imOtsu, cmap=plt.cm.gray)

# Drawing the figure
plt.show()
