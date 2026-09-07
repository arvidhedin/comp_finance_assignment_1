import numpy as np
import matplotlib.pyplot as plt
from assignment_1_code import S0, r, sigma, gamma, T, b, euler, milstein

np.random.seed(7)
N=500000
M_values = np.array([2, 4, 8, 16, 32, 64, 128])
dt_values = T/M_values
euler_error, milstein_error = [], []

for M in M_values:
    euler_error.append(abs(np.mean(euler(S0, r, sigma, gamma, T, M, N)) - b))
    milstein_error.append(abs(np.mean(milstein(S0, r, sigma, gamma, T, M, N)) - b))

plt.loglog(dt_values, euler_error, "o-", label="Euler")
plt.loglog(dt_values, milstein_error, "s-", label="Milstein")
plt.xlabel(r"Timestep ($\Delta t$)")
plt.ylabel("Absolute error against Black--Scholes")
plt.grid(True, which="both", ls=":")
plt.legend()
plt.tight_layout()
plt.show()
