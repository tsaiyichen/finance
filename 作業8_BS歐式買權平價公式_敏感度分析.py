import pandas as pd
import numpy as np
import scipy
import scipy.stats as si
import matplotlib.pyplot as plt
#(1)
T_list = [1, 0.9, 0.5, 0.3, 0.1]

S, X, r, sigma, q = 90, 100, 0.01, 0.3, 0

for T in T_list:
    d1 = (np.log(S/X) + (r - q + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    c = (S * np.exp((-q) * T) * si.norm.cdf(d1)) - (X * np.exp((-r) * T) * si.norm.cdf(d2))
    print(f"T: {T}, Call: {c.round(4)}")

#(2)
T_list = []
C_list = []
for i in range(10, 0, -1):
    T = i / 10
    T_list.append(T)
    d1 = (np.log(S/X) + (r - q + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    c = (S * np.exp((-q) * T) * si.norm.cdf(d1)) - (X * np.exp((-r) * T) * si.norm.cdf(d2))
    C_list.append(c)

plt.plot(T_list, C_list)
plt.xlabel("T")
plt.ylabel("C")
plt.savefig("HW8", dpi=300, bbox_inches='tight')
plt.show()