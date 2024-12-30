import pydicom
import matplotlib.pyplot as plt

filename = pydicom.data.get_testdata_file("CT_small.dcm")
dc = pydicom.dcmread(filename)
print(dc)
plt.imshow(dc.pixel_array, cmap=plt.cm.gray)
plt.show()
