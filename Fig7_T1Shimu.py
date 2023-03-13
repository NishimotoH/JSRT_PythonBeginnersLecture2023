import numpy as np
import matplotlib.pyplot as plt

# M0 and T1 values
M0 = 1000
T1_1 = 0.3
T1_2 = 0.6

# Function


def funcT1(M0, T1, t):
    Mz = M0 * (1 - np.exp(-t/T1))
    return Mz


# t=0, 0.05, 0.1,... 3.0
t = np.arange(0, 3.05, 0.05)
Mz_1 = funcT1(M0, T1_1, t)
Mz_2 = funcT1(M0, T1_2, t)

# Plot result
plt.plot(t, Mz_1)
plt.plot(t, Mz_2, linestyle="dashed")
plt.grid()
plt.show()
