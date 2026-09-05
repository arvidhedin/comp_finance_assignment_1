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

