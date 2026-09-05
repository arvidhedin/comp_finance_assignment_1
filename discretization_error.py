from assignment_1_code import *

M_values = np.array([2, 4, 8, 16, 32, 64, 128,256])
dt_values = T / M_values
errors = []
std_errors = []
N = 10**6

for M in M_values:
    e = euler(S0, r, sigma, gamma, T, M, N)
    
    errors.append(np.abs(np.mean(e) - b))
    
    std_errors.append(np.std(e, ddof=1) / np.sqrt(N))


plt.figure(figsize=(8, 5))
plt.loglog(dt_values, errors, 's-', color='tab:red', label=r'Euler discretization error ')

ref_slope = dt_values * (errors[0] / dt_values[0])
plt.loglog(dt_values, ref_slope, 'k--', label=r'Theoretical')

plt.xlabel(r'Timestep')
plt.ylabel('Diskretidiscretization error')
plt.grid(True, which="both", ls=":")
plt.legend()
plt.show()