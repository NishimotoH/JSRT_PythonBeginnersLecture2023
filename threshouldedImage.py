import pydicom
import numpy as np
import matplotlib.pyplot as plt

# Read DICOM data
filename = pydicom.data.get_testdata_file("CT_small.dcm")
dc = pydicom.dcmread(filename)

# Threshoulding -> imBone
threshould = 1400
print(dc.pixel_array.shape)
imBone = np.zeros(dc.pixel_array.shape)
for x in range(0, dc.pixel_array.shape[0]):
    for y in range(0, dc.pixel_array.shape[1]):
        if dc.pixel_array[x, y] > threshould:
            imBone[x, y] = 1
        else:
            imBone[x, y] = 0

# Show imBone
plt.imshow(imBone, cmap=plt.cm.gray)
plt.show()

# Other method for threshoulding
imBone2 = np.zeros(dc.pixel_array.shape)
imBone2 = dc.pixel_array > threshould
plt.imshow(imBone2, cmap=plt.cm.gray)
plt.show()
