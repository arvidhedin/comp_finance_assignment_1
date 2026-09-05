import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
from numpy import exp, log, sqrt


S0 = 14
K = 15
r = 0.1
sigma = 0.25
T = 0.5
gamma = 1
S_t = S0




def bsexact(sigma: float, R: float, K: float, T: float, s: float):
    d1 = (log(s/K)+(R+0.5*sigma**2)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    F = 0.5*s*(1+erf(d1/sqrt(2)))-exp(-R*T)*K*0.5*(1+erf(d2/sqrt(2)))
    return F

def euler(S0,r,sigma,gamma,T,M,N):
    dt = T / M
    S = np.full(N,S0)
    
    for i in range(M):
        Z = np.random.normal(0,1,N)
        S = S+r *S*dt + sigma *(S**gamma)*np.sqrt(dt)*Z

    return np.exp(-r * T)*np.maximum(S-K, 0)

gamma_values = np.linspace(0.5, 1.0, 11)
option_prices = []

for i in gamma_values:
    e = euler(S0,r,sigma,i,T,100,100000)
    option_prices.append(np.mean(e))


plt.xlabel('gamma values')
plt.ylabel('price of option')
plt.plot(gamma_values, option_prices, 'o--')
plt.show()

"""
N_values = np.logspace(1, 6, 9, dtype=int)
errors = []
std_errors = []
M = 1000

for N in N_values:
    e = euler(S0, r, sigma, gamma, T, M, N)
    
    errors.append(np.abs(np.mean(e) - b))
    
    std_errors.append(np.std(e, ddof=1) / np.sqrt(N))


plt.figure(figsize=(8, 5))
plt.loglog(N_values, errors, 'o-', label='Uppmätt fel |V_MC - V_exakt|')
plt.loglog(N_values, std_errors, 's--', label=r'Standardfel ($\hat{\sigma}/\sqrt{N}$)')
plt.loglog(N_values, 1.0 / np.sqrt(N_values), 'k:', label=r'Teoretisk referens $\mathcal{O}(N^{-1/2})$')

plt.xlabel('Antal samplingbanor (N)')
plt.ylabel('Fel')
plt.title('Del 1: Samplingsfel som funktion av N')
plt.grid(True, which="both", ls=":")
plt.legend()
plt.show()


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
plt.loglog(dt_values, errors, 's-', color='tab:red', label=r'Euler diskretiseringsfel |$\bar{V} - V_{exakt}$|')

# Teoretisk referenslinje för svag konvergens: O(dt^1)
ref_slope = dt_values * (errors[0] / dt_values[0])
plt.loglog(dt_values, ref_slope, 'k--', label=r'Teoretisk referens $\mathcal{O}(\Delta t^1)$')

plt.xlabel(r'Tidssteg ($\Delta t$)')
plt.ylabel('Diskretiseringsfel (Bias)')
plt.title(r'Del 2: Diskretiseringsfel som funktion av tidssteg $\Delta t$')
plt.grid(True, which="both", ls=":")
plt.legend()
plt.tight_layout()
plt.show()



"""