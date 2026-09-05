import numpy as np
import matplotlib.pyplot as plt

S0 = 14.0
K = 15.0
r = 0.1
sigma = 0.25
T = 0.5
gamma = 1.0

# Välj M-värden (t.ex. 2, 4, 8, 16, 32, 64, 128)
M_values = np.array([2, 4, 8, 16, 32, 64, 128])
dt_values = T / M_values

N = 200000  # Räcker gott och väl tack vare Common Random Numbers
disc_errors = []

for M in M_values:
    dt = T / M
    sqrt_dt = np.sqrt(dt)
    
    S_euler = np.full(N, S0)
    W_T = np.zeros(N)
    
    for _ in range(M):
        Z = np.random.normal(0.0, 1.0, N)
        # Spara den totala Brownska rörelsen för den exakta banan
        W_T += sqrt_dt * Z
        # Euler-steget
        S_euler = S_euler + r * S_euler * dt + sigma * S_euler * sqrt_dt * Z
        S_euler = np.maximum(S_euler, 0.0)
        
    # Exakt slutpris för samma banor
    S_exact = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * W_T)
    
    payoff_euler = np.exp(-r * T) * np.maximum(S_euler - K, 0.0)
    payoff_exact = np.exp(-r * T) * np.maximum(S_exact - K, 0.0)
    
    # Bruset tar ut sig självt när vi tar differensen bana för bana!
    bias = np.abs(np.mean(payoff_euler - payoff_exact))
    disc_errors.append(bias)

# Plotta mot tidssteget dt (inte M!)
plt.figure(figsize=(8, 5))
plt.loglog(dt_values, disc_errors, 's-', color='tab:red', label='Euler bias |V_Euler - V_exakt|')

# Teoretisk referenslinje: O(dt^1)
ref_line = dt_values * (disc_errors[-1] / dt_values[-1])
plt.loglog(dt_values, ref_line, 'k--', label=r'Teoretisk svag ordning $\mathcal{O}(\Delta t^1)$')

plt.xlabel(r'Tidssteg ($\Delta t$)')
plt.ylabel('Diskretiseringsfel (Bias)')
plt.title(r'Del 2: Diskretiseringsfel som funktion av tidssteg $\Delta t$')
plt.grid(True, which="both", ls=":")
plt.legend()
plt.tight_layout()
plt.show()