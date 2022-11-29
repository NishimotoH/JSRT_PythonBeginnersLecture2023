import pydicom
import numpy as np
import matplotlib.pyplot as plt
import time

# Read DICOM data
filename = pydicom.data.get_testdata_file("CT_small.dcm")
dc = pydicom.dcmread(filename)

# Thresholding -> imBone
threshold1 = 1400

# Original
time_sta = time.time()
imBone1 = np.zeros(dc.pixel_array.shape)
for x in range(0, dc.pixel_array.shape[0]):
    for y in range(0, dc.pixel_array.shape[1]):
        if dc.pixel_array[x, y] >= threshold1:
            imBone1[x, y] = 1
        else:
            imBone1[x, y] = 0
time_end = time.time()
tim = time_end- time_sta
print("DICOM original: "+ str(tim))

time.sleep(1.0)

# Eliminate "else"
time_sta = time.time()
imBone2 = np.zeros(dc.pixel_array.shape)
for x in range(0, dc.pixel_array.shape[0]):
    for y in range(0, dc.pixel_array.shape[1]):
        if dc.pixel_array[x, y] >= threshold1:
            imBone2[x, y] = 1
time_end = time.time()
tim = time_end- time_sta
print("DICOM No \"else\": " + str(tim))

time.sleep(1.0)


# No use "if" and "for"
time_sta = time.time()
imBone3 = (dc.pixel_array > threshold1)
time_end = time.time()
tim = time_end- time_sta
print("DICOM No \"if\" and \"for\": " + str(tim))

time.sleep(1.0)


# Big size list (5,000 x 5,000 matrix, random)
bsl = np.random.randint(0, 100, (5000, 5000))
threshold2 = 500
print("====================")
print("Big size list. Mat: " + str(bsl.shape[0]) + " x " + str(bsl.shape[1]))

# Original
time_sta = time.time()
bsl1 = np.zeros(bsl.shape)
for x in range(0, bsl.shape[0]):
    for y in range(0, bsl.shape[1]):
        if bsl[x, y] >= threshold2:
            bsl1[x, y] = 1
        else:
            bsl1[x, y] = 0
time_end = time.time()
tim = time_end- time_sta
print("Original: " + str(tim))


# Eliminate "else"
time_sta = time.time()
bsl2 = np.zeros(bsl.shape)
for x in range(0, bsl.shape[0]):
    for y in range(0, bsl.shape[1]):
        if bsl[x, y] >= threshold2:
            bsl2[x, y] = 1
time_end = time.time()
tim = time_end- time_sta
print("No \"else\": " + str(tim))

time.sleep(1.0)


# No use "if" and "for"
time_sta = time.time()
bsl3 = (bsl > threshold2)
time_end = time.time()
tim = time_end- time_sta
print("No \"if\" and \"for\": " + str(tim))
