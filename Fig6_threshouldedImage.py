import pydicom
import numpy as np
import matplotlib.pyplot as plt

# Read DICOM data
filename = pydicom.data.get_testdata_file("CT_small.dcm")
dc = pydicom.dcmread(filename)

# Thresholding -> imBone
threshold = 1400
imBone = np.zeros(dc.pixel_array.shape)
for x in range(0, dc.pixel_array.shape[0]):
    for y in range(0, dc.pixel_array.shape[1]):
        if dc.pixel_array[x, y] >= threshold:
            imBone[x, y] = 1
        else:
            imBone[x, y] = 0

# Show imBone
plt.imshow(imBone, cmap=plt.cm.gray)
plt.show()
