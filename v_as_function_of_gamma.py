from assignment_1_code import *

gamma_values = np.linspace(0.5, 1.0, 11)
option_prices = []

for i in gamma_values:
    e = euler(S0,r,sigma,i,T,100,100000)
    option_prices.append(np.mean(e))


plt.xlabel('gamma values')
plt.ylabel('price of option')
plt.plot(gamma_values, option_prices, 'o--')
plt.grid()
plt.show()

