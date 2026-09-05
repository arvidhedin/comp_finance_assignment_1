from assignment_1_code import *

N_values = np.logspace(1, 6, 9, dtype=int)
errors = []
std_errors = []
M = 1000

for N in N_values:
    e = euler(S0, r, sigma, gamma, T, M, N)
    
    errors.append(np.abs(np.mean(e) - b))
    
    std_errors.append(np.std(e, ddof=1) / np.sqrt(N))


plt.figure(figsize=(8, 5))
plt.loglog(N_values, errors, 'o-', label='measured error')
plt.loglog(N_values, std_errors, 's--', label=r'standard error')
plt.loglog(N_values, 1.0 / np.sqrt(N_values), 'k:', label=r'Theoretical error')

plt.xlabel('Number of samples (N)')
plt.ylabel('Error')
plt.grid(True, which="both", ls=":")
plt.legend()
plt.show()