import numpy as np
import matplotlib.pyplot as plt
from assignment_1_code import S0, K, r, sigma, T, gamma, euler, euler_antithetic, b
import numpy as np
import matplotlib.pyplot as plt
from assignment_1_code import (
    S0, K, r, sigma, T, gamma,
    euler, euler_antithetic
)
np.random.seed(7)
M = 200
N_values = np.logspace(2, 5, 7, dtype=int)
plain_se = []
anti_se = []
plain_error = []
anti_error = []
for N in N_values:
    plain = euler(S0, r, sigma, gamma, T, M, N)
    anti = euler_antithetic(S0, r, sigma, gamma, T, M, N)
    plain_se.append(np.std(plain, ddof=1) / np.sqrt(N))
    anti_se.append(np.std(anti, ddof=1) / np.sqrt(N))
    plain_error.append(np.abs(np.mean(plain) - b))
    anti_error.append(np.abs(np.mean(anti) - b))


plt.figure(figsize=(8, 5))

plt.loglog(
    N_values, plain_se, "o--",
    label="Euler standard error"
)
plt.loglog(
    N_values, anti_se, "s--",
    label="Antithetic standard error"
)
plt.loglog(
    N_values, plain_error, "o-",
    label="Euler absolute error"
)
plt.loglog(
    N_values, anti_error, "s-",
    label="Antithetic absolute error"
)
plt.xlabel("Number of samples (N)")
plt.ylabel("Error")
plt.grid(True, which="both", ls=":")
plt.legend()
plt.tight_layout()
plt.show()
