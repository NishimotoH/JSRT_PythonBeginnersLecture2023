import numpy as np
import matplotlib.pyplot as plt

# Initial values of M0 and T1
M0 = 1000
T1 = 0.3

# Function for Mz
def funcT1(M0, T1, t):
    Mz = M0 * (1 - np.exp(-t / T1))
    return Mz


# Show Mz(0.1)
t = 0.1
print("t=" + str(t) + ": Mz=" + str(funcT1(M0, T1, t)))

# Show Mz(t), t=0, 1, 2... 10
for t in range(0, 11):
    print("t=" + str(t) + ": Mz=" + str(funcT1(M0, T1, t)))

# Show Mz(t), t=0, 0.1, 0.2,... 1.0
for t in np.arange(0, 1.1, 0.1):
    print("t=" + str(t) + ": Mz=" + str(funcT1(M0, T1, t)))

# Show Mz(t), t=0, 0.05, 0.1,... 0.5
for t in np.arange(0, 0.55, 0.05):
    print(
        "t="
        + str("{:.2f}".format(t))
        + ": Mz="
        + str("{:.02f}".format(funcT1(M0, T1, t)))
    )

# Vector Mz, t=0, 0.05, 0.1,... 1.0
t = np.arange(0, 2.05, 0.05)
print(str(t))
Mz = funcT1(M0, T1, t)
print(Mz)

# Plot result
plt.plot(t, Mz)
plt.grid()
plt.show()
